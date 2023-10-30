from sys import argv
import csv
from json import dump, load

print("\n*** Rozszerzenie programu do zarządzania plikami csv ***\n")


class ConsoleArgumentsAmountException(Exception):
    def __str__(self):
        return "Too few arguments give to console."


class Type:
    def __init__(self):
        self.input_file = argv[1]
        self.output_file = argv[2]
        self.changes_list = argv[3:]

class JSON(Type):
    pass


class CSV(Type):
    pass


class TXT(Type):
    pass


# try:
#     pass
# except IndentationError:
#     print("Błąd - Niewłaściwa ilość podanych argumentów.")
#     exit()
# except :
#     pass


# # Przykładowe wartości
# input_file, output_file, changes_list = "in.csv", "out.csv", ["0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]

if len(argv) < 3:
    print("Błąd - Zbyt mała liczba podanych argumentów.")
    exit()

try:
    input_file, output_file, changes_list = argv[1], argv[2], argv[3:]
except IndentationError:
    print("Błąd - Niewłaściwa ilość podanych argumentów.")
    exit()

    # print(input_file, output_file, changes_list)

rows_list_from_csv = []
changes_list_mod = []

for change in changes_list:
    changes_list_mod.append(change.split(","))

try:
    with open(input_file) as file:
        object_csv_file = csv.reader(file)
        for row in object_csv_file:
            rows_list_from_csv.append(row)
except FileNotFoundError:
    print("Błąd - niepoprawna ścieżka. Podaj właściwą ścieżkę do pliku wejściowego.")
    exit()

# print(rows_list_from_csv)

try:
    for changes in changes_list_mod:
        row, column, name = changes
        row = int(row)
        column = int(column)
        if row < 0 or column < 0:
            print("Błąd - współrzędna ujemna. Podaj współrzędną równą lub większą od zera.")
            exit()
        rows_list_from_csv[column][row] = name
except ValueError:
    print("Błąd - niewłaściwa wartość. Podaj właściwą wartość dla docelowych zmian. "
          "Zmiany mają być w podane formacie \"x,y,z\" "
          "(1. współrzędna, 2. współrzędna, nazwa)")
    exit()
except IndexError:
    print("Błąd - zbyt duża wartość współrzędnej. Podaj właściwą wartość współrzędnych.")
    exit()

# print(rows_list_from_csv)

with open(output_file, "w", newline="") as file:
    # file.write(rows_list_from_csv)
    write = csv.writer(file, delimiter=",")  # Utworzenie obiektu pliku csv
    for row in rows_list_from_csv:
        write.writerow(row)

print("Polecenie zostało wykonane pomyślnie.")
