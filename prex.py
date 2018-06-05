#A program to convert the date to Month Day, Year
#Mathew Apanovich
#W5Ex2

def main():
    day, month, year = eval(input("Please give date numbers for Day, Month, and Year:"))
    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", "May", ",June", "July", "Auguest", "September", "October", "November", "December"]

    monthstr = months[month-1]
    date2 = monthstr+" " + str(day) + ", " + str(year)

    print("The date is", date1, "or", date2+".")
    
