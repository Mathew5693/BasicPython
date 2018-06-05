#A program that accepts a value to test if it is prime
#Mathew Apanovich
#Exercise5


def main():
    n = input("input a number you would like to test: ")
    n = int(n)
    if n%2==0:
        print(n,"is not a prime number!")

    elif n%2 ==1:
        print(n,"is a prime number!")
main()
