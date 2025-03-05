import products as pr




def main():
    products = []


    laptop = pr.Product(
        'Laptop',
        800.00,
        '15-inch display, 8GB RAM, 256GB SSD')
    laptop.display()
    print(laptop)
    # print( '__dict__', laptop.__dict__)
    # print( '__module__', laptop.__module__)
    # print( '__repr__', laptop.__repr__())
    # print( '__str__', laptop.__str__())
    
    products.append(laptop)

    smartphone = pr.Product(
        "Smartphone",
        500.0,
        "6-inch display, 128GB storage")
    smartphone.display()
    products.append(smartphone)
    print(smartphone)

    print(products)



if __name__ =='__main__':
    main()