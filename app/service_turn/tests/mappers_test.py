"""Service Turn API Handlers tests
"""

import unittest
from app.service_turn.mappers import map_turn_status_item


class MappersTest(unittest.TestCase):
    """Service Turn Mappers functions tests"""

    def setUp(self):
        self.status_item_data = {
            "ticketNumber": "test-ticket-number",
            "queueName": "Test queue name",
            "statusName": "Test status name",
            "statusCode": "Test status code",
        }

    def test_map_turn_status_item(self):
        """map_turn_status_item: It maps service turn status item correctly"""
        response = map_turn_status_item(self.status_item_data)
        self.assertEqual(response.ticketNumber, self.status_item_data["ticketNumber"])
        self.assertEqual(response.queueName, self.status_item_data["queueName"])
        self.assertEqual(response.statusName, self.status_item_data["statusName"])
        self.assertEqual(response.statusCode, self.status_item_data["statusCode"])


if __name__ == "__main__":
    unittest.main()
