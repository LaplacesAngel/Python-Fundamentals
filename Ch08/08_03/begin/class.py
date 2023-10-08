class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{}s tickets increased to {}'.format(self.name, self.tickets))


attendee1 = Attendee('Paul', 15)

attendee1.displayAttendee()
attendee1.addTicket()