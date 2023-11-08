from sys import argv
import csv
from json import dump, load

print("\n*** Rozszerzenie programu do zarządzania plikami csv ***\n")


class Type:
    def __init__(self, input_file, output_file, changes_list):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_list = changes_list

    def file_read(self):
        pass

    def file_write(self, changed_file):
        if ".txt" in self.output_file or ".csv" in self.output_file:
            file_to_convert = []
            for element in changed_file:
                file_to_convert.append(",".join(element))

            with open(self.output_file, "w") as file_stream:
                for element in file_to_convert:
                    file_stream.write(element)
                    file_stream.write("\n")

        elif ".json" in self.output_file:
            with open(self.output_file, "w") as file_stream:
                dump(changed_file, file_stream)

    def set_changes(self, list_to_mod):
        changes_list_mod = []
        for change in self.changes_list:
            changes_list_mod.append(change.split(","))

        for changes in changes_list_mod:
            row, column, name = changes
            row = int(row)
            column = int(column)
            if row < 0 or column < 0:
                print("Błąd - współrzędna ujemna. Podaj współrzędną równą lub większą od zera.")
                exit()
            list_to_mod[column][row] = name
        return list_to_mod


class JSON(Type):
    def file_read(self):
        with open(self.input_file) as file_stream:
            rows_list = load(file_stream)
        return rows_list


class CSV(Type):
    def file_read(self):
        with open(self.input_file) as file_stream:
            rows_list = []
            object_csv_file = csv.reader(file_stream)
            for row in object_csv_file:
                rows_list.append(row)
        return rows_list


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
            return rows_list


# print(argv)

if len(argv) < 3:
    print("Błąd - Zbyt mała liczba podanych argumentów.")
    exit()

try:
    if ".txt" in argv[1]:
        file = TXT(argv[1], argv[2], argv[3:])
    elif ".json" in argv[1]:
        file = JSON(argv[1], argv[2], argv[3:])
    elif ".csv" in argv[1]:
        file = CSV(argv[1], argv[2], argv[3:])
    else:
        print("Błąd - Niepoprawny format pliku wejściowego.")
        exit()
except IndentationError:
    print("Błąd - Niewłaściwa ilość podanych argumentów.")
    exit()

if ".txt" not in argv[2] and ".json" not in argv[2] and ".csv" not in argv[2]:
    print("Błąd - Niespodziewany format pliku wyjściowego.")
    exit()


try:
    changed_file = file.set_changes(file.file_read())
    file.file_write(changed_file)
    # print(changed_file)
except ValueError:
    print("Błąd - niewłaściwa wartość. Podaj właściwą wartość dla docelowych zmian. "
          "Zmiany mają być w podane formacie \"x,y,z\" "
          "(1. współrzędna, 2. współrzędna, nazwa)")
    exit()
except IndexError:
    print("Błąd - zbyt duża wartość współrzędnej. Podaj właściwą wartość współrzędnych.")
    exit()
except FileNotFoundError:
    print("Błąd - niepoprawna ścieżka. Podaj właściwą ścieżkę do pliku wejściowego.")
    exit()


print("Polecenie zostało wykonane pomyślnie.")
