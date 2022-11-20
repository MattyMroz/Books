# łączenie 2 linii w 1 linię i zapis do pliku
def main():
    with open('1.1.txt', 'r') as f:
        for line in f:
            with open('1.1_out.txt', 'a') as f2:
                line = line.strip() + ' = ' + next(f).strip()
                f2.write(line + '\n')


main()

# zamiana słów za i przed zankiem występującym w tej linii
def main():
    with open('1.1_out.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if '=' in line:
                before = line.split('=')[0]
                after = line.split('=')[1]
                with open('1.1_out2.txt', 'a') as f2:
                    f2.write(after + ' = ' + before + '\n')


main()


# usuwanie numeracji stron z pliku tekstowego
a = open('3.txt', 'r', encoding="utf8")
b = open('t3.txt', 'w', encoding="utf8")

for line in a:
    if line[0] in '0123456789':
        continue
    else:
        b.write(line)

        
        
        
        
        
        
# Zamień nazyy plików na autonumerowanie zgodne z datą utworzenia
import os
import time

def filenameToTime():
    path = r'C:\Users\mateu\Downloads\SOLO LEVELING WEBTOON PL\R2'
    files = os.listdir(path)
    # dla karzdego pliku w folderze zamień jego nazwe na date modyfikacji co do sekundy z rozszerzeniem jpg jeśli data jest taka sama to dodaj _ + numer
    i = 0
    for file in files:
        # jeśli file kończy się na jpg to zmień nazwe
        # if file.endswith('.jpg'):
        # pobierz date modyfikacji pliku
        date = time.strftime(
            '%Y-%m-%d_%H-%M-%S', time.localtime(os.path.getmtime(path + '\\' + file)))
        # pobierz rozszerzenie pliku
        extension = file.split('.')[-1]
        # zmień nazwe pliku na date sprawżdź czy plik o tej samej nazwie istnieje jeśli tak to dodaj 1 do sekundy
        if not os.path.exists(path + '\\' + date + '.' + extension):
            os.rename(path + '\\' + file, path +
                      '\\' + date + '.' + extension)
        else:
            os.rename(path + '\\' + file, path + '\\' +
                      date + '_' + str(i) + '.' + extension)
            i += 1


def autoNumericFilename():
    path = r'C:\Users\mateu\Downloads\SOLO LEVELING WEBTOON PL\R2'
    files = os.listdir(path)
    n = 1
    # zamień nazwy wszystkich polików z rozszerzeniem jpg na kolejne liczby n
    for file in files:
        # if file.endswith('.jpg'):
        os.rename(path + '\\' + file, path + '\\' + str(n) + '.jpg')
        n += 1


def main():
    filenameToTime()
    autoNumericFilename()


if __name__ == "__main__":
    main()


# # folder in autonumeric foder numeric xd
# import os
# import time

# frist = 1
# last = 179


# def filenameToTime():
#     for j in range(frist, last + 1):
#         path = r'C:\Users\mateu\Downloads\SOLO LEVELING WEBTOON PL\R' + str(j)
#         files = os.listdir(path)
#         i = 0
#         for file in files:
#             # if file.endswith('.jpg'):
#             date = time.strftime(
#                 '%Y-%m-%d_%H-%M-%S', time.localtime(os.path.getmtime(path + '\\' + file)))
#             extension = file.split('.')[-1]
#             if not os.path.exists(path + '\\' + date + '.' + extension):
#                 os.rename(path + '\\' + file, path +
#                           '\\' + date + '.' + extension)
#             else:
#                 os.rename(path + '\\' + file, path + '\\' +
#                           date + '_' + str(i) + '.' + extension)
#                 i += 1


# def autoNumericFilename():
#     for j in range(frist, last + 1):
#         path = r'C:\Users\mateu\Downloads\SOLO LEVELING WEBTOON PL\R' + str(j)
#         files = os.listdir(path)
#         n = 1
#         for file in files:
#             # if file.endswith('.jpg'):
#             os.rename(path + '\\' + file, path + '\\' + str(n) + '.jpg')
#             n += 1


# def main():
#     filenameToTime()
#     autoNumericFilename()


# if __name__ == "__main__":
#     main()
