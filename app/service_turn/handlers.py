"""Service Turn API handlers
"""

import io
from . import models
from . import api
from . import mappers
from .text_to_audio import text_to_audio


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


def get_turn_audio(turn_name: str) -> io.BytesIO:
    """Gets the audio of the turn name

    Args:
        turn_name (str): The turn name

    Returns:
        io.BytesIO: The turn audio
    """
    return text_to_audio(turn_name)
