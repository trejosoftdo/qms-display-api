"""Service Turn fakes"""

from pydantic_factories import ModelFactory
from app.service_turn.models import (ServiceTurnStatusItem,)


class ServiceTurnStatusItemFactory(ModelFactory):
    """Service Turn Status Item factory"""

    __model__ = ServiceTurnStatusItem
