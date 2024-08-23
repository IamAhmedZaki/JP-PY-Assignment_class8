from item import Item

class Laptop(Item):
    discount=0.3
    all=[]
    def __init__(self, name: str, price: float, gpu:str, quantity=0, port_count=0):
        super().__init__(name, price, quantity)
        
        self._price=self.price * Laptop.discount
        self.gpu=gpu
        self.port_count=port_count
        