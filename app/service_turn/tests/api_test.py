"""Service Turn Helpers tests
"""

import unittest
from unittest.mock import Mock, patch
from app.constants import (
    TIMEOUT,
    CONTENT_TYPE_JSON,
)
from app.service_turn.api import get_turns_status_table
from app.service_turn.constants import SERVICE_TURNS_STATUS_TABLE_EXTERNAL_PATH

# pylint: disable=R0801

BASE_URL = "http://base-url.test"
TEST_API_KEY = "test-api-key"

mock_environment = Mock(
    core_api_base_url=BASE_URL,
    core_api_key=TEST_API_KEY,
)


class ServiceTurnAPITest(unittest.TestCase):
    """Service Turn API functions tests"""

    def setUp(self):
        self.base_path = BASE_URL
        self.common_headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "api_key": mock_environment.core_api_key,
        }
        self.application = "test-application"
        self.authorization = "Bearer test-token"

    @patch("app.service_turn.api.requests.get")
    @patch(
        "app.service_turn.api.environment",
        mock_environment,
    )
    def test_get_turns_status_table(self, get_mock):
        """get_turns_status_table: It gets the service turns status table"""
        get_mock.return_value = Mock(status_code=200)
        response = get_turns_status_table(self.application, self.authorization)
        self.assertEqual(response, get_mock.return_value)
        get_mock.assert_called_with(
            f"{self.base_path}{SERVICE_TURNS_STATUS_TABLE_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": self.application,
                "authorization": self.authorization,
            },
            timeout=TIMEOUT,
        )


if __name__ == "__main__":
    unittest.main()
