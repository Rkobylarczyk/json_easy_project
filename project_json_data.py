#importujemy bibliotekę json do pracy na plikach tego formatu
import json

#definiujemy klase, i funkcje, na podstawie której bedziemy potem tworzyc pola
class User:
    def __init__(self, _id, index, guid, age, eyeColor, name):
        self.id = _id
        self.index = index
        self.guid = guid
        self.age = age
        self.eyeColor = eyeColor
        self.name = name

#tworzymy reprezentanta, ktory zwraca nam caly wiersz w dictcie
    def __repr__(self):
#nie mam pojęcia czy da się zastąpić "F"
        return f"\n User id = {self.id},index = {self.index}, name = {self.name}, guid = {self.guid},age = {self.age}, kolor oczu = {self.eyeColor}"

#tworzymy dicta, ktory bedzie sie skladac z kilku wierszy
users_list = []
#otwieramy plik jako json_file
with open("generated.json", "r") as json_file:
#przypisujemy zmiennej user_data dekodowanie czytania json_file
    user_data = json.loads(json_file.read())
#dla każdego elementu w user_data dodaj element z klasy User (elementy okreslone przez parametry self i mające repra)
    for u in user_data:
#dodaje elementy z klasą User, każdy element
        users_list.append(User(**u))

#wypisz wszystko
print(users_list)