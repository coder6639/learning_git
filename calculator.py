import logging
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

def substraction(x:float, y:float):
    return x - y


def division(x:float, y:float):
    if float(y) != 0:
        return x / y
    else:
        print("Pamiętaj cholero, nie dziel przez zero!")


def addition(tup):
    sum_of_items = sum(list(tup))
    return sum_of_items


def multiplication(tup):
    multi = 1
    for number in tup:
        multi *= float(number)
    return multi


def validate(*args) -> bool:
    """
    Sprawdzamy, czy wprowadzono poprawne liczby do kalkulatora
    """
    validity = True
    for arg in args:
        if (type(arg) == tuple) or (type(arg) == list):
            for item in arg:
                try:
                    number = float(item)
                except ValueError:
                    validity = False
        else:
            try:
                number = float(arg)
            except ValueError:
                validity = False
    return validity


def data_two(a:int):
    x = input(f"Proszę podaj {sub_div[a][0]}: ")
    y = input(f"Proszę podaj {sub_div[a][1]}: ")
    return x, y


def data_multi(x: int):
    to_be_multi = []
    elem = int(input(f"Ile liczb chciałbyś {add_multi[x][0]}? "))
    for i in range(elem):
        number = input(f"Proszę podać {add_multi[x][1]} {i + 1}: ")
        to_be_multi.append(number)
    return tuple(to_be_multi)

  
add_multi = [["dodać", "składnik", "Dodaję"], ["pomnożyć", "czynnik", "Mnożę"]]
sub_div = [["odjemna", "odjemnik", "Odejmuję"], ["dzielna", "dzielnik", "Dzielę"]]

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
    choice = input(time_to_choose)

    if choice == "1":
        a, b = data_two(0)
        if validate(a, b) == True:
            result = substraction(float(a), float(b))
            logging.info(f"{sub_div[0][2]} {b} od {a} ")
            print(f"Wynik odejmowania to {result}")
            return result
        else:
            print("Podano nieprawidłowe wartości")


    elif choice == "2":
        a, b = data_two(1)
        if validate(a, b) == True:
            result = division(float(a), float(b))
            logging.info(f"{sub_div[1][2]} {a} przez {b}")
            print(f"Wynik dzielenia to {result}")
            return result
        else:
            print("Podano nieprawidłowe wartości")


    elif choice == "3":
        float_list = []
        args = data_multi(0)
        if validate(args) == True:
            for item in args:
                float_list.append(float(item))
            result = addition(float_list)
            logging.info(f"{add_multi[0][2]} następujące liczby: {float_list}")
            print(f"wynik dodawania to {result}")
        else:
            print("Podano nieprawidłowe wartości")
    elif choice == "4":


        float_list = []
        args = data_multi(1)
        if validate(args) == True:
            for item in args:
                float_list.append(float(item))
            result = multiplication(float_list)
            logging.info(f"{add_multi[1][2]} następujące liczby: {float_list}")
            print(f"Wynik mnożenia to {result}")
        else:
            print("Podano nieprawidłowe wartości")
    

    elif choice == "0":
        print("Koniec gry!")
        exit(1)

    else:
        print("Proszę wybrać jedną z opcji!")

while True:
    choosing()