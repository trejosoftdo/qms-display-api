"""Service Turn API handlers
"""

from . import models
from . import api
from . import mappers


def get_turns_status_table(
    application: str, authorization: str
) -> models.ServiceTurnsStatusTableResponse:
    """Gets turns status table for the application in context

    Args:
        application (str): The application in context.
        authorization (str): The access token for the user in context

    Returns:
        models.ServiceTurnsStatusTableResponse: Turns status table response
    """
    response = api.get_turns_status_table(application, authorization)
    status_table = response.json()
    return list(map(mappers.map_turn_status_item, status_table))
