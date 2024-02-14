import csv 
with open("products.csv", encoding ="utf-8-sig") as file:
    data = list(csv.DictReader(file, delimiter=";"))[1:]
    category_input = input()
    while category_input!="молоко":
        save_name = ""
        save_number = 100000.0
        flag = False
        for el in data:
            if el["Category"] == category_input:
                flag = True
                if float(el["Count"])<save_number:
                    save_number = float(el["Count"])
                    save_name = el["product"]

        if flag == True:
            print(f"В категории: {category_input} товар: {save_name} был куплен {save_number} раз")
        else:
            print("Такой категории не существует в нашей БД")
        category_input = input()

