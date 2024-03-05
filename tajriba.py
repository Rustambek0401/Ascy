import json
with open("data1.json", "r") as fayl:
    data = json.load(fayl)
    ismi = []
    narxi = []
    for i in data["kurs"]:
        ismi.append(i["name"])
        narxi.append(i["price"])

with open("data2.json", "w") as fayl:
    for i in ismi:
        fayl.write(i)
    for j in narxi:
        fayl.write(str(j))