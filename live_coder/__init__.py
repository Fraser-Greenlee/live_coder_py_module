import sys
import os
import shutil
from contextlib import redirect_stdout, redirect_stderr
import io
from snoop.tracer import Tracer
import snoop


KEY = '4EmR7TzOvAICFVCp2wcU'

LOGS_FOLDER = '.live_coder/'
if not os.path.exists(LOGS_FOLDER):
    os.mkdir(LOGS_FOLDER)


def sanitize(filename):
    return ''.join([c for c in filename if c.isalpha() or c.isdigit() or c == ' '])


log_fname_base = sanitize(' '.join([v[-30:] for v in sys.argv]))[-75:]
if not log_fname_base:
    log_fname_base = 'NO_ARGS'

log_fname = log_fname_base + '.txt'
log_path = LOGS_FOLDER + log_fname

# empty log file at start
if os.path.exists(log_path):
    with open(log_path, 'w') as f:
        f.write(' '.join(sys.argv) + '\n')

snoop.install(builtins=False, prefix=KEY, color=False)


class InfDefaultTracer(Tracer):
    config = snoop.config

    def __init__(self, *args, **kwargs):
        kwargs['depth'] = kwargs.get('depth', float('inf'))
        super().__init__(*args, **kwargs)

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
            with open(log_path, 'w') as fd:
                f.seek(0)
                shutil.copyfileobj(f, fd)
            return result

        return inner


snoop = InfDefaultTracer
