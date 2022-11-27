from datetime import date, datetime
from collections import UserDict
from re import search, match
from info import *
import pickle
import os


class AddressBook(UserDict):

    def __init__(self, data = None):
        super().__init__(data)
        self.notes = []

    def add_record(self, record):
        self.data[record.name.value] = record

    def load(self, filename):
        if os.path.exists(os.path.join(os.path.dirname('.'), 'AddressBook.dat')):    
            info_file = os.startfile(filename + '.dat')
            if info_file.st_size == 0:
                self.log('Adressbook has been created!')
            else:
                with open(filename + '.dat', 'rb') as file:
                    self = file.load(file)
                self.log("Addressbook has been loaded!")
        return self

    def log(self, action):
        current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
        message = f'[{current_time}] {action}'
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')

    def save(self, filename):
        with open(filename + '.bin', "wb") as file:
            pickle.dump(self, file)
