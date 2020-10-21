lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola", "groszek"]
}
for store in lista_zakupow.keys():
    correct_list = []
    for item in lista_zakupow[store]:
        correct_list.append(item.capitalize())
    
    print(f"Idę do {store.capitalize()} i kupuję tam {correct_list}")