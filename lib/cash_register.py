#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
            return
        self._discount = value

    
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
  
    def apply_discount(self):
        if len(self.items) == 0 or self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)

        final_total = int(round(self.total))

        print(f"After the discount, the total comes to ${final_total}.")

        self.total = final_total
    
    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])

