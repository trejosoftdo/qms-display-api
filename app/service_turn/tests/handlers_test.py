"""Service Turn Handlers tests
"""

import unittest
from unittest.mock import Mock, patch
from fastapi import status
from requests import Response
from app.service_turn.tests.fakes import (
    ServiceTurnStatusItemFactory,
)
from app.service_turn.handlers import get_turns_status_table


class HandlersTest(unittest.TestCase):
    """Service Turn Handlers functions tests"""

    def setUp(self):
        self.application = "test-application"
        self.authorization = "Bearer test-access-token"

    @patch("app.service_turn.mappers.map_turn_status_item")
    @patch("app.service_turn.api.get_turns_status_table")
    def test_get_turns_status_table(
        self, get_turns_status_table_mock, map_turn_status_item_mock
    ):
        """get_turns_status_table: It gets the service turns status table"""
        json_data = [{"queueName": "Test Queue Name"}]
        get_turns_status_table_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value=json_data),
        )
        map_turn_status_item_mock.return_value = ServiceTurnStatusItemFactory.build()
        response = get_turns_status_table(self.application, self.authorization)
        self.assertEqual(response, [map_turn_status_item_mock.return_value])
        get_turns_status_table_mock.assert_called_with(
            self.application, self.authorization
        )
        map_turn_status_item_mock.assert_called_with(json_data[0])


if __name__ == "__main__":
    unittest.main()
