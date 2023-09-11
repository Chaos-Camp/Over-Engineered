import unittest
from factories.message_factory import MessageFactory
from data.messages.hello_message import HelloMessageProduction, HelloMessageDebug
from config import settings


class TestMessageFactory(unittest.TestCase):
    def test_create_message_production(self):
        settings.APP_MODE = "PRODUCTION"
        factory = MessageFactory()
        message = factory.create_message()
        self.assertIsInstance(message, HelloMessageProduction)

    
    def test_create_message_debug(self):
        settings.APP_MODE = "DEBUG"
        factory = MessageFactory()
        message = factory.create_message()
        self.assertIsInstance(message, HelloMessageDebug)
