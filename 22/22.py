import re


class Loader:
    """This class download info from files into class attributes: list"""
    hospital_patients: list = []
    ambulatory_patients: list = []
    nurses: list = []
    doctors: list = []

    @classmethod
    def load_hospital_patients(cls, file_name):
        """Download from 'hospital' file"""
        with open(file_name, 'r', encoding='utf-8') as file_3:
            for line in file_3:
                line = line.strip().split(';')[:-1]
                patient_1: HospitalPatient = HospitalPatient(*line)
                cls.hospital_patients.append(patient_1)

    @classmethod
    def load_ambulatory_patients(cls, file_name):
        """Download from 'ambulatory' file"""
        with open(file_name, 'r', encoding='utf-8') as file_1:
            for line in file_1:
                line = line.strip().split(';')[:-1]
                patient_2: AmbulatoryPatient = AmbulatoryPatient(*line)
                cls.ambulatory_patients.append(patient_2)

    @classmethod
    def load_nurses(cls, file_name):
        """Download from 'nurses' file"""
        with open(file_name, 'r', encoding='utf-8') as file_4:
            for line in file_4:
                line = line.strip().split(';')[:-1]
                nurse: Nurse = Nurse(*line)
                cls.nurses.append(nurse)

    @classmethod
    def load_doctors(cls, file_name):
        """Download from 'doctors' file"""
        with open(file_name, 'r', encoding='utf-8') as file_2:
            for line in file_2:
                line = line.strip().split(';')[:-1]
                doctor: Doctor = Doctor(*line)
                cls.doctors.append(doctor)


class Person:
    __global_int: int = 1

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone):

        self.__id = Person.__global_int
        Person.__global_int += 1  # Нумерация

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
        self.married = self.check_bool(married)  # Информация о том находится ли в браке человек

        if self.check_passport(passport):  # Определяем данные паспорта
            self.__passport = passport
        else:
            self.__passport = None

        self.residence_address = res  # Адрес регистрации

        if self.check_education(edu):  # Уровень обучения
            self.__level_education = edu
        else:
            self.__level_education = None

        if self.check_phone(phone):  # Проверяет верность вводимых данных о телефоне
            self.__phone_number = phone
        else:
            self.__phone_number = None

    @staticmethod
    def cut_full_name(name):
        """In case of exceeding 25 characters, subsequent characters are deleted."""
        return name[:25]

    @staticmethod
    def check_bool(item_1):
        """Checks for compliance and leads to bool"""
        if item_1 == 'False':
            item_1 = False
            return item_1
        elif item_1 == 'True':
            item_1 = True
            return item_1
        else:
            return None

    @staticmethod
    def print_yes_no(item_2):
        """Outputs 'да' or 'нет'"""
        if item_2:
            return 'да'
        else:
            return 'нет'

    @staticmethod
    def check_gender(gender):
        """String values only 'муж.' or 'жен.'"""
        if gender == 'муж.' or gender == 'жен.':
            return True
        else:
            return False

    @staticmethod
    def check_date(birth):
        """Only a string of 10 characters in the following format: 99.99.9999, where 9 is any digit."""
        if len(birth) == 10:
            if birth.find('.') != -1:
                birth = birth.split('.')
                if len(birth[0]) == 2 and birth[0].isdigit():
                    if len(birth[1]) == 2 and birth[1].isdigit():
                        if len(birth[2]) == 4 and birth[0].isdigit():
                            return True
        return False

    def check_passport(self, passport):
        """Only a string of 22 characters in the following format: 9999 999999 99.99.9999, where 9 is any digit."""
        if len(passport) == 22:
            passport = passport.split(' ')
            if len(passport[0]) == 4 and passport[0].isdigit():
                if len(passport[1]) == 6 and passport[1].isdigit():
                    if self.check_date(passport[2]):
                        return True
        return False

    @staticmethod
    def check_education(edu):
        """String values only 'высшее', 'ср.спец', 'среднее'."""
        if edu in ['высшее', 'ср.спец', 'среднее']:
            return True
        else:
            return False

    @staticmethod
    def check_phone(phone):
        """Only a string of 16 characters in the following format: +7(999)999-99-99, where 9 is any digit."""
        return bool(re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone))

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

    @property  # Свойство - phone_number
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone):
        if self.check_phone(phone):  # Проверяет верность вводимых данных о телефоне
            self.__phone_number = phone
        else:
            self.__phone_number = None

    def __str__(self):
        """str representation"""
        number = 'Номер: {}\n'.format(self.__id)
        name = 'ФИО: {}\n'.format(self.full_name)
        gender = 'Пол: {}\n'.format(self.gender) if self.gender is not None else None
        birth = 'Дата рождения: {}\n'.format(self.birthday) if self.birthday is not None else None
        place_birth = 'Место рождения: {}\n'.format(self.place_birth) if self.place_birth is not None else None
        marriage = 'В браке: {}\n'.format(self.print_yes_no(self.married)) if self.married is not None else None
        passport = 'Паспорт: {}\n'.format(self.passport) if self.passport is not None else None
        address = 'Адрес регистрации: {}\n'.format(
            self.residence_address) if self.residence_address is not None else None
        edu = 'Уровень образования: {}\n'.format(self.level_education) if self.level_education is not None else None
        phone = 'Телефон: {}\n'.format(self.phone_number) if self.phone_number is not None else None

        list_1 = [number, name, gender, birth, place_birth, marriage, passport, address, edu, phone]
        answer = ''
        for i in list_1:
            if i is not None:
                answer = answer + i

        return answer

    def __repr__(self):
        """repr representation"""
        return '{}. {}'.format(self.__id, self.full_name)


