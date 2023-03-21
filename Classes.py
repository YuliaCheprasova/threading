import datetime


class wish():
    """The class that generates wish of a person through dialogue"""

    def subject(self) -> str:
        """The method that determines a subject of sending"""

        print('Write who you want to send on a journey, for example, hateful man')
        who = input()
        return who

    def place(self, who: str) -> str:
        """The method that determines a place of sending"""

        print('I want to send a ', who, ' to (write any place in the world as the sending place, for example, hell) ')
        where = input()
        return where

    def time(self, who: str, where: str) -> int:
        """The method that determines the date of sending
        and calculates the difference between it and the present time"""

        print(
            'I want to send a ', who, ' to ', where, ' in '
            '(write the sending date you want in the year-month-date format, for example, 2028-06-09) ')
        when = input()
        when = datetime.datetime.strptime(when, '%Y-%m-%d')
        when = when.date()
        now = datetime.datetime.now()
        now = now.date()
        tdelta = when - now
        tdelta = tdelta.days
        return tdelta


class time_machine():
    """The class that simulates actions of the time machine"""

    def sending(self, mas):
        """The method that generates the sending message"""

        if mas[2] >= 0:
            print('I am sending a ', mas[0], ' to ', mas[1], ' ', str(mas[2]), ' days forward')
        else:
            print('I am sending a ', mas[0], ' to ', mas[1], ' ', str(-mas[2]), ' days ago')




"""def __main__():
    a = wish()
    b = time_machine()
    who = a.subject()
    where = a.place(who)
    when = a.time(who, where)
    b.request(who, where, when)
    b.result()"""
