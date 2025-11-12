from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10: # перевірка коректності номера телефону
            super().__init__(value)
        else:
            raise ValueError("Номер має містити 10 цифр")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone)) # додає новий номер телефону
        except Exception:
            pass

    def remove_phone(self, phone):
        
        self.phones = [p for p in self.phones if p.value != phone] #видаляє телефон за значенням

    def edit_phone(self, old_phone, new_phone):
        try:
            for phone in self.phones: # редагує існуючий телефон
                if phone.value == old_phone:
                    phone.value = new_phone
        except Exception:
            pass

    def find_phone(self, phone_number):
        try:
            for phone in self.phones: # пошук об’єкта Phone за значенням
                if phone.value == phone_number:
                    return phone
            return None
        except Exception:
            pass


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        try:
            self.data[record.name.value] = record
        except Exception:
            pass

    def find(self, name):
        try:
            return self.data[name]
        except Exception:
            pass
        
    def delete(self, name):
        try:
            del self.data[name]
        except Exception:
            pass


# Створення нової адресної книги

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")
