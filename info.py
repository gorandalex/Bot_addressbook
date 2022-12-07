from datetime import date, datetime
from re import search, match
from abc import ABC, abstractmethod


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_information(self, info):
        info.change_information(self)

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone.value:
                self.phones.pop(record_phone)
                return f'Phone {phone.value} deleted'
        return f'Phone {phone.value} not found'

    def show_information(self):
        ...


class Field(ABC):
    def __init__(self):
        self.value = Field.show_question()

    @abstractmethod
    def change_information(self, record):
        ...

    @staticmethod
    @abstractmethod
    def show_question():
        ...


class Address(Field):
    def __init__(self):
        self.value = Address.show_question()

    def change_information(self, record):
        record.address = self

    @staticmethod
    def show_question():
        while True:
            value = input(
                "Address (format should be IIIII, м. Місто, в. Вулиця, дод.записи):")
            try:
                clean_address = (
                    value.strip()
                    .replace("(", "")
                    .replace(")", "")
                    .replace("-", "")
                    .replace(" ", "")
                    .replace(",", " ")
                )

                if value == '':
                    break
                elif not match(r"\d{5}\ \м.\w+\ \в.\w+(\d+|\D+)+", clean_address):
                    raise ValueError
            except ValueError:
                print('Incorrect address format! Please provide correct address format.')
            else:
                break
        return value


class Birthday(Field):
    def __init__(self):
        self.value = Birthday.show_question()

    def change_information(self, record):
        record.birthday = self

    @staticmethod
    def show_question():
        while True:
            value = input("Birthday: ").strip()
            try:
                for separator in (".", ",", "-", ":", "/"):
                    value, *args = value.split(separator)

                    if args:
                        break
                if value == '':
                    break
                elif not args or len(args) > 2:
                    raise ValueError("Invalide date format. Date format should be YYYY.MM.DD or DD.MM.YYYY.")
                else:
                    if int(value) > 31:
                        value = date(int(value), int(args[0]), int(args[1]))
                    else:
                        value = date(int(args[1]), int(args[0]), int(value))
                    break
            except ValueError:
                print('Invalide date format. Date format should be YYYY.MM.DD or DD.MM.YYYY.')
        return value


class Email(Field):
    def __init__(self):
        self.value = Email.show_question()

    def change_information(self, record):
        record.email = self

    @staticmethod
    def show_question():
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            value = input("Email: ")
            try:
                if match(regex, value) or value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f""""Email {value} is not valid,
            please enter correct email.
            Example of emails: my.ownsite@our-earth.org
                                ankitrai326@gmail.com""")
        return value


class Name(Field):
    def __init__(self):
        self.value = Name.show_question()

    def change_information(self, record):
        record.name = self

    @staticmethod
    def show_question():
        return input("Name: ").strip()


class Phone(Field):
    def __init__(self):
        self.value = Phone.show_question()

    def change_information(self, record):
        record.phones.append(self)

    @staticmethod
    def show_question():
        while True:
            value = input("Phone: (+38..........): ")
            try:
                if match('^\\+38\d{10}$', value) or value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print(
                    'Incorrect phone number format! Please provide correct phone number format.')
        return value


class Note:
    pass
