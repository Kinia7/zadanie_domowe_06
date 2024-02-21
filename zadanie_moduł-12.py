import csv
import argparse

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
        print(f'Dodano kontakt: {contact.name}')

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
        print("Wyszukiwanie kontaktów...")
        print(f"Query: {query}")
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        print(f"Liczba znalezionych kontaktów: {len(results)}")
        return results

def parse_args():
    parser = argparse.ArgumentParser(description="Zarządzaj swoją książką adresową")
    parser.add_argument('--add', nargs=4, metavar=('NAME', 'PHONE', 'EMAIL', 'FAVORITE'), help="Dodaj nowy kontakt")
    parser.add_argument('--save', metavar='FILENAME', help="Zapisz książkę adresową do pliku")
    parser.add_argument('--load', metavar='FILENAME', help="Wczytaj książkę adresową z pliku")
    parser.add_argument('--search', metavar='QUERY', help="Szukaj kontaktów zawierających QUERY")
    parser.add_argument('--list', action='store_true', help="Wyświetl zawartość książki adresowej")
    return parser.parse_args()

def main():
    args = parse_args()
    address_book = AddressBook()

    if args.add:
        name, phone, email, favorite = args.add
        favorite = True if favorite.lower() in ['true', 't', 'yes', 'y'] else False
        address_book.add_contact(Contact(name, phone, email, favorite))

    if args.save:
        address_book.save_to_disk(args.save)
        print(f"Książka adresowa została zapisana do pliku {args.save}.")

    if args.load:
        address_book.load_from_disk(args.load)
        print(f"Książka adresowa została wczytana z pliku {args.load}.")

    if args.list:
        print("Zawartość książki adresowej:")
        for contact in address_book.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Favorite: {contact.favorite}")

    if args.search:
        results = address_book.search_contacts(args.search)
        for result in results:
            print(f"Name: {result.name}, Phone: {result.phone}, Email: {result.email}, Favorite: {result.favorite}")

if __name__ == "__main__":
    main()
