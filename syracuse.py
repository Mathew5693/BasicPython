#A program that uses imput for the syracuse formula.
#Mathew Apanovich
#ProgrammingEx4

def main():
    x = eval(input("Please enter a number: "))
    n = 0
    while x != 1:
        if (x % 2 == 0):
            n = x//2
            print("Syracuse value =", n)
            x = n
            n = n + 1
        else:
            n = x*3+1
            print("Syracuse value =", n)
            x = n
            n = n + 1

main()
