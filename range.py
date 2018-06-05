#A program to find the cubes of the n value
#Mathew Apanovich
#Exercise12.py

def main():
    n = eval(input("Please enter any natural number:"))
    n1 = 0
    for i in range(n):
        n1 = n1 + i**3
    print(n1)
