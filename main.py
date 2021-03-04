from math import *

#. Napisz pierwszy skrypt,
# w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

a = 2
b = 0.5
print(a,b)

#Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne


a = 5
b = 2
c = 7

dzielenie = a / b
print(dzielenie)

dodawanie = b + c
print(dodawanie)

dzielenie_calkowite = a // c
print(dzielenie_calkowite)

odejmowanie = a - b
print(odejmowanie)

mnozenie = b * c
print(mnozenie)

#. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

a-=b
print(a)
a+=b
print(a)
a/=c
print(a)
a*=b
print(a)
a**=2
print(a)
b%=a
print(b)

#Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
#Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka
#a pozostałe małe. (trzeba użyć metody capitalize)

imie = "ANGELIKA"
nazwisko = "LAZORYSZYN"
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie,nazwisko)

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki
# z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)

piosenka = "la la la la la"
print(piosenka.count("la"))

#7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę,
# wykorzystując indeksy.

imie = "Angelika"
print(imie[3])

#Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy.
# (trzeba użyć metody split)
print(piosenka.split())


#Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.

heksad = 126
srednia = 3.56
int = 50

print(hex(heksad), srednia, int)
