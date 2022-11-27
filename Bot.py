from AddressBook import *
from Levenshtein import ratio


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def corrector(handler):
        def wrapper(*args, **kwargs):
            try:
                result = handler(*args, **kwargs)
                return result
            except KeyError:
                return 'Enter user name.'
            except ValueError as e:
                return e.args[0]
            except IndexError:
                return 'Give me name and phone'
            except TypeError:
                return 'Give me name and phone'
        return wrapper

    @corrector
    def answer_exit():
        return 'Good bye!'

    @corrector
    def hello(self):
        print("Hello! How can I help you?")

    @corrector
    def add_contact(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
        else:
            record = Record(name)
            self.book.add_record(record)
        record.add_information(Phone())
        record.add_information(Email())
        record.add_information(Birthday())
        record.add_information(Address())
        
        self.book.add_record(record)
            
        print(f'Contact {name.value} is added')
        
    @corrector
    def delete_contact(self):
        name = Name()
        if name.value in self.book.data:
            self.book.data.pop(name.value)
            print(f'Contact {name.value} is deleted')
        else:
            print(f'Contact {name.value} not found')
            
    @corrector
    def add_phone(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            record.add_information(Phone())
        else:
            print(f'Contact {name.value} not found')
            
    @corrector
    def add_email(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            record.add_information(Email())
        else:
            print(f'Contact {name.value} not found')

    @corrector
    def add_birthday(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            record.add_information(Birthday())
        else:
            print(f'Contact {name.value} not found')

    @corrector
    def add_address(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            record.add_information(Address())
        else:
            print(f'Contact {name.value} not found')
            
    @corrector
    def search_contact(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            record.show_information()
        else:
            print(f'Contact {name.value} not found')
            
    @corrector
    def delete_phone(self):
        name = Name()
        if name.value in self.book.data:
            record = self.book.data[name.value]
            print(record.delete_phone(Phone()))
        else:
            print(f'Contact {name.value} not found')

    @staticmethod
    def run_command(bot_command):
        bot_command()
                
    @staticmethod
    def command_error(user_data, data, name_data = 'command'):
        similar_answer =  {ratio(user_data, key) : key for key in data}
        similar_answer = sorted(similar_answer.items(), reverse=True)
        print(f'Wrong {name_data}. May be you wont to write "{similar_answer[0][1]}", please try again.')
