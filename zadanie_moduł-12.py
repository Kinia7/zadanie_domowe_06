import csv

class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_disk(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Favorite'])
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email, contact.favorite])

    def load_from_disk(self, filename):
        self.contacts = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                name, phone, email, favorite = row
                favorite = True if favorite.lower() == 'true' else False
                self.contacts.append(Contact(name, phone, email, favorite))

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

# Przykład użycia:
address_book = AddressBook()

address_book.add_contact(Contact("John Doe", "123456789", "john@example.com"))
address_book.add_contact(Contact("Jane Smith", "987654321", "jane@example.com", favorite=True))

address_book.save_to_disk("address_book.csv")

address_book.load_from_disk("address_book.csv")

query = "Jane"
results = address_book.search_contacts(query)
for result in results:
    print(f"Name: {result.name}, Phone: {result.phone}, Email: {result.email}, Favorite: {result.favorite}")
