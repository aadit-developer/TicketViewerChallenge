import requests


def get_tickets_data(ticket_id = None):
    credentials = 'aaditdim@usc.edu/token', 'bXKle4a7KdcqYUYTNo92yQzwob6O6GGth0XtPzsi'
    session = requests.Session()
    session.auth = credentials
    zendesk = 'https://zccaaditdim.zendesk.com'

    if not ticket_id:
        url = f'{zendesk}/api/v2/tickets'
        try:
            response = session.get(url)
            data = response.json()
        except Exception as e:
            print("Fetching tickets data failed because of "+str(e))
        finally:
            session.close()

        if response.status_code != 200:
            print(f'Error with status code {response.status_code}')
            exit()
        return data['tickets']
    else:
        url = f'{zendesk}/api/v2/tickets/{ticket_id}'
        try:
            response = session.get(url)
            data = response.json()
        except Exception as e:
            print("Fetching single ticket data failed because of "+str(e))
        finally:
            session.close()

        if response.status_code != 200:
            print(f'Error with status code {response.status_code}')
            exit()
        return [data['ticket']]


def pagination(tickets, page=0):
    tickets_count = len(tickets)
    has_next = False
    has_prev = False
    res = tickets[page*25: page*25+25]
    if tickets_count > (page+1)*25:
        has_next = True
    if page > 0:
        has_prev = True
    return res, has_next, has_prev


def viewer():
    print('Welcome to the ticket viewer')
    print("Type 'menu' to view options or enter any key to exit")
    inp = str(input())
    if inp.lower() != 'menu':
        exit()

    print("\tSelect view options: \n"
          "\t* Press 1 to view all tickets \n"
          "\t* Press 2 to view a ticket \n"
          "\t* Enter any key to exit")
    inp = str(input())
    if inp == '1':
        tickets = get_tickets_data()
    elif inp == '2':
        print('Enter ticket number: ')
        ticket_id = str(input())
        tickets = get_tickets_data(ticket_id)

    page = 0
    while True:
        try:
            res, has_next, has_prev = pagination(tickets, page)
        except Exception as e:
            print("Error Loading Page because of "+str(e))

        print('ID'.ljust(10),'Created at'.ljust(30), 'Status'.ljust(10), 'Message')
        for ticket in res:
            subject = ticket['subject']
            if len(subject) > 20:
                subject = subject[:20] + '...'
            msg = f"Ticket with subject {subject} opened by " \
                  f"{ticket['requester_id']}"
            status = ticket['status'] or ''
            created_at = ticket['created_at'] or ''
            ticket_id = str(ticket['id'])
            print(ticket_id.ljust(10), created_at.ljust(30), status.ljust(10), msg)
        print("\n\tSelect option")
        if has_prev:
            print("\t* Type 'prev' for previous page")
        if has_next:
            print("\t* Type 'next' for next page")
        print("\t* Press any key to exit")
        inp = str(input())
        if inp == 'prev' and has_prev:
            page -= 1
        elif inp == 'next' and has_next:
            page += 1
        else:
            exit()


if __name__ == '__main__':
    viewer()