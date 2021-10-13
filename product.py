
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def items_to_buy(self):
        name = []
        price = []
        category = []
        interrogative = input ('Would you like to add something to your cart? 1 for yes and 2 for no')
        while interrogative != ('2'):
            new_item = input ('Type the name of the item you would like to add to your cart: ')
            name.append (new_item)
            new_price = input ('Type the price of the item you are adding to your cart: ') 
            price.append(new_price)
            new_category = input ('Type the category of the item you added to your cart: ')
            category.append(new_category)
            interrogative = input ('Would you like to add anything else to your cart? 1 for yes and 2 for no ')
        