class Employee(Person):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, lang, document, year,
                 qualification, speciality, profession, exp):
        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone)

        self.know_foreign_language = self.check_bool(lang)  # Знание иностранных языков
        self.education_document = document  # Документ об образовании

        if self.check_year(year):  # Дата выпуска из высшего учебного заведения. От 1950 до 2030.
            self.__year_graduation = int(year)
        else:
            self.__year_graduation = None

        self.qualification = qualification  # Квалификация
        self.speciality = speciality  # Специализация

        if self.check_profession(profession):  # Только строковые значения 'врач', 'медицинская сестра'
            self.__profession = profession
        else:
            self.__profession = None

        if self.check_exp(exp):  # Опыт работы
            self.__work_experience = int(exp)
        else:
            self.__work_experience = None

    @staticmethod
    def check_year(year):
        """Only an integer from 1950 to 2030."""
        if year.isdigit():
            year = int(year)
            if 1950 <= year <= 2030:
                return True
        return False

    @staticmethod
    def check_profession(profession):
        """String values only 'врач', 'медицинская сестра'."""
        return profession in ['врач', 'медицинская сестра']

    @staticmethod
    def check_exp(exp):
        """An integer from 0 to 60."""
        if exp.isdigit():
            exp = int(exp)
            if 0 <= exp <= 60:
                return True
        return False

    @property  # Свойство - year_graduation
    def year_graduation(self):
        return self.__year_graduation

    @year_graduation.setter
    def year_graduation(self, year):
        if self.check_year(year):  # Дата выпуска из высшего учебного заведения. От 1950 до 2030.
            self.__year_graduation = int(year)
        else:
            self.__year_graduation = None

    @property  # Свойство - profession
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        if self.check_profession(profession):  # Только строковые значения 'врач', 'медицинская сестра'
            self.__profession = profession
        else:
            self.__profession = None

    @property  # Свойство - work_experience
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, exp):
        if self.check_exp(exp):  # Опыт работы
            self.__work_experience = int(exp)
        else:
            self.__work_experience = None

    def __str__(self):
        """str representation"""
        answer = super().__str__()
        lang = 'Знание иностранного языка: {}\n'.format(self.print_yes_no(self.know_foreign_language)) if \
            self.know_foreign_language is not None else None
        doc = 'Документ об образовании: {}\n'.format(self.education_document) if self.education_document is not None \
            else None
        year = 'Год окончания: {}\n'.format(self.year_graduation) if self.year_graduation is not None else None
        qualification = 'Квалификация: {}\n'.format(self.qualification) if self.qualification is not None else None
        spec = 'Специализация: {}\n'.format(self.speciality) if self.speciality is not None else None
        profession = 'Профессия: {}\n'.format(self.profession) if self.profession is not None else None
        exp = 'Стаж: {}\n'.format(self.work_experience) if self.work_experience is not None else None

        list_2 = [lang, doc, year, qualification, spec, profession, exp]
        for j in list_2:
            if j is not None:
                answer = answer + j

        return answer

    def __repr__(self):
        return super().__repr__()


class Nurse(Employee):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, lang, document, year,
                 qualification, speciality, profession, exp, service, care, procedures):

        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone, lang, document, year,
                         qualification, speciality, profession, exp)

        self.sanitary_service = self.check_bool(service)  # Санитарная обработка помещений
        self.patient_care = self.check_bool(care)  # Уход за больными
        self.medical_procedures = self.check_bool(procedures)  # Выполнение медицинских процедур

    def __str__(self):
        """str representation"""
        answer = super().__str__()
        service = 'Санитарная обработка помещений: {}\n'.format(self.print_yes_no(self.sanitary_service)) if \
            self.sanitary_service is not None else None
        care = 'Уход за больными: {}\n'.format(self.print_yes_no(self.patient_care)) if self.patient_care is not None \
            else None
        procedures = 'Выполнение медицинских процедур: {}\n'.format(self.print_yes_no(self.medical_procedures)) if \
            self.medical_procedures is not None else None

        list_3 = [service, care, procedures]
        for k in list_3:
            if k is not None:
                answer = answer + k

        return answer

    def __repr__(self):
        return super().__repr__()


