import products as pr
import customers as cr




def main():
    products = []


    laptop = pr.Product(
        'Laptop',
        800.00,
        '15-inch display, 8GB RAM, 256GB SSD')
    #laptop.display()
    # print( '__dict__', laptop.__dict__)
    # print( '__module__', laptop.__module__)
    # print( '__repr__', laptop.__repr__())
    # print( '__str__', laptop.__str__())
    
    products.append(laptop)
    print(laptop)

    smartphone = pr.Product(
        "Smartphone",
        500.0,
        "6-inch display, 128GB storage")
    #smartphone.display()
    products.append(smartphone)
    print(smartphone)

    print(products)


    customers = []


    tech_solution = cr.Customers('Tech Solution',
                                 'info@techsolutions.com',
                                 '12345678901' )


    customers.append(tech_solution)

    print(tech_solution)

    print(customers)

if __name__ =='__main__':
    main()