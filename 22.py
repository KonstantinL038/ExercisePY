class Loader:
    hospital_patients = []
    ambulatory_patients = []
    nurses = []
    doctors = []

    @classmethod
    def load_hospital_patients(cls, file_name):
        pass

    @classmethod
    def load_ambulatory_patients(cls, file_name):
        pass

    @classmethod
    def load_nurses(cls, file_name):
        pass

    @classmethod
    def load_doctors(cls, file_name):
        pass


class Person:
    __id = 0

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu):
        self.__id += 1  # Номер экземпляра
        self.__full_name = self.cut_full_name(name)  # Имя обрезанное до 25 символов

        if self.check_gender(gender):  # Определяем гендер - допустимое только "муж." и "жен."
            self.__gender = gender
        else:
            self.__gender = None

        if self.check_date(birth):  # Определяем день рождения
            self.__birthday = birth
        else:
            self.__birthday = None

        self.place_birth = place_birth  # Место рождения
        self.married = married  # Информация о том находится ли в браке человек

        if self.check_passport(passport):  # Определяем данные паспорта
            self.__passport = passport
        else:
            self.__passport = None

        self.residence_address = res  # Адрес регистрации

        if self.check_education(edu):  # Уровень обучения
            self.__level_education = edu
        else:
            self.__level_education = None

    @staticmethod
    def cut_full_name(name):
        """В случае превышения 25 символов, последующие символы удаляются."""
        return name[:26]

    @staticmethod
    def check_gender(gender):
        """Только строковые значения 'муж.' или 'жен.'"""
        if gender == 'муж.' or gender == 'жен.':
            return True
        else:
            return False

    @staticmethod
    def check_date(birth):
        """Только строка из 10 символов следующего формата: 99.99.9999, где 9 - любая цифра."""
        if len(birth) == 10:
            if birth.find('.') != -1:
                birth = birth.split('.')
                if len(birth[0]) == 2 and birth[0].isdigit():
                    if len(birth[1]) == 2 and birth[1].isdigit():
                        if len(birth[2]) == 4 and birth[0].isdigit():
                            return True
        return False

    def check_passport(self, passport):
        """Только строка из 22 символов следующего формата: 9999 999999 99.99.9999, где 9 - любая цифра."""
        if len(passport) == 22:
            passport = passport.split(' ')
            if len(passport[0]) == 4 and passport[0].isdigit():
                if len(passport[1]) == 6 and passport[1].isdigit():
                    if self.check_date(passport[2]):
                        return True
        return False

    @staticmethod
    def check_education(edu):
        """Только строковые значения 'высшее', 'ср.спец', 'среднее'."""
        if edu in ['высшее', 'ср.спец', 'среднее']:
            return True
        else:
            return False

    @property  # Свойство - full_name
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, name):
        self.__full_name = self.cut_full_name(name)

    @property  # Свойство - gender
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if self.check_gender(gender):
            self.__gender = gender
        else:
            self.__gender = None

    @property  # Свойство - birthday
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birth):
        if self.check_date(birth):  # Определяем допустимый день рождения
            self.__birthday = birth
        else:
            self.__birthday = None

    @property  # Свойство - passport
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if self.check_passport(passport):  # Определяем данные паспорта
            self.__passport = passport
        else:
            self.__passport = None

    @property  # Cвойство - level_education
    def level_education(self):
        return self.__level_education

    @level_education.setter
    def level_education(self, edu):
        if self.check_education(edu):  # Уровень обучения
            self.__level_education = edu
        else:
            self.__level_education = None
