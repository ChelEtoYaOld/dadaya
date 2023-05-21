import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Papa:
    salary = 33000
    age = 33

    def about(self):
        print("i am Papa")
    def about_myself(self):
        print('I am GrandParent')


class Mama(Papa):
    grade = 8
    utility = 0

    def about_myself(self):
        print('I am Mama')


class Mikrochel(Mama):
    dota2 = 100
    def __init__(self):
        super().about()
        super().about_myself()
        print('I am Misha')


misha = Mikrochel()

print(Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + "Posle kontrakta")
print(f'Nu vse hulyaem u menya zarplata {Papa.salary}!')
print(Style.BRIGHT + Fore.CYAN + "Nu vse go dota!")
print(f'U menya ocenka {Mikrochel.grade}')
print(Style.BRIGHT + Fore.BLUE + "Mama molodec!")
print(f'Po domu vse {Mama.utility}!')
print(Style.BRIGHT + Fore.RED + "NEIN SCHEISSE!")
print(f'Ich spiele {Mikrochel.dota2} Stunden in Dota?!??!!!1')