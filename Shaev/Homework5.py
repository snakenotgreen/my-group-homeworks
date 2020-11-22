import string
def cezar(x, y, z):
    with open(x, 'r+', encoding='utf-8') as f:
        text = f.read().lower().split()
        for word in text:
            for letter in word:
                loc = string.ascii_letters.find(letter)
                new_letter = string.ascii_letters[loc + y]
                with open(z, 'a+', encoding='utf-8') as f:
                    f.write(new_letter.lower())


def uncezar(x, y, z):
    with open(x, 'r+', encoding='utf-8') as f:
        a = f.read().lower().split()
        for word in a:
            for letter in word:
                loc = string.ascii_lowercase.find(letter)
                new_letter = string.ascii_letters[loc - y]
                with open(z, 'a+', encoding='utf-8') as f:
                    f.write(new_letter.lower())


answer = input('Здравствуйте, вы желаете зашифровать или расшифровать файл? [code] [encode]')
try:
    if answer == 'code':
        cezar(input('Введите имя шифруемого файла [.txt]'),
              int(input('Введите ключ шифровки от 1 до 25')),
              input('Введите имя файла с будущим шифром [.txt]'))
    elif answer == 'encode':
        uncezar(input('Введите имя зашифрованого файла [.txt]'),
                int(input('Введите ключ шифровки от 1 до 25')),
                input('Введите имя файла с будущей расшифровкой [.txt]'))
except FileNotFoundError:
    print('Введите корректное имя файла! [.txt]')
except IndexError:
    print('Введите от 1 до 25!')
except ValueError:
    print('Введите именно число!')
