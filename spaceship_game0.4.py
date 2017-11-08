#Andrew Hilton, 4th pd, 10/12/17
NAME=" "
PLANET=" "
WEIGHT=" "
SPEED=" "
NEXT_PLANET=" "
SCORE=0

def escape_earth():
    global SPEED
    global PLANET
    global SCORE
    SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
    if SPEED > 11 and SPEED < 12:
        print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
        SCORE = SCORE + 1
        print("Your score is " +str(SCORE))
        PLANET = NEXT_PLANET
        escape_planet()
    elif SPEED < 12:
        print("Too slow, you DIED.")
        SCORE = 0
        escape_earth()
    elif SPEED > 11:
        print("Too fast, you DIED.")
        SCORE = 0
        escape_earth()
    else:
        print("Invalid Inputs! (Use numbers including decimals)")
        escape_earth()

def escape_planet():
    global PLANET
    global NEXT_PLANET
    global SCORE
    NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
    PLANET = NEXT_PLANET
    global SPEED
    if PLANET == "pluto":
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 1.1 and SPEED < 1.5:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
            
        elif SPEED < 1.5:
             print("Too slow, you DIED.")
             SCORE = 0
             escape_planet()
        elif SPEED > 1.1:
             print("Too fast, you DIED.")
             SCORE = 0
             escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "mercury":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 4.1 and SPEED < 4.4:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 4.4:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 4.1:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()


    elif PLANET == "venus":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 10.1 and SPEED < 10.5:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 10.5:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 10.1:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "mars":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 4.6 and SPEED < 5.5:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 5.5:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 4.6:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "jupiter":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 60 and SPEED < 63.4:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 63.4:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 60:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "saturn":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 35 and SPEED < 37:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 37:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 35:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "uranus":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 21 and SPEED < 22.6:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 22.6:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 21:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    elif PLANET == "neptune":
#        NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
        SPEED = float(input("How fast do you want to go in km/s " +NAME+"?" " (Decimals are allowed)"))
        if SPEED > 23.3 and SPEED < 24.7:
            print("You escaped the planet! You are now on; " +NEXT_PLANET+ ".")
            SCORE = SCORE + 1
            print("Your score is " +str(SCORE))
            PLANET = NEXT_PLANET
            escape_planet()
        elif SPEED < 24.7:
            print("Too slow, you DIED.")
            SCORE = 0
            escape_planet()
        elif SPEED > 23.3:
            print("Too fast, you DIED.")
            SCORE = 0
            escape_planet()
        else:
            print("Invalid Inputs! (Use numbers including decimals)")
            escape_planet()

    else:
        print("ERROR")
        escape_planet()

def startup():
    global NAME
    print("Welcome to Spaceship Game One")
    print("The point of this game is to choose your speed to jump")
    print("between different planets, using your weight and gravity")
    print("to your advantage.")
    NAME = input("What is your name?")
    
def start_menu():
    global NAME
    global PLANET
    global NEXT_PLANET
    print("1. Start Game\n2. Load Planet\n3. Quit Game")
    choice = input("Enter a number to select an option, " +NAME)
    if choice =="1":
        start()
    elif choice =="2":
        NEXT_PLANET = input("Which planet would you like to start on? (all undercase)")
        PLANET = NEXT_PLANET
        escape_planet()
    elif choice =="3":
        quit()
    else:
        start_menu()
        
def start():
    global WEIGHT
    global SPEED
    global PLANET
    global NAME
    global NEXT_PLANET
    PLANET = "earth"
    print("You are on planet Earth")
    WEIGHT = input("How much does the ship weigh in pounds?")
    NEXT_PLANET = input("Where do you want to go from here? Enter a planet in our solar system in lowercase.")
    escape_earth()
    
startup()
start_menu()
