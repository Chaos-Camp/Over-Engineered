import unittest
from unittest.mock import patch, Mock
from services.display_service import DisplayService


class TestDisplayService(unittest.TestCase):
    @patch("services.display_service.MessageFactory")
    def test_display(self, MockMessageFactory):
        # Mock the message factory and its behavior
        mock_message = Mock()
        mock_message.get_content.return_value = "Hello, World!"

        MockMessageFactory.return_value.create_message.return_value = mock_message

        # Test display
        service = DisplayService()
        with patch("builtins.print") as mock_print:
            service.display()
            mock_print.assert_called_once_with("Hello, World!")


if __name__ == "__main__":
    unittest.main()
