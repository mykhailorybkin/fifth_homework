from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
	def __init__(self, number):
            pattern = r"^\d{10}$"
            if re.fullmatch(pattern, number):
                self.value = number
            else:
                return ValueError
            
               

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones =[]

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    def remove_phone(self, phone):
        try:
            for p in self.phones:
                if p.value == phone:
                    self.phones.remove(p)
                    return "Phone deleted"
                else:
                    return "Phone not found"
        except:
            return "Exception occured"
    def edit_phone(self, old_phone, new_phone):
        try:
              for p in self.phones:
                   if p.value == old_phone:
                        self.phones.remove(p)
                        self.add_phone(new_phone)
                        return "Phone changed"
                   else:
                        return "Phone not found"
        except ValueError as v:
             return v
    def find_phone(self, phone_number):
        try:
              for p in self.phones:
                   if p.value == phone_number:
                        return p
                   else:
                        return None
        except Exception as e:
             return e
            
        

class AddressBook(UserDict):

    # реалізація класу
    def add_record(self, record : Record):
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
             del self.data[name]
             return f"Record {name} has been deleted"
        else:
             return f"Record {name} has not been found"
    def __str__(self):
         return '\n'.join(str(record) for record in self.data.values())
        
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
print(book)


#decorators
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "I don't have such name in my dictionary."
        except Exception as ex:
            return f"Unexpected error{ex}"
        

    return inner


#general methods
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    return contacts
    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
