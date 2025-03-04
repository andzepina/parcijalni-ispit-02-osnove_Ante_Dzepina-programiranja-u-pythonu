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
    for product in offer_products:
        sub_total += product['item_total']
    
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

    # Kreiraj novu podnudu
    new_offer = len(offers) + 1
    print()
    print('NOVA PONUDA')
    print()
    try:
        offer = {
            'offer_number': new_offer,
            'customer': selected_customer,
            'date': input('Unesite datum ponude (Godina-Mjesec-Dan): '),
            'items': offer_products,
            'sub_total': sub_total,
            'tax': tax,
            'total': total
        }
        offers.append(offer)
        print('Ponuda uspješno kreirana!')
        print_offer(offer)
    except Exception as ex:
        print(f'Dogodila se pogreška {ex}')
    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    print()
    print('UPRAVLJANJE PROIZVODIMA')
    print()
    print('1. Dodaj novi proizvod')
    print('2. Izmijeni postojeći proizvod')

    change_add_product = int(input('Odaberi broj opcije: '))

    match change_add_product:
        case 1:
            try:
                id = len(products) + 1
                name = input('Unesite naziv proizvoda: ')
                description = input('Upisite opis proizvoda: ')
                price = float(input('Unesite cijenu proizvoda: '))

                new_product ={
                    'id': id,
                    'name': name,
                    'description': description,
                    'price': price
                }
                products.append(new_product)

                save_data(PRODUCTS_FILE, products)
            except Exception as ex:
                print(f'Dogodila se pogreška: {ex}')
        case 2:
            print()
            for i, product in enumerate(products):
                print(f'{i + 1}. {product['name']}')
            print()

            try:
                product_choice = int(input('Odaberite proizvod za izmjenu: '))
                selected_product = products[product_choice - 1]
                selected_product['name'] = input(f"Unesite novi naziv (trenutno: {selected_product['name']}): ")
                selected_product['description'] = input(f"Unesite novi opis (trenutno: {selected_product['description']}): ")
                selected_product['price'] = float(input(f"Unesite novu cijenu (trenutno: {selected_product['price']}): "))

                save_data(PRODUCTS_FILE, products)
            
            except Exception as ex:
                print(f'Dogodila se pogreška {ex}')
        
        case _:
            print('Krivo ste odabrali opciju Upravljanja proizvodom')

    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    #pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    print()
    print('UPRAVLJANJE KUPCIMA')
    print()
    print('1. Unesite podatke o novom kupcu')
    print('2. Prikaz svih kupaca')
    print()

    choice = int(input('Odaberi opciju Upravljanja kupcima: '))

    match choice:
        case 1:
            try:
                name = input('Unesite naziv kupca: ')
                email = input('Unesite email adresu kupca: ')
                vat_id = input('Unesite OIB kupca: ')
                new_customer = {
                    'name': name,
                    'email': email,
                    'vat_id': vat_id
                }
                customers.append(new_customer)
                save_data(CUSTOMERS_FILE, customers)
            except Exception as ex:
                print(f'Dogodila se greška {ex}.')
            
        case 2:
            try:
                print('Popis svih kupaca:')
                print()
                for i, customer in enumerate(customers):
                    print(f'{i + 1} {customer['name']} {customer['email']} vat_id: {customer['vat_id']}')

            except Exception as ex:
                print(f'Dogodila se pogreška {ex}')
        case _:
            print('Krivo ste odabrali opciju Upravljanje kupcima')


    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    #pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    print()
    print('PREGLED PONUDA')
    print()
    print('1. Prikaz svih ponuda')
    print('2. Prikaz ponuda za odabrani mjesec')
    print('3. Prikaz ponuda prema željenom ID-u')
    print()

    offers_choice = int(input('Selektirajte redni broj gore prikaznih opcija: '))

    match offers_choice:
        case 1:
            print(offers)
        case 2:
            month = input('Upisite mjesec za koji želite pretražiti pounde, zapis (Godina-Mjesec): ')
            selected_month = []
            for offer in offers:
                if offer['date'].startswith(month):
                    selected_month.append(offer)
                    print(selected_month)
    
        case 3:
            offer_id = int(input('Unesite ID ponude koju želite pregledati: '))
            selected_id_offer = None

            for offer in offers:
                if offer['offer_number'] == offer_id:
                    selected_id_offer = offer
                    break
            try:
                print('-'*40)
                print(selected_id_offer)
                print('-'*40)

            except Exception as ex:
                print(f'Dogodila se greška{ex} Ponuda pod tim ID-om nije pronađena')
        
        case _:
            print('Krivo odabrana opcija pregleda PONUDA')


    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    
    
    
    #pass


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
