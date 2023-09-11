class AbstractHelloMessage:
    def get_content(self):
        raise NotImplementedError()


class HelloMessageProduction(AbstractHelloMessage):
    def get_content(self):
        return "Hello, World!"


class HelloMessageDebug(AbstractHelloMessage):
    def get_content(self):
        return "Hello, World! [DEBUG MODE]"
