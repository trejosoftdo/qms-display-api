"""Service Turn API models
"""

from typing import List
from pydantic import BaseModel


class ServiceTurnStatusItem(BaseModel):
    """Service Turn Status Item data
    """

    ticketNumber: str
    queueName: str
    statusName: str
    statusCode: str

class ServiceTurnAudioResponse(BaseModel):
    """Service Turn Audio
    """

    name: str

ServiceTurnsStatusTableResponse = List[ServiceTurnStatusItem]
