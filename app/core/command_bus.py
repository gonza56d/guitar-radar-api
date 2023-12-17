from pymessagebus import CommandBus


class APICommandBus(CommandBus):

    def __init__(self, handlers: dict):
        super().__init__()
        for command, handler in handlers.items():
            self.add_handler(command, handler)
