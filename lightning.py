#Distance of a lightning Strike.py
#by Mathew Apanovich
#This program will help estimate the distance of a lightning strike relative to your position.

def strike():
    sec = eval(input("Roughly how many seconds were between the lightning flash and the sound of thunder?: "))
    speed = sec * 1100
    distance = speed/5280
    print("This is the estimated distance, in miles, the strike hit relative to your current position:",distance)
    
