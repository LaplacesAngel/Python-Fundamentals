class Attendee:
    'Common base class for all attendees'

    def __init__(self, name = "", tickets = ""):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self, n=1):
        self.tickets += n
        print('{}s tickets increased to {}'.format(self.name, self.tickets))


attendee1 = Attendee('Paul', 15)
attendee2 = Attendee()

attendee1.displayAttendee()
attendee1.addTicket()

attendee2.displayAttendee()