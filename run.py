import json
from typing import List, Union


class Buch:
    def __init__(self, titel: str, autor: str, genre: str, preis: float):
        """Initialisiert ein Buch mit Titel, Autor, Genre und Preis.

        Args:
            titel (str): Der Titel des Buches.
            autor (str): Der Autor des Buches.
            genre (str): Das Genre des Buches.
            preis (float): Der Preis des Buches.
        """
        self.titel = titel
        self.autor = autor
        self.genre = genre
        self.preis = preis
        
class Bookstore:
    def __init__(self):
        """Initialisiert den Buchladen mit leeren Buch- und Kundenlisten."""
        self.books: List[Buch] = []
        self.customers: List[Kunde] = []

    def add_book(self, book: 'Buch'):
        """Fügt dem Buchladen ein Buch hinzu.

        Args:
            book (Buch): Das Buch, das hinzugefügt werden soll.
        """
        self.books.append(book)

    def list_books_in_store(self):
        """Listet alle Bücher im Buchladen auf oder zeigt eine Nachricht an, wenn keine Bücher verfügbar sind."""
        if not self.books:
            print("Der Buchladen hat derzeit keine Bücher.")
        else:
            print("Bücher im Buchladen:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. '{book.titel}' von {book.autor} - Genre: {book.genre} - {book.preis} Euro")

class Person:
    def __init__(self, name: str):
        """Initialisiert eine Person mit ihrem Namen.

        Args:
            name (str): Der Name der Person.
        """
        self.name = name
    
    def introduce(self):
        """Stellt die Person vor."""
        print(f"Hallo, mein Name ist {self.name}")

class Kunde(Person):
    def __init__(self, name: str, email: str):
        """Initialisiert einen Kunden mit seinem Namen, seiner E-Mail-Adresse und leeren Sammlungs- und Wunschlisten.

        Args:
            name (str): Der Name des Kunden.
            email (str): Die E-Mail-Adresse des Kunden.
        """
        super().__init__(name)
        self.email = email
        self.collection: List[Buch] = []
        self.wishlist: List[Union[Buch, str]] = []

    def purchase(self, book: 'Buch', bookstore: 'Bookstore'):
        """Kauft ein Buch und fügt es zur Sammlung des Kunden hinzu.

        Args:
            book (Buch): Das zu kaufende Buch.
            bookstore (Bookstore): Der Buchladen, in dem das Buch gekauft wird.
        """
        self.collection.append(book)
        print(f"{self.name}, Sie haben '{book.titel}' von {book.autor} gekauft.")
        self.list_customer_books()

    def list_customer_books(self):
        """Listet die Bücher in der Sammlung des Kunden auf oder zeigt eine Nachricht an, wenn die Sammlung leer ist."""
        num_books = len(self.collection)
        if num_books > 0:
            print(f"Sie haben {num_books} Buch/Bücher in Ihrer Sammlung:")
            for book in self.collection:
                print(f"'{book.titel}' von {book.autor} - Genre: {book.genre}")
        else:
            print("Ihre Sammlung ist noch leer.")

    def list_wishlist(self):
        """Listet die Elemente in der Wunschliste des Kunden auf oder zeigt eine Nachricht an, wenn die Wunschliste leer ist."""
        if not self.wishlist:
            print("Ihre Wunschliste ist leer.")
        else:
            print("Ihre Wunschliste:")
            for i, item in enumerate(self.wishlist, 1):
                if isinstance(item, Buch):
                    print(f"{i}. '{item.titel}' von {item.autor} - Genre: {item.genre}")
                else:
                    print(f"{i}. '{item}' (Suchbegriff)")

    def add_to_wishlist(self, book_or_keyword: Union[Buch, str]):
        """Fügt ein Buch oder einen Suchbegriff zur Wunschliste des Kunden hinzu.

        Args:
            book_or_keyword (Union[Buch, str]): Das Buch oder der Suchbegriff, der zur Wunschliste hinzugefügt werden soll.
        """
        if isinstance(book_or_keyword, Buch):
            self.wishlist.append(book_or_keyword)
            print(f"'{book_or_keyword.titel}' wurde zur Wunschliste hinzugefügt.")
        else:
            self.wishlist.append(book_or_keyword)
            print(f"'{book_or_keyword}' (Suchbegriff) wurde zur Wunschliste hinzugefügt.")

    def buy_from_wishlist(self, bookstore: 'Bookstore'):
        """Kauft Bücher oder führt eine Suche basierend auf der Wunschliste des Kunden durch.

        Args:
            bookstore (Bookstore): Der Buchladen, in dem die Bücher gekauft werden sollen oder in dem die Suche durchgeführt wird.
        """
        self.list_wishlist()

        if not self.wishlist:
            print("Ihre Wunschliste ist leer.")
            return

        choice = input("Geben Sie die Nummer des Buches oder Suchbegriffs ein, den Sie kaufen möchten, oder '0' zum Zurückkehren: ")
        if choice == '0':
            return

        try:
            choice = int(choice)
            if choice > 0 and choice <= len(self.wishlist):
                selected_item = self.wishlist[choice - 1]
                if isinstance(selected_item, Buch):
                    self.purchase(selected_item, bookstore)
                else:
                    keyword = selected_item
                    self.search_books(bookstore, keyword)
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            valid_selection = False
            for i, item in enumerate(self.wishlist, 1):
                if isinstance(item, Buch):
                    if choice.lower() == item.titel.lower():
                        self.purchase(item, bookstore)
                        valid_selection = True
                        break
                else:
                    if choice.lower() == item.lower():
                        keyword = item
                        self.search_books(bookstore, keyword)
                        valid_selection = True
                        break

            if not valid_selection:
                print("Ungültige Auswahl.")

    def purchase_books(self, bookstore: 'Bookstore', purchase_titles: List[str]):
        """Kauft Bücher basierend auf einer Liste von Buchtiteln.

        Args:
            bookstore (Bookstore): Der Buchladen, in dem die Bücher gekauft werden sollen.
            purchase_titles (List[str]): Die Liste der Buchtitel, die gekauft werden sollen.
        """
        for title in purchase_titles:
            for book in bookstore.books:
                if title.lower() == book.titel.lower():
                    self.purchase(book, bookstore)
                    break

    def search_books(self, bookstore: 'Bookstore', keyword: str):
        """Sucht nach Büchern im Buchladen basierend auf einem Suchbegriff.

        Args:
            bookstore (Bookstore): Der Buchladen, in dem die Suche durchgeführt wird.
            keyword (str): Der Suchbegriff.
        """
        results = [book for book in bookstore.books if keyword.lower() in book.titel.lower() or keyword.lower() in book.autor.lower()]
        if results:
            print("Gefundene Bücher:")
            for i, book in enumerate(results, 1):
                print(f"{i}. '{book.titel}' von {book.autor} - Genre: {book.genre} - {book.preis} Euro")

            choice = input("Geben Sie die Nummer des Buches ein, das Sie kaufen möchten, '0' zum Zurückkehren oder 'w' zum Zur Wunschliste hinzufügen: ")
            if choice == '0':
                return

            try:
                choice = int(choice)
                if choice > 0 and choice <= len(results):
                    selected_book = results[choice - 1]
                    self.purchase(selected_book, bookstore)
                else:
                    print("Ungültige Auswahl.")
            except ValueError:
                if choice.lower() == 'w':
                    self.add_to_wishlist(keyword)
                    print(f"'{keyword}' wurde zur Wunschliste hinzugefügt.")
                else:
                    print("Ungültige Auswahl.")
        else:
            print("Das gesuchte Buch ist nicht verfügbar.")
            notify = input("Möchten Sie benachrichtigt werden, wenn es verfügbar ist? (ja/nein): ")
            if notify.lower() == 'ja':
                self.add_to_wishlist(keyword)
                print(f"'{keyword}' wurde zur Merkliste hinzugefügt. Sie erhalten eine Benachrichtigung, wenn es verfügbar ist.")



