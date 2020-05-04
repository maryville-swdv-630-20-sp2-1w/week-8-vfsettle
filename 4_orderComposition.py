# this composes an order summary to be sent to the fulfillment store after customer has finished checkout.

class Customer:
    def __init__(self, customerID):
        self.customerID = customerID
        self.fName = ''
        self.lName = ''
        self.address = ''

    def __str__(self):
        return  self.customerID
                
    def getCustomer(self):
        print (self.customerID)

class Store:
    def __init__(self, storeID):
        self.storeID = storeID
        self.name = ''
        self.address = ''

    def __str__(self):
        return  self.storeID
                
    def getStore(self):
        print (self.storeID)

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return  str(self.items)  
        
#order summary
class OrderSummary(Customer, Store, Cart):
    def __init__(self, customer, store, cart):
        self.customer = customer
        self.store = store
        self.cart = cart
        
    def __str__(self):
        return 'Order for Customer ID: ' + str(self.customer) + ' to Store ID: ' + str(self.store) + ' for: ' + str(self.cart)
        
def main(): # tests implementation of base clase Pizza which inherits from Customer, Store & Cart
    customer = Customer ('12345')
    store = Store ('67890')

    cart = Cart()
    cart.add("medium 2-topping pizza: $ 9.99")
    cart.add("extra-large specialty pizza: $ 15.99")
    
    summary = OrderSummary(customer, store, cart)
    print ('\n', summary, '\n', "CartID:", store, "-", customer)

main()