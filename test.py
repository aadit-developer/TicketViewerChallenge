import unittest
import ticketsViewer
import json

class TicketsViewerTestCase(unittest.TestCase):
    def test_ticket_with_id(self):
        ticket_data = ticketsViewer.get_tickets_data(1)
        with open("test_data/single_ticket_id_1.json","r") as f:
            self.assertEqual(json.loads(f.read()),ticket_data)

    def test_all_tickets(self):
        ticket_data = ticketsViewer.get_tickets_data()
        with open("test_data/all_id_tickets.json","r") as f:
            self.assertEqual(json.loads(f.read()),ticket_data)

    def test_pagination_on_first_page(self):
        tickets = ticketsViewer.get_tickets_data()
        res, has_next, has_prev = ticketsViewer.pagination(tickets, 0)
        self.assertEqual(has_prev, False)

    def test_pagination_on_last_page(self):
        tickets = ticketsViewer.get_tickets_data()
        last_page = len(tickets)//4
        res, has_next, has_prev = ticketsViewer.pagination(tickets, last_page)
        self.assertEqual(has_next, False)


if __name__ == '__main__':
    unittest.main()
