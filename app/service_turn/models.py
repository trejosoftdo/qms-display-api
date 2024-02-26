"""Service Turn API models
"""

from typing import List
from pydantic import BaseModel


class ServiceTurnStatusItem(BaseModel):
    """Service Turn Status Item data

    Args:
        BaseModel (class): Base model class
    """

    ticketNumber: str
    queueName: str
    statusName: str
    statusCode: str


ServiceTurnsStatusTableResponse = List[ServiceTurnStatusItem]
