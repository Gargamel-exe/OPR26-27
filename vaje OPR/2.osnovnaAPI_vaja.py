#api vaje
#ugotovi najstarejše ime
#enumerate
"""
print(list(enumerate(imena)))

for i,ime in enumerate(imena):
    print(i,ime)
"""


#ugotovi najstarejše ime
import requests

imena = ["jaka", "lojze", "kris"]

seznam = []

for ime in imena:
    response = requests.get(
        "https://api.agify.io",
        params={"name": ime}
    )

    podatki = response.json()
    print(podatki)

    seznam.append(podatki)

print(seznam)


najstarejsi = seznam[0]

for oseba in seznam:
    if oseba["age"] > najstarejsi["age"]:
        najstarejsi = oseba

print("Najstarejše ime je:", najstarejsi["name"])
print("Ocenjena starost je:", najstarejsi["age"])

