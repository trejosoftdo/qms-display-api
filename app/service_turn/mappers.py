"""Service Turn API mappers
"""

from . import models


def map_turn_status_item(item: dict) -> models.ServiceTurnStatusItem:
    """Maps a service turn status item from the given data

    Args:
        item (dict): turn status data

    Returns:
        models.ServiceTurnStatusItem: Service Turn status item
    """
    return models.ServiceTurnStatusItem(
        ticketNumber=item.get("ticketNumber"),
        queueName=item.get("queueName"),
        statusName=item.get("statusName"),
        statusCode=item.get("statusCode"),
    )
