from sys import argv
import csv
from json import dump, load

print("\n*** Rozszerzenie programu do zarządzania plikami csv ***\n")


# class ConsoleArgumentsAmountException(Exception):
#     def __str__(self):
#         return "Too few arguments give to console."


class Type:
    def __init__(self, input_file, output_file, changes_list):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_list = changes_list

    def file_read(self):
        pass

    def file_write(self):
        pass

    def set_changes(self):
        pass


class JSON(Type):
    def file_read(self):
        pass

    def file_write(self):
        pass

    def set_changes(self):
        pass


class CSV(Type):
    def file_read(self):
        with open(self.input_file) as file_stream:
            rows_list = []
            object_csv_file = csv.reader(file_stream)
            for row in object_csv_file:
                rows_list.append(row)
        return rows_list

    def file_write(self):
        pass

    def set_changes(self):
        pass


class TXT(Type):
    def file_read(self):
        with open(self.input_file) as file_stream:
            rows_list = []
            object_txt_file = file_stream.readline()
            while object_txt_file:
                object_txt_file = object_txt_file.removesuffix("\n")
                object_txt_file = object_txt_file.split(",")
                rows_list.append(object_txt_file)
                object_txt_file = file_stream.readline()

    def file_write(self):
        pass

    def set_changes(self):
        pass


# # Przykładowe wartości
# input_file, output_file, changes_list = "in.csv", "out.csv", ["0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]

if len(argv) < 3:
    print("Błąd - Zbyt mała liczba podanych argumentów.")
    exit()

# TODO Powyżej 3 czy 4 ?

try:
    if ".txt" in argv[1]:
        print("To jest txt.")
        file = TXT(argv[1], argv[2], argv[3:])
    elif ".json" in argv[1]:
        print("To jest json.")
        file = JSON(argv[1], argv[2], argv[3:])
    elif ".csv" in argv[1]:
        print("To jest csv.")
        file = CSV(argv[1], argv[2], argv[3:])
    else:
        print("Błąd - Niepoprawny format pliku.")
        exit()
except IndentationError:
    print("Błąd - Niewłaściwa ilość podanych argumentów.")
    exit()


print(file.file_read())







# rows_list = []
# changes_list_mod = []

# for change in changes_list:
#     changes_list_mod.append(change.split(","))
#
# try:
#     with open(input_file) as file:
#         object_csv_file = csv.reader(file)
#         for row in object_csv_file:
#             rows_list.append(row)
# except FileNotFoundError:
#     print("Błąd - niepoprawna ścieżka. Podaj właściwą ścieżkę do pliku wejściowego.")
#     exit()
#
# # print(rows_list_from_csv)
#
# try:
#     for changes in changes_list_mod:
#         row, column, name = changes
#         row = int(row)
#         column = int(column)
#         if row < 0 or column < 0:
#             print("Błąd - współrzędna ujemna. Podaj współrzędną równą lub większą od zera.")
#             exit()
#         rows_list[column][row] = name
# except ValueError:
#     print("Błąd - niewłaściwa wartość. Podaj właściwą wartość dla docelowych zmian. "
#           "Zmiany mają być w podane formacie \"x,y,z\" "
#           "(1. współrzędna, 2. współrzędna, nazwa)")
#     exit()
# except IndexError:
#     print("Błąd - zbyt duża wartość współrzędnej. Podaj właściwą wartość współrzędnych.")
#     exit()
#
# # print(rows_list_from_csv)
#
# with open(output_file, "w", newline="") as file:
#     # file.write(rows_list_from_csv)
#     write = csv.writer(file, delimiter=",")  # Utworzenie obiektu pliku csv
#     for row in rows_list:
#         write.writerow(row)
#
# print("Polecenie zostało wykonane pomyślnie.")