class Doctor(Employee):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, lang, document, year,
                 qualification, speciality, profession, exp, degree, rank, category, trainings, errors, diagnosis,
                 treatment, rehab):

        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone, lang, document, year,
                         qualification, speciality, profession, exp)

        self.academic_degree = self.check_bool(degree)  # Академическая степень
        self.academic_rank = self.check_bool(rank)  # Академический ранг

        if self.check_category(category):  # Только строковые значения 'высшая', 'первая', 'вторая'.
            self.__category = category
        else:
            self.__category = None

        self.trainings = self.check_bool(trainings)  # Повышение квалификации
        self.medical_errors = errors  # Врачебные ошибки
        self.diagnosis_patients = self.check_bool(diagnosis)  # Выполнение диагностики заболеваний
        self.treatment_patients = self.check_bool(treatment)  # Лечебная практика:
        self.rehabilitation_patients = self.check_bool(rehab)  # Реабилитация больных

    @staticmethod
    def check_category(item_3):
        """String values only 'высшая', 'первая', 'вторая'."""
        if item_3 in ['высшая', 'первая', 'вторая']:
            return True
        else:
            return False

    @property  # Свойство - category
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if self.check_category(category):  # Только строковые значения 'высшая', 'первая', 'вторая'.
            self.__category = category
        else:
            self.__category = None

    def __str__(self):
        """str representation"""
        answer = super().__str__()

        degree = 'Ученая степень: {}\n'.format(self.print_yes_no(self.academic_degree)) if self.academic_degree is not \
            None else None
        rank = 'Ученое звание: {}\n'.format(self.print_yes_no(self.academic_rank)) if self.academic_rank is not None \
            else None
        category = 'Категория: {}\n'.format(self.category) if self.category is not None else None
        trainings = 'Повышение квалификации: {}\n'.format(self.print_yes_no(self.trainings)) if self.trainings is not \
                    None else None
        errors = 'Врачебные ошибки: {}\n'.format(self.medical_errors) if self.medical_errors is not None else None
        diagnosis = 'Выполнение диагностики заболеваний: {}\n'.format(self.print_yes_no(self.diagnosis_patients)) if \
            self.diagnosis_patients is not None else None
        treatment = 'Лечебная практика: {}\n'.format(self.print_yes_no(self.treatment_patients)) if \
            self.treatment_patients is not None else None
        rehab = 'Реабилитация больных: {}\n'.format(self.print_yes_no(self.rehabilitation_patients)) if \
            self.rehabilitation_patients is not None else None

        list_4 = [degree, rank, category, trainings, errors, diagnosis, treatment, rehab]
        for t in list_4:
            if t is not None:
                answer = answer + t
        return answer

    def __repr__(self):
        return super().__repr__()


class Patient(Person):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, policy, status, place,
                 blood, rhesus, allergy):
        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone)

        self.medical_policy = policy  # Медицинский полис

        if self.check_status(status):  # Статус(вид занятости)
            self.__status = status
        else:
            self.__status = None

        self.place_work_study = place  # Место работы, учёбы

        if self.check_blood(blood):
            self.__blood_type = int(blood)
        else:
            self.__blood_type = None

        if self.check_rhesus(rhesus):  # Резус-фактор
            self.__rhesus_affiliation = rhesus
        else:
            self.__rhesus_affiliation = None

        self.allergic_reactions = allergy  # Аллергия

    @staticmethod
    def check_status(status):
        """String values only 'рабочий', 'служащий', 'обучающийся'"""
        if status in ['рабочий', 'служащий', 'обучающийся']:
            return True
        else:
            return False

    @staticmethod
    def check_blood(blood):
        """An integer from 1 to 4."""
        if blood.isdigit():
            blood = int(blood)
            if 1 <= blood <= 4:
                return True
        return False

    @staticmethod
    def check_rhesus(rhesus):
        """String values only '+', '-'."""
        if rhesus in ['+', '-']:
            return True
        else:
            return False

    @property  # Свойство - status
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if self.check_status(status):  # Статус(вид занятости)
            self.__status = status
        else:
            self.__status = None

    @property  # Свойство - blood_type
    def blood_type(self):
        return self.__blood_type

    @blood_type.setter
    def blood_type(self, blood):
        if self.check_blood(blood):
            self.__blood_type = int(blood)
        else:
            self.__blood_type = None

    @property  # Свойство - rhesus_affiliation
    def rhesus_affiliation(self):
        return self.__rhesus_affiliation

    @rhesus_affiliation.setter
    def rhesus_affiliation(self, rhesus):
        if self.check_rhesus(rhesus):  # Резус-фактор
            self.__rhesus_affiliation = rhesus
        else:
            self.__rhesus_affiliation = None

    def __str__(self):
        """str representation"""
        answer = super().__str__()

        policy = 'Медицинский полис: {}\n'.format(self.medical_policy) if self.medical_policy is not None else None
        status = 'Статус: {}\n'.format(self.status) if self.status is not None else None
        place = 'Место работы (учебы): {}\n'.format(
            self.place_work_study) if self.place_work_study is not None else None
        blood = 'Группа крови: {}({})\n'.format(self.blood_type, self.rhesus_affiliation) if (
                self.blood_type is not None
                and self.rhesus_affiliation
                is not None) else None
        allergy = 'Аллергические реакции: {}\n'.format(self.allergic_reactions) if self.allergic_reactions is not None \
            else None

        list_5 = [policy, status, place, blood, allergy]
        for i in list_5:
            if i is not None:
                answer = answer + i
        return answer

    def __repr__(self):
        return super().__repr__()


