import csv 
import string

def make_promocode(el):
    """ Создает промокод для товара на основе формулы: 
    Первые 2 буквы названия + день поступления + 2 предпоследних буквы названия в обратном порядке + месяц поступления в обратном порядке
        el - OrderedDict товара
    """
    date = el["Date"].split(".")
    promo = el["product"][:2].upper() +date[0]+el["product"][-1].upper()+el["product"][-2].upper()+date[1][::-1]
    return promo


with open("products.csv", encoding ="utf-8-sig") as file:
    data = list(csv.DictReader(file, delimiter=";"))[1:]
    for el in data:
        el['promocode'] = make_promocode(el)

with open("product_promo.csv","w", newline="", encoding ="utf-8-sig") as file:
    w = csv.DictWriter(file, fieldnames=["Category","product","Date","Price per unit","Count","promocode"])
    w.writeheader()
    w.writerows(data)
