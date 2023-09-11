from factories.message_factory import MessageFactory


class DisplayService:
    def __init__(self):
        self.message_factory = MessageFactory()

    def display(self):
        message = self.message_factory.create_message()
        print(message.get_content())
