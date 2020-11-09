import racesql

username="admin"
password="admin"
print("^^^^^^^^^^^^^^^^^")
user=input("Enter your username::  ")
pas=input("Enter your password::  ")
print("^^^^^^^^^^^^^^^^^")
print("")
while user== username and pas==password:
    print("--------------------RACE TEAM MANAGEMENT----------------------")
    print("___MAIN MENU___")
    print("")
    print("Enter -> 1 <- to manage EVENTS.")
    print("Enter -> 2 <- to manage CARS.")
    print("Enter -> 3 <- to manage DRIVERS.")
    print("Enter -> 4 <- to see the TEAM STATS. ")
    print("Enter -> 5 <- to see the due events and respective racers:")
    print("Enter -> 6 <- to EXIT. ")
    print("")
    option=int(input("Enter your option::  "))
    
    if option==1:
        print("")
        print("Enter -> a <- to ADD event.")
        print("Enter -> b <- to REMOVE event.")
        print("Enter -> c <- to VIEW event.")
        print("Enter -> d <- to EDIT event. ")
        print("Enter -> e <- to SEARCH event.")
        print("Enter -> f <- to return to main menu.")
        print("")
        optionevent=input("Enter your option::  ")
        while True:
            

            if optionevent.lower() == "a":
                racesql.addevent()
            elif optionevent.lower() =="b":
                racesql.removeevents()
              
            elif optionevent.lower() == "c":
                racesql.displayevents()
               
            elif optionevent.lower() == "d":
                x=int(input("Enter 1 to add position. \n Enter 2 to add prize money.\n Enter 3 to add expenses. \n Enter 4 to go back.\
                    Enter your option:  "))
                while true:
                    if x==1:
                        racesql.addposition()
                    elif x==2:
                        racesql.addprizemoney()
                    elif x==3:
                        racesql.addexpenses()
                    else:
                        break

             
                
            elif optionevent.lower() == "e":
                racesql.searchevent()
                
            elif optionevent.lower() == "f":
                print("Returning to menu....")
                break
            else:
                print("Enter a valid option!!!")
                break
            
    elif option==2:
        print("")
        print("Enter -> a <- to ADD car.")
        print("Enter -> b <- to REMOVE car.")
        print("Enter -> c <- to VIEW cars.")
        print("Enter -> d <- to EDIT car. ")
        print("Enter -> e <- to SEARCH car.")
        print("Enter -> f <- to return to menu.")
        print("")
        optioncar=input("Enter your option::  ")
        while True:
            

            if optioncar.lower() == "a":
                racesql.addcar()  
            elif optioncar.lower() == "b":
                racesql.removecars()
                
            elif optioncar.lower() == "c":
                racesql.displaycars()
                
            elif optioncar.lower() == "d":
                w=int(input("Enter 1 to add mileage.\n Enter 2 to add win.\n Enter 3 to go back.\n Enter your option: "))
                while True:
                    if w==1:
                        racesql.addmileage()
                    elif w==2:
                        racesql.addwincar()
                
            elif optioncar.lower() == "e":
                racesql.searchcar()
                
            elif optioncar.lower() == "f":
                print("Returning to menu....")
                break
            else:
                print("Enter a valid option!!!")
                break

    elif option==3:
        print("")
        print("Enter -> a <- to ADD driver.")
        print("Enter -> b <- to REMOVE driver.")
        print("Enter -> c <- to VIEW driver.")
        print("Enter -> d <- to EDIT driver. ")
        print("Enter -> e <- to SEARCH driver.")
        print("Enter -> f <- to return to main menu.")
        print("")
        optiondriver=input("Enter your option::  ")

        if optiondriver.lower() == "a":
            racesql.adddriver()
            
        elif optiondriver.lower() == "b":
            racesql.removedrivers()
            
        elif optiondriver.lower() == "c":
            racesql.displaydrivers()
            
        elif optiondriver.lower() == "d":
            w=int(input("Enter 1 to add distance.\n Enter 2 to add win.\n Enter 3 to go back.\n Enter your option: "))
            while True:
                if w==1:
                    racesql.adddist()
                elif w==2:
                    racesql.addwin()
            
        elif optiondriver.lower() == "e":
            racesql.searchdriver()
            
        elif optiondriver.lower() == "f":
            print("Returning to menu....")
            break
        
        else:
            print("Enter a valid option!!!")  
            break
    elif option==4:
        print("")
        print("Enter -> a <- for positions")
        print("Enter -> b <- to sort.")
        print("Enter -> c <- financial stats.")
        print("Enter -> d <- upcoming events. ")
        print("Enter -> e <- finished events.")
        print("Enter -> f <- to return to main menu.")
        print("")
        optionstats=input("Enter your option::  ")
        while True:

            if optionstats.lower() == "a":
                racesql.positions()
                
            elif optionstats.lower() == "b":
                racesql.sort()
                
            elif optionstats.lower() == "c":
                racesql.financial()
                
            elif optiondriver.lower() == "d":
                racesql.upcomming()
                
            elif optionstats.lower() == "e":
                racesql.finished()
                
            elif optionstats.lower() == "f":
                print("Returning to menu....")
                break
            
            else:
                print("Enter a valid option!!!")
                break
    elif option==5:
        print("__Auto select driver and cars__")
        racesql.auto()

    elif option== 6:
        print("")
        break
    else:
        print("Enter a valid option!!!")
        break

        
