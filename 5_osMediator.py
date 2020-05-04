#this module implements the fillStore order status notification updates to the order system.auu
import abc

class Status(metaclass=abc.ABCMeta):
    def __init__(self, med, status):
        self.mediator = med
        self.status = status

    @abc.abstractmethod
    def send(self, msg):
        pass

    @abc.abstractmethod
    def receive(self, msg):
        pass


class StatusMediatorImpl:
    def __init__(self):
        self.employee = []

    def add_cartID(self, cartID):
        self.employee.append(cartID)

    def send_message(self, msg, cartID):
        for u in self.employee:
            if u != cartID:
                u.receive(msg)


class StatusImpl(Status):
    def send(self, msg):
        print(self.status + ": Sent Status: " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.status + ": System Status: " + msg + "\n")


if __name__ == '__main__':
    mediator = StatusMediatorImpl()
    fillStore = StatusImpl(mediator, "StoreID: 54321")
    mediator.add_cartID(fillStore)
    orderSystem = StatusImpl(mediator, "CartID: 98765")
    mediator.add_cartID(orderSystem)
    fillStore.send("Order Received")
    fillStore.send("Order WIP")
    fillStore.send("Order Ready")
    fillStore.send("Order Delivered")