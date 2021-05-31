import sys
import logging
import os
from snoop.tracer import Tracer
import snoop


LOGS_FOLDER = '.live_coder/'
if not os.path.exists(LOGS_FOLDER):
    os.mkdir(LOGS_FOLDER)


def sanitize(filename):
    return ''.join([c for c in filename if c.isalpha() or c.isdigit() or c == ' '])


log_path = LOGS_FOLDER + sanitize(
    ' '.join(
        (' '.join(sys.argv)).split()
    ))[:255] + '.txt'


# empty log file at start
with open(log_path, 'w') as f:
    f.write(' '.join(sys.argv) + '\n')
logging.basicConfig(filename=log_path)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

snoop.install(
    builtins=False,
    out=logger.info,
    prefix='4EmR7TzOvAICFVCp2wcU',
)


class InfDefaultTracer(Tracer):
    config = snoop.config

    def __init__(self, *args, **kwargs):
        kwargs['depth'] = kwargs.get('depth', float('inf'))
        super().__init__(*args, **kwargs)


snoop = InfDefaultTracer
