

class Customers:
    def __init__(self, name, email, vat_id):
        self.name = name
        self.email = email
        self.vat_id = vat_id

    
    def __repr__(self) -> str:

        return f'{self.name}'