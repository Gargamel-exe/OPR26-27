import requests
import pprint

urlTrivia = "https://opentdb.com/api.php?amount=10&type=multiple"

kt = requests.get(urlTrivia).json()

rez = kt["results"]

for vprasanje in rez:
    print(vprasanje["question"])
    print("Možni odgovori:", vprasanje["incorrect_answers"] + [vprasanje["correct_answer"]])

    odgovor = input("Tvoj odgovor: ")

    if odgovor == vprasanje["correct_answer"]:
        print("Pravilno!")
    else:
        print("Napačno!")
        print("Pravilen odgovor je:", vprasanje["correct_answer"])








