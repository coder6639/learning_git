lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola", "groszek"]
}

sum_of_products = 0

for store in lista_zakupow.keys():
    sum_of_products += len(lista_zakupow[store])
    correct_list = []
    for item in lista_zakupow[store]:
        correct_list.append(item.capitalize())
    
    print(f"Idę do {store.capitalize()} i kupuję tam {correct_list}")

print(f"W sumie kupuję {sum_of_products} produktów")