import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    
    customer_insert = load_data(CUSTOMERS_FILE)

    print()
    print('Odaberi redni broj dolje navedenih kupaca: ')
    print()
    for i, customer in enumerate(customer_insert):
        print(f'{i +1}. {customer['name']} ')

    
    try:
        customer_choice = int(input('Odaberi redni broj kupca: '))
        selected_customer = customers[customer_choice - 1]
        print(f'Odabrali ste kupca: {selected_customer['name']} ({selected_customer['email']}) {selected_customer['vat_id']}')

    except Exception as ex:
        print(f'Greška {ex} Odabrali ste nepostojeći redni broj kupca.')



    print()
    print('Odaberite proizvod koji želite u ponudi')
    print()
    
    offer_products = []
    while True:
        for i, product in enumerate(products):
            print(f'{i + 1}. {product['name']} podjednačna cijena {product['price']} EUR')
        try:
            product_choice = int(input('Odaberite redni broj proizvoda 0 je izlazak: '))
            if product_choice == 0:
                break
            selected_product = products[product_choice - 1]
            quantity = int(input(f'Unesite količinu za proizvod {selected_product['name']}: '))
            product_total = selected_product['price'] * quantity
            offer_products.append({
                    "product_id": selected_product['id'],
                    "product_name": selected_product['name'],
                    "description": selected_product['description'],
                    "price": selected_product['price'],
                    "quantity": quantity,
                    "item_total": product_total
                })
        except Exception as ex:
                print('Dogodila se greška, Ponovno odaberite proizvod.')

    # Izračunaj ukupno
     
    sub_total = 0
    for item in offer_products:
        sub_total += product_total['item_total']
    
    print(f'Subtotal: {sub_total} EUR')
    tax = sub_total * 0.25
    print(f'tax: {tax}')
    
    total = sub_total + tax
    print(f'total: {total} EUR')

    # Omogućite unos kupca
    # Print liste kupaca -> kupac upise broj ispred a vi onda pokupite podatke
    # while petlja 
    # Izračunajte sub_total, tax i total
    # Možda dodati novu funkciju koa ručuna total, tax i
    # total = calculate_total()
    # Dodajte novu ponudu u listu offers
    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """

    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")
    return products


if __name__ == "__main__":
    main()
