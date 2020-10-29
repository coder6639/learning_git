import sys
import logging
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def substraction():
    try:
        first_number = float(input("Proszę podać pierwszą liczbę: "))
        try:
            second_number = float(input("Proszę podać drugą liczbę: "))
            result = first_number - second_number
            logging.info(f"Odejmuję {second_number} od {first_number}")
            print(f"Wynik działania to {result}")
        except:
            print("\nProszę podać LICZBĘ\n")
            substraction()
    except ValueError:
        print("\nProszę podać LICZBĘ\n")
        substraction()


def division():
    try:
        first_number = float(input("Proszę podać pierwszą liczbę: "))
        try:
            second_number = float(input("Proszę podać drugą liczbę: "))
            if second_number != 0:
                result = first_number / second_number
                logging.info(f"Dzielę {first_number} przez {second_number}")
                print(f"Wynik działania to {result}")
            else:
                print("Pamiętaj cholero, nie dziel przez zero!")
        except ValueError:
            print("\nProszę podać LICZBĘ\n")
            division()
    except ValueError:
        print("\nProszę podać LICZBĘ\n")
        division()


def addition():
    try:
        number_of_items = int(input("Ile liczb chciałbyś dodać? "))
        items_list = []
        sum_of_items = 0
        correct_numbers = True
        for i in range(number_of_items):
            number = input(f"Proszę podać liczbę numer {i + 1}: ")    
            items_list.append(number)
        
        for item in items_list:
            try:
                sum_of_items += float(item)
            except ValueError:
                correct_numbers = False
                sum_of_items = 0
                print("\n Podano niewłaściwą liczbę\n")
        
        if correct_numbers == True:  
            items_string = ', '.join(item for item in items_list)
            logging.info(f"Dodaję następujące liczby: {items_string}")
            print(f"Wynik działania to {sum_of_items}")
        else:
            addition()

    except ValueError:
        print("\nProszę wybrać LICZBĘ\n")
        addition()
   

def multiplication():
    try:
        number_of_items = int(input("Ile liczb chciałbyś pomnożyć? "))
        items_list = []
        multi_items = 1
        correct_numbers = True
        for i in range(number_of_items):
            number = input(f"Proszę podać liczbę numer {i + 1}: ")
            items_list.append(number)

        for item in items_list:
            try:
                multi_items *= float(item)
            except ValueError:
                correct_numbers = False
                multi_items = 1
                print("\n Podano niewłaściwą liczbę\n")

        if correct_numbers == True:  
            items_string = ', '.join(item for item in items_list)
            logging.info(f"Mnożę następujące liczby: {items_string}")
            print(f"Wynik działania to {multi_items}")
        else:
            multiplication()
        
    except ValueError:
        print("\nProszę wybrać LICZBĘ\n")
        multiplication()

def choosing():

    time_to_choose = """
    Witamy w kalkulatorze!
    Jakie działanie chciałbyś wykonać? Podaj odpowiednią liczbę:
    1. Odejmowanie
    2. Dzielenie
    3. Dodawanie
    4. Mnożenie
    (Naciśnij 0 aby wyjść)
    """
    print(time_to_choose)
    try:
        operation = int(input())
        if operation == 1:
            substraction()        
        elif operation == 2:
            division()
        elif operation == 3:
            addition()
        elif operation == 4:
            multiplication()
        elif operation == 0:
            print("Koniec gry!")
            exit(1)
        else:
            print("Proszę wybrać odpowiedni numer")
    except ValueError:
        print("Proszę wybrać NUMER")

while True:
    choosing()