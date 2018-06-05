#Programming exercise 4
#Mathew Apanovich
#A program to out put the sum of all cubes of n natural numbers

def cude(n):

    x = 0
    for i in range(1,n+1,1):
        x = x+ i**3
        
    return x
def main():
    n = eval(input("Please enter natural number:"))
    z = cude(n)
    print(z)
    