def main():
    bookstore = Bookstore()
    
    with open('books.json', 'r') as file:
            book_data = json.load(file)
            for book_info in book_data:
                book = Buch(book_info['titel'], book_info['autor'], book_info['genre'], book_info['preis'])
                bookstore.add_book(book)

    email = input("Geben Sie Ihre E-Mail-Adresse ein: ")
    customer = None

    for existing_customer in bookstore.customers:
        if existing_customer.email == email:
            customer = existing_customer
            print(f"Hallo {customer.name}, Willkommen in Liams Buchhaus!")
            break

    if not customer:
        print("Es scheint, als wären Sie heute zum ersten Mal hier!")
        name = input("Verraten Sie uns doch Ihren Namen: ")
        customer = Kunde(name, email)
        print(f"Hallo {customer.name}, Willkommen in Liams Buchhaus!")
        bookstore.customers.append(customer)

    while True:
        print("\nHauptmenü:")
        print("1. Buch suchen")
        print("2. Buch kaufen")
        print("3. Sammlung ansehen")
        print("4. Wunschliste ansehen")
        print("5. Bücher auf Wunschliste kaufen")
        print("6. Beenden")

        choice = input("Bitte wählen Sie eine Option (1/2/3/4/5/6): ")

        if choice == '1':
            keyword = input("Geben Sie ein Suchwort ein: ")
            customer.search_books(bookstore, keyword)
        elif choice == '2':
            bookstore.list_books_in_store()
            purchase_titles = input("Geben Sie die Titel der Bücher ein, die Sie kaufen möchten (kommagetrennt): ")
            purchase_titles = [title.strip() for title in purchase_titles.split(',')]
            customer.purchase_books(bookstore, purchase_titles)
        elif choice == '3':
            customer.list_customer_books()
        elif choice == '4':
            customer.list_wishlist()
        elif choice == '5':
            customer.buy_from_wishlist(bookstore)
        elif choice == '6':
            print("Vielen Dank für Ihren Besuch, wir wünschen Ihnen einen schönen Tag!")
            break
        else:
            print("Ungültige Option. Bitte wählen Sie eine der verfügbaren Optionen (1/2/3/4/5/6/7).")

if __name__ == "__main__":
    main()
