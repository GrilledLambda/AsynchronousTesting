import asyncio, time

#prints out even numbers
async def func1():
    evenNumbers = [num for num in range(50) if num % 2==0]
    for num in evenNumbers:
        await asyncio.sleep(1)
        print(num)

#prints out odd numbers
async def func2():
    oddNumbers = [num for num in range(50) if num % 2!=0]
    for num in oddNumbers:
        await asyncio.sleep(1)
        print(num)

#handles asynchronous method calling
async def main():
    await asyncio.gather(
        func1(),
        func2()
    )

asyncio.run(main())