from config import settings
from data.messages import hello_message


class MessageFactory:
    def create_message(self):
        if settings.APP_MODE == "PRODUCTION":
            return hello_message.HelloMessageProduction()
        else:
            return hello_message.HelloMessageDebug()
