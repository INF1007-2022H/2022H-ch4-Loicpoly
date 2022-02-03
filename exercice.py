#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0


def remove_third_char(stri: str) -> str:
    a = stri.replace(stri[2],"")
    return a


def replace_char(stri: str, old_char: str, new_char: str) -> str:
    a = stri.replace(old_char, new_char, 1)
    return a


def get_number_of_char(stri: str, char: str) -> int:
    a = 0
    for i in range(len(stri)):
        if stri[i] == char:
            a += 1
    return a


def get_number_of_words(sentence: str, word: str) -> int:
    a = sentence.split()
    b = 0
    for i in range(len(a)):
        if a[i] == word:
            b += 1
    return b


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()



