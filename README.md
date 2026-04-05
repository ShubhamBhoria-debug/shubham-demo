# shubham-demo
This is my First repo
<br>
Author-Shubham bhoria
<br>
from abc import ABC,abstractmethod
import math

class Discount:
    @staticmethod
    def apply_discount(self,amount):
        raise

class PercentageDiscount(Discount):
    def __init__(self,percentage):
        self.percentage=percentage
    def apply_discount(self, amount):
        return amount* (1-self.percentage /100)
    
class FixedDiscount(Discount):
    def __init__(self,amount_off):
        self.amount_off=amount_off

    def apply_discount(self, amount):
        return amount-self.amount_off
    
class Cart:
    def __init__(self,price):
        self.total=sum(price)
    def calculate_final_total(self,discount_type):
        return discount_type.apply_discount(self.total)
    
my_cart=Cart([1000,2000,3000])

promo1=PercentageDiscount(10)
promo2=FixedDiscount(500)

print(f"final with 10% off:{my_cart.calculate_final_total(promo1)}")
print(f"final with RS 500 off:{my_cart.calculate_final_total(promo2)}")

print(f"final with RS 500 off:{my_cart.calculate_final_total(promo2)}")
