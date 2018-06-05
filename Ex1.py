#A program to create acronyms
#Mathew Apanovich
#Acronym.py

def main():
    sentence = input("Enter your sentence:")
    words = sentence.split()
    acro = [i[0].upper()for i in words]
    print("".join(acro))
