import asyncio
async def task2(son):
    # await asyncio.sleep()
    s = son[-1::-1]
    son = int(son)
    s = int(s)
    if s == son:
        print(f"{True} str")
    else:
        print(False)
async def task1(a):
    # await asyncio.sleep()
    d = a
    t = 0
    while a > 0:
        s = a % 10
        t = t * 10 + s
        a = a // 10
    if d == t:
        print(f"{True} sonlik")
    else:
        print(False)
async def main():
    son = input("SON: ")
    a = int(input("A: "))
    # task_2 = task2(son)
    # task_1 = task1(a)

    await asyncio.gather(task1(a), task2(son))

if __name__ == "__main__":
    asyncio.run(main())
