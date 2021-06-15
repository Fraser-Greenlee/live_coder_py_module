

from snoop.formatting import DefaultFormatter


class JsonFormatter(DefaultFormatter):
    '''
        Currently I just get truncated string representations of variables.
        This is fast but means users can't inspect variabels.
        Would be good to try log a summary of the object as json.

        e.g.
        INFO:root:4EmR7TzOvAICFVCp2wcU     11:04:04.09 .......... a = 8
        INFO:root:4EmR7TzOvAICFVCp2wcU     {"a": {" value": 8}}

        INFO:root:4EmR7TzOvAICFVCp2wcU     11:04:04.09 .......... a = tensor([[8,4,,,]])
        INFO:root:4EmR7TzOvAICFVCp2wcU     {"a": {" value": tensor([[8,4,,,]]), 0: {0:, 1:, 2:},,,}}
    '''
    pass
