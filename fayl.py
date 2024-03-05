import json
import asyncio
async def task1(ismi,narxi):
    with open("task2.json", "r") as fayl:
        data = json.load(fayl)
        for i in range(len(ismi)):
            dict1 = {"ismi": ismi[i], "narxi": narxi[i]}
            data["kurs"].append(dict1)

    with open("task2.json", "w") as fayl:
        json.dump(data, fayl, indent=4)
    print("ma'lumotlari qo'shildi:")

async def task2():
    with open("data1.json", "r") as fayl:
        data = json.load(fayl)
        ismi = []
        narxi = []
        for i in data["kurs"]:
            ismi.append(i["name"])
            narxi.append(i["price"])
        asyncio.run(task1(ismi,narxi))
        print("MAlumot qo'shilishga jo'natdi ")
async def main():
    await asyncio.gather(task2())
if __name__ == "__main__":
    asyncio.run(main())