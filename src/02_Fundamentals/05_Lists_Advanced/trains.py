from typing import List

def leave_peoples(numbers, data):
    index = int(data[1])
    peoples = int(data[2])
    numbers[index] -= peoples

def insert_peoples(numbers, data):
    index = int(data[1])
    peoples = int(data[2])
    numbers[index] += peoples

def add_peoples(size, numbers, data):
    peoples = int(data[1])
    numbers[size - 1] += peoples

def run():
    size = int(input())
    numbers = [0] * size 
    while True:
        data = input().split(" ")
        if data[0].lower() == "end":
            break

        if data[0] == "add":
            add_peoples(size, numbers, data)
        elif data[0] == "insert":
            insert_peoples(numbers, data)
        elif data[0] == "leave":
            leave_peoples(numbers, data)
         
    print(numbers)

if __name__ == "__main__":
    run()