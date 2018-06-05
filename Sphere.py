#A program that will calcualte the volume and surface area of a sphere
#by Mathew Apanovich
#Sphere.py

def main():
    r = eval(input("Please enter the radius of the sphere: "))
    c = r*r*r
    s = r*r
    V = (4/3)*3.14*c
    A = 4*3.14*s
    print("The radius given is",r)
    print("The Volume would equal:",V)
    print("The Area would equal:",A)