class HospitalPatient(Patient):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, policy, status, place,
                 blood, rhesus, allergy, department, room, clinic):
        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone, policy, status, place,
                         blood, rhesus, allergy)

        self.medical_department = department  # Отделение
        self.room_number = self.turn_room(room)  # Номер палаты
        self.clinical_diagnosis = clinic  # Диагноз

    @staticmethod
    def turn_room(room):
        if room.isdigit():
            return int(room)
        return None

    def __str__(self):
        """str representation"""
        answer = super().__str__()
        department = 'Отделение: {}\n'.format(self.medical_department) if self.medical_department is not None else None
        room = 'Палата: {}\n'.format(self.room_number) if self.room_number is not None else None
        clinic = 'Клинический диагноз: {}\n'.format(self.clinical_diagnosis) if self.clinical_diagnosis != \
            'Не выявлено' else None

        list_6 = [department, room, clinic]
        for j in list_6:
            if j is not None:
                answer = answer + j
        return answer

    def __repr__(self):
        return super().__repr__()


class AmbulatoryPatient(Patient):

    def __init__(self, name, gender, birth, place_birth, married, passport, res, edu, phone, policy, status, place,
                 blood, rhesus, allergy, number, disability, group, chronic):
        super().__init__(name, gender, birth, place_birth, married, passport, res, edu, phone, policy, status, place,
                         blood, rhesus, allergy)

        if self.check_number(number):  # Участок
            self.__territorial_number = int(number)
        else:
            self.__territorial_number = None

        if self.check_disability(disability):  # Группа инвалидности
            self.__disability = int(disability)
        else:
            self.__disability = None

        if self.check_group(group):  # Группа здоровья
            self.__health_group = group
        else:
            self.__health_group = None

        self.chronic_diagnosis = chronic  # Хронические заболевания

    @staticmethod
    def check_number(number):
        """An integer from 1 to 20."""
        if number.isdigit():
            number = int(number)
            if 1 <= number <= 20:
                return True
        return False

    @staticmethod
    def check_disability(disability):
        """An integer from 0 to 3."""
        if disability.isdigit():
            disability = int(disability)
            if 0 <= disability <= 3:
                return True
        return False

    @staticmethod
    def check_group(group):
        """String values only 'I', 'II', 'III'."""
        if group in ['I', 'II', 'III']:
            return True
        else:
            return False

    @property  # Свойство - territorial_number
    def territorial_number(self):
        return self.__territorial_number

    @territorial_number.setter
    def territorial_number(self, number):
        if self.check_number(number):  # Участок
            self.__territorial_number = int(number)
        else:
            self.__territorial_number = None

    @property  # Свойство - disability
    def disability(self):
        return self.__disability

    @disability.setter
    def disability(self, disability):
        if self.check_disability(disability):  # Группа инвалидности
            self.__disability = int(disability)
        else:
            self.__disability = None

    @property
    def health_group(self):
        return self.__health_group

    @health_group.setter
    def health_group(self, group):
        if self.check_group(group):  # Группа здоровья
            self.__health_group = group
        else:
            self.__health_group = None

    def __str__(self):
        answer = super().__str__()
        number = 'Участок: {}\n'.format(self.territorial_number) if self.territorial_number is not None else None
        disability = 'Группа инвалидности: {}\n'.format(self.disability) if (self.disability != 0 and self.disability
                                                                             is not None) else None
        group = 'Группа здоровья: {}\n'.format(self.health_group) if self.health_group is not None else None
        chronic = 'Хронический диагноз: {}\n'.format(self.chronic_diagnosis) if self.chronic_diagnosis != \
            'Не выявлено' else None
        list_7 = [number, disability, group, chronic]
        for k in list_7:
            if k is not None:
                answer = answer + k
        return answer

    def __repr__(self):
        return super().__repr__()
