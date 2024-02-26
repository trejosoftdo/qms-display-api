"""Service Turn API Router tests
"""

import unittest
from unittest.mock import Mock, patch
from requests import Response
from fastapi import status
from fastapi.testclient import TestClient
from app import main, constants
from app.service_turn.constants import TURNS_STATUS_TABLE_PATH
from app.service_turn.tests.fakes import ServiceTurnStatusItemFactory


# pylint: disable=R0801

class RouterTest(unittest.TestCase):
    """Service Turn Router functions tests"""

    def setUp(self):
        self.client = TestClient(main.app)
        self.application = "test-application"
        self.authorization = "Bearer test-token"
        self.headers = {
            "application": self.application,
            "authorization": self.authorization,
        }
        self.valid_token_response = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(
                return_value={
                    "data": {
                        "isValid": True,
                        "isAuthorized": True,
                    }
                }
            ),
        )

    @patch("app.auth.api.validate_token")
    @patch("app.service_turn.handlers.get_turns_status_table")
    def test_get_categories(self, get_turns_status_table_mock, validate_token_mock):
        """get_turns_status_table: It should be able to get the turns status table"""
        validate_token_mock.return_value = self.valid_token_response

        get_turns_status_table_mock.return_value = [ServiceTurnStatusItemFactory.build()]
        response = self.client.get(
            f"{constants.SERVICE_TURNS_ROUTE_PREFIX}{TURNS_STATUS_TABLE_PATH}",
            headers=self.headers,
        )
        self.assertEqual(response.json(), get_turns_status_table_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        get_turns_status_table_mock.assert_called()


if __name__ == "__main__":
    unittest.main()
