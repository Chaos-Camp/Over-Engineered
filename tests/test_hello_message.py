import unittest
from data.messages.hello_message import HelloMessageProduction, HelloMessageDebug


class TestHelloMessage(unittest.TestCase):
    def test_hello_message_production_content(self):
        message = HelloMessageProduction()
        self.assertEqual(message.get_content(), "Hello, World!")

    def test_hello_message_debug_content(self):
        message = HelloMessageDebug()
        self.assertEqual(message.get_content(), "Hello, World! [DEBUG MODE]")
