"""Service Turn API router
"""

from fastapi import APIRouter, Depends, Header
from fastapi.responses import FileResponse
from .. import helpers
from .. import constants
from .. import responses
from .constants import (
    TAGS,
    GET_TURNS_STATUS_TABLE_OPERATION_ID,
    GET_TURN_AUDIO_OPERATION_ID,
    TURNS_STATUS_TABLE_PATH,
    TURN_AUDIO_PATH,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    TURNS_STATUS_TABLE_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_SERVICE_TURNS_SCOPE))],
    tags=TAGS,
    operation_id=GET_TURNS_STATUS_TABLE_OPERATION_ID,
    response_model=models.ServiceTurnsStatusTableResponse,
    responses=responses.responses_descriptions,
)
def get_turns_status_table(
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
) -> models.ServiceTurnsStatusTableResponse:
    """Gets turns status table for the application in context"""
    return handlers.get_turns_status_table(application, authorization)


@router.get(
    TURN_AUDIO_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_SERVICE_TURNS_SCOPE))],
    tags=TAGS,
    operation_id=GET_TURN_AUDIO_OPERATION_ID,
    response_class=FileResponse,
    responses=responses.responses_descriptions,
)
def get_turn_audio(turn_name: str) -> FileResponse:
    """Gets the audio of a turn"""
    path = handlers.get_turn_audio(turn_name)
    return FileResponse(path, filename="audio.mp3", media_type="audio/mpeg")
