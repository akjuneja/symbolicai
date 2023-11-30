from typing import List

from ...base import Engine


class UserInputEngine(Engine):
    def __init__(self):
        super().__init__()

    def id(self) -> str:
        return 'userinput'

    def forward(self, argument):
        msg           = argument.prop.processed_input
        kwargs        = argument.kwargs
        input_handler = kwargs['input_handler'] if 'input_handler' in kwargs else None
        if input_handler:
            input_handler((msg,))

        mock = kwargs['mock'] if 'mock' in kwargs else False
        if mock: # mock user input
            print(msg, end='') # print prompt
            rsp = mock
        else:
            rsp = input(msg)

        output_handler = kwargs['output_handler'] if 'output_handler' in kwargs else None
        if output_handler:
            output_handler(rsp)

        metadata = {}
        if 'metadata' in kwargs and kwargs['metadata']:
            metadata['kwargs'] = kwargs
            metadata['input']  = msg
            metadata['output'] = None

        return [rsp], metadata

    def prepare(self, argument):
        argument.prop.processed_input = argument.prop.prompt
