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
                return None
            
               

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
        required_phone = self.find_phone(phone)
        if required_phone in self.phones:
            self.phones.remove(required_phone)
        else:
            return None
        
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.add_phone(new_phone)
            else:
                return None
        
    def find_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                return p
            else:
                continue
        return self.phones
        
            
        

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
john_record.remove_phone("5555555555")
print(book)



