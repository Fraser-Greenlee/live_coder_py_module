import sys
import os
import shutil
import pathlib
from contextlib import redirect_stdout, redirect_stderr
import io
from snoop.tracer import Tracer
import snoop


KEY = '4EmR7TzOvAICFVCp2wcU'
snoop.install(builtins=False, prefix=KEY, color=False)


def get_ignore_path(workspace_path):
    if workspace_path:
        python_path = sys.executable
        if python_path.startswith(workspace_path):
            ignore_dir = python_path[len(workspace_path):].strip('/').split('/')[0]
            return os.path.join(workspace_path, ignore_dir)


def current_working_dir():
    return pathlib.Path().absolute().as_posix()


WORKSPACE_PATH = os.environ.get('LC_WORKSPACE_PATH', current_working_dir())
IGNORE_PATH = get_ignore_path(WORKSPACE_PATH)
TRACE_ALL_CODE = os.environ.get('LC_TRACE_ALL_CODE', False)


def sanitize(filename):
    return ''.join([c for c in filename if c.isalpha() or c.isdigit() or c == ' '])


def prepare_logs(logs_folder):
    if not os.path.exists(logs_folder):
        os.mkdir(logs_folder)

    log_fname_base = sanitize(' '.join([v[-30:] for v in sys.argv]))[-75:]
    if not log_fname_base:
        log_fname_base = 'NO_ARGS'

    log_fname = log_fname_base + '.txt'
    log_path = logs_folder + log_fname

    # empty log file at start
    if os.path.exists(log_path):
        with open(log_path, 'w') as f:
            f.write(' '.join(sys.argv) + '\n')

    return log_path


LOGS_FOLDER = '.live_coder/'
LOG_PATH = prepare_logs(LOGS_FOLDER)


class InfDefaultTracer(Tracer):
    config = snoop.config

    def __init__(self, *args, **kwargs):
        kwargs['depth'] = kwargs.get('depth', float('inf'))
        super().__init__(*args, **kwargs)

    @staticmethod
    def _is_non_workspace_frame(frame):
        path: str = frame.f_code.co_filename
        if WORKSPACE_PATH and not path.startswith(WORKSPACE_PATH):
            return True
        if IGNORE_PATH and path.startswith(IGNORE_PATH):
            return True
        return False

    def _is_internal_frame(self, frame):
        return super()._is_internal_frame(frame) or (self._is_non_workspace_frame(frame) and not TRACE_ALL_CODE)

    def __call__(self, function):
        snoop_function = super().__call__(function)

        def inner(*args, **kwargs):
            f = io.StringIO()
            try:
                if os.environ.get('IGNORE_STDOUT', False):
                    with redirect_stderr(f):
                        result = snoop_function(*args, **kwargs)
                else:
                    with redirect_stdout(f), redirect_stderr(f):
                        result = snoop_function(*args, **kwargs)
            except:
                result = None
            with open(LOG_PATH, 'w') as fd:
                f.seek(0)
                shutil.copyfileobj(f, fd)
            return result

        return inner


snoop = InfDefaultTracer
