# import logging
# logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


# def substraction(x, y):
#     return x, y


# def division(x, y):
#     if y != 0:
#         return x / y
#     else:
#         print("Pamiętaj cholero, nie dziel przez zero!")


# def addition(x, y, *args):
#     return x + y + sum(args)

   
# def multiplication(x, y, *args):
#     multi = 1
#     for number in args:
#         multi *= number
#     return x * y * multi


# def get_data(a: int):
#     if a == 1:
#         x = float(input("Proszę podaj odjemną: "))
#         y = float(input("Proszę podaj odjemnik: "))
#         return x, y
#     elif a == 2:
#         x = float(input("Proszę podaj dzielną: "))
#         y = float(input("Proszę podaj dzielnik: "))
#         return x, y
#     elif a == 3:
#         numbers_to_add = []
#         comp_number = int(input("Ile składników chciałbyś dodać? "))
#         for i in range(comp_number):
#             print(f"Proszę podaj składnik {i + 1}: ")
#             number = float(input())
#             numbers_to_add.append(number)
        
#         x = numbers_to_add[0]
#         y = numbers_to_add[1]
#         args = numbers_to_add[2:]
#         return x, y, args
#     elif a == 4:
#         numbers_to_multi = []
#         comp_number = int(input("Ile czynników chciałbyś pomnożyć? "))
#         for i in range(comp_number):
#             print(f"Proszę podaj czynnik {i + 1}: ")
#             number = float(input())
#             numbers_to_multi.append(number)
        
#         x = numbers_to_multi[0]
#         y = numbers_to_multi[1]
#         args = numbers_to_multi[2:]
#         return x, y, args     


# def choosing():

#     time_to_choose = """
#     Witamy w kalkulatorze!
#     Jakie działanie chciałbyś wykonać? Podaj odpowiednią liczbę:
#     1. Odejmowanie
#     2. Dzielenie
#     3. Dodawanie
#     4. Mnożenie
#     (Naciśnij 0 aby wyjść)
#     """
#     print(time_to_choose)
#     try:
#         operation = int(input())
#         if operation == 1:
#             x, y, args = get_data(1)
#             result = substraction(x, y)
#             print(f"Wynik odejmowania to {result}")       
#         elif operation == 2:
#             x, y, args = get_data(2)
#             result = division(x, y)
#             print(f"Wynik dzielenia to {result}")
#         elif operation == 3:
#             x, y, args = get_data(3)
#             result = addition(x, y, args)
#             print(f"Wynik dodawania to {result}")
#         elif operation == 4:
#             x, y, args = get_data(4)
#             result = multiplication(x, y, args)
#             print(f"Wynik mnożenia to {result}")
#         elif operation == 0:
#             print("Koniec gry!")
#             exit(1)
#         else:
#             print("Proszę wybrać odpowiedni numer")
#     except ValueError:
#         print("Proszę wybrać NUMER")

# while True:
#     choosing()