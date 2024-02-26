"""Service Turn API helpers
"""

import requests
from .. import environment
from .. import constants
from .constants import SERVICE_TURNS_STATUS_TABLE_EXTERNAL_PATH


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.core_api_key,
    }


def get_turns_status_table(application: str, authorization: str) -> requests.Response:
    """Gets turns status table for the application in context

    Args:
        application (str): The application in context.
        authorization (str): The access token for the user in context

    Returns:
        requests.Response: The response from the core api.
    """
    url = f"{environment.core_api_base_url}{SERVICE_TURNS_STATUS_TABLE_EXTERNAL_PATH}"
    headers = {
        **get_common_headers(),
        "application": application,
        "authorization": authorization,
    }
    return requests.get(
        url, headers=headers, timeout=constants.TIMEOUT
    )
