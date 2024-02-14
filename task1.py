import csv 

with open("products.csv", encoding ="utf-8-sig") as file:
    data = list(csv.DictReader(file, delimiter=";"))[1:]
    sum = 0
    for el in data:
        el['total'] = float(el["Price per unit"])*float(el["Count"])
    for el in data:
        if el['Category'] == "Закуски":
            sum+= el['total'] 
    print("Итоговая сумма по категории Закуски:" ,sum)

with open("products_new.csv","w", newline="", encoding ="utf-8-sig") as file:
    w = csv.DictWriter(file, fieldnames=["Category","product","Date","Price per unit","Count","total"])
    w.writeheader()
    w.writerows(data)
