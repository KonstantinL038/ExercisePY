# Опишите здесь классы Load, Meeting, User, Date.
import datetime


class Load:
    """load"""
    meet_2 = []
    person_meet = []

    @classmethod
    def write(cls, fl_meet, fl_pers, fl_pers_meet):

        with open(fl_pers_meet, 'r', encoding='utf-8') as file_3:
            first_line = file_3.readline()
            for k in file_3:
                person_meet = k.strip().split(';')[:-1]
                if person_meet not in cls.person_meet:
                    cls.person_meet.append(person_meet)

        with open(fl_pers, 'r', encoding='utf-8') as file_2:
            first_line = file_2.readline()
            for k in cls.person_meet:
                for j in file_2:
                    person = User(*j.strip().split(';')[:-1])
                    cls.meet_2.append(person)

        with open(fl_meet, 'r', encoding='utf-8') as file_1:
            first_line = file_1.readline()
            for i in file_1:
                meet = Meeting(*i.strip().split(';')[:-1])
                for k in cls.person_meet:
                    for j in cls.meet_2:
                        if int(k[0]) == int(meet.id):
                            if int(k[1]) == int(j.id):
                                meet.add_person(j)


class Date:
    """date"""
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    day_months = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, user_date: str):
        if self.check(user_date):
            self.__date = user_date
        else:
            self.__date = None
            print('ошибка')

    @staticmethod
    def check_leap(year):
        return (year % 4 == 0 or year % 400 == 0) and year % 100 != 0

    @staticmethod
    def check(user_date):
        """ho"""
        flag = False
        if user_date.find('.') == -1:  # Если неправильный формат ввода
            return flag
        else:
            my_list = user_date.split('.')

            if len(my_list) == 3:  # если 3 цифры
                if len(my_list[0]) == 2 and len(my_list[1]) == 2 and len(my_list[2]) == 4:  # сопоставим кол-во элем
                    if my_list[0].isdigit() and my_list[1].isdigit() and my_list[2].isdigit():  # если даты состоят
                        # из цифр
                        if 1 <= int(my_list[1]) <= 12:  # если количество месяцев меньше 12
                            my_index = int(my_list[1]) - 1

                            if my_index == 1:  # Февраль
                                if Date.check_leap(int(my_list[2])):
                                    amount = Date.day_months[my_index][1]
                                else:
                                    amount = Date.day_months[my_index][0]
                            else:
                                amount = Date.day_months[my_index]

                            if 1 <= int(my_list[0]) <= amount:  # Проверяем кол-во дней
                                flag = True
        return flag

    @property
    def date(self):
        """getter"""
        if self.__date is not None:
            middle_list = self.__date.split('.')
            return '{} {} {} г.'.format(int(middle_list[0]), Date.months[int(middle_list[1]) - 1], middle_list[2])
        else:
            return self.__date

    @date.setter
    def date(self, value):
        """setter"""
        if self.check(value):
            self.__date = value
        else:
            self.__date = None
            print('ошибка')

    def to_timestamp(self):
        """return the amount of seconds"""
        my_time = datetime.datetime.strptime(self.__date, '%d.%m.%Y')
        dt_start = datetime.datetime(1970, 1, 1)
        return int((my_time - dt_start).total_seconds())

    def __lt__(self, other):
        """operation of <"""
        return self.to_timestamp() < other.to_timestamp()

    def __le__(self, other):
        """operation of <="""
        return self.to_timestamp() <= other.to_timestamp()

    def __eq__(self, other):
        """operation of =="""
        return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        """operation of !="""
        return self.to_timestamp() != other.to_timestamp()

    def __gt__(self, other):
        """operation of >"""
        return self.to_timestamp() > other.to_timestamp()

    def __ge__(self, other):
        """operation of >="""
        return self.to_timestamp() >= other.to_timestamp()

    def __repr__(self):
        """str representation"""
        return '{}'.format(self.date)


# Опишите здесь класс User.
class User:
    """This class represent data about user.
    Has such positional attributes as: id, nick_name, first_name
    Has such named attributes as: last_name, middle_name, gender
    And has a method: update"""

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """Initializing attributes"""
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id, nick_name, first_name, last_name='', middle_name='', gender=''):
        """Renew the information about a user"""
        if id != 0:
            self.id = id
        if nick_name != '':
            self.nick_name = nick_name
        if first_name != '':
            self.first_name = first_name
        if last_name != '':
            self.last_name = last_name
        if middle_name != '':
            self.middle_name = middle_name
        if gender != '':
            self.gender = gender

    def __str__(self):
        """Output depending on the number of attributes"""
        not_important = [self.last_name, self.middle_name, self.gender]
        output = 'ID: {} LOGIN: {} NAME: {}'.format(self.id, self.nick_name, self.first_name)
        if not_important[0] != '':
            output = 'ID: {} LOGIN: {} NAME: {} {}'.format(self.id, self.nick_name, self.last_name, self.first_name)
        if not_important[1] != '':
            output = output + ' {}'.format(self.middle_name)
        if not_important[2] != '':
            output = output + ' GENDER: {}'.format(self.gender)

        while '  ' in output:
            output = output.replace('  ', ' ')

        return output

    def __repr__(self):
        """adds to the list nick_names"""
        return self.nick_name


class Meeting:
    """meet"""
    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id  # ID
        self.date = Date(date)  # Дата
        self.title = title  # Название мероприятия
        self.employees = []  # Список сотрудников
        Meeting.lst_meeting.append(self)

    def add_person(self, person):
        """добавить сотрудника person"""
        if person not in self.employees:
            self.employees.append(person)

    @classmethod
    def total(cls):
        """Общее количество всех участников на всех конференциях."""
        total = 0
        for i in Meeting.lst_meeting:
            total += len(i.employees)
        return total

    @classmethod
    def count_meeting(cls, date):
        """Количество встреч на указанную дату date"""
        total = 0
        if type(date) == Date:
            for i in cls.lst_meeting:
                if i.date == date:
                    total += 1
        else:
            for i in cls.lst_meeting:
                if i.date == Date(date):
                    total += 1
        return total

    def count(self):
        """Определяющий количество сотрудников, зарегистрированных на встречу"""
        return len(self.employees)

    def __str__(self):
        answer = ''
        for i in self.employees:
            answer = answer + '{}\n'.format(i)

        return 'Рабочая встреча {}\n{} {}\n{}'.format(self.id, self.date, self.title, answer)


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)

print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))


