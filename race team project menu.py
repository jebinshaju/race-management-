import racesql

username="admin"
password="admin"
print("^^^^^^^^^^^^^^^^^")
user=input("Enter your username::  ")
pas=input("Enter your password::  ")
print("^^^^^^^^^^^^^^^^^")
print("")
while user== username and pas==password:
    print("--RACE TEAM MANAGEMENT--".center(77,"🚗"))    
    print("")
    print("__________________________________________________________________________MAIN MENU_______________________________________________________________________________")
    print("")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print("                     ENTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 1 👈- to manage EVENTS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 2 👈-to manage CARS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 3 👈-to manage DRIVERS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 4 👈- to see the TEAM STATS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 5 👈- to see the due events and respective racers,(Auto selection)>>>~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 6 👈-to EXIT>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print("")
    option=int(input("Enter your option::"))
    
    if option==1:
        print("")
        print("🏁"*20)
        print("")
        print("-> a <- to ADD event.")
        print("-> b <- to REMOVE event.")
        print("-> c <- to VIEW event.")
        print("-> d <- to EDIT event. ")
        print("-> e <- to SEARCH event.")
        print("-> f <- to return to main menu.")
        print("")
        print("🏁"*20)
        print("")
        optionevent=input("Enter your option::")
        while True:
            

            if optionevent.lower() == "a":
                racesql.addevent()
                break
            elif optionevent.lower() =="b":
                racesql.removeevents()
                break
              
            elif optionevent.lower() == "c":
                racesql.displayevents()
                break
               
            elif optionevent.lower() == "d":
                print("")
                x=int(input("👉 1 to add position. \n 👉 2 to add prize money.\n 👉 3 to add expenses. \n 👉 4 to go back.\
                    Enter your option:  "))
                print("")
                while True:
                    if x==1:
                        racesql.addposition()
                        break
                    elif x==2:
                        racesql.addprizemoney()
                        break
                    elif x==3:
                        racesql.addexpenses()
                        break
                    else:
                        break
                break
             
                
            elif optionevent.lower() == "e":
                racesql.searchevent()
                break
                
            elif optionevent.lower() == "f":
                print("")
                print("Returning to menu....")
                print("")
                break
            else:
                print("")
                print("Enter a valid option!!!")
                pirnt("")
                break
            
    elif option==2:
        print("")
        print("🏎"*20)
        print("")
        print("-> a <- to ADD car.")
        print("-> b <- to REMOVE car.")
        print("-> c <- to VIEW cars.")
        print("-> d <- to EDIT car. ")
        print("-> e <- to SEARCH car.")
        print("-> f <- to return to menu.")
        print("")
        print("🏎"*20)
        print("")
        optioncar=input("Enter your option::  ")
        print("")
        while True:
            

            if optioncar.lower() == "a":
                racesql.addcar()  
                break
            elif optioncar.lower() == "b":
                racesql.removecars()
                break
            elif optioncar.lower() == "c":
                racesql.displaycars()
                break
            elif optioncar.lower() == "d":
                print("")
                w=int(input("👉 1 to add mileage.\n 👉 2 to add win.\n 👉 3 to go back.\n Enter your option: "))
                print("")
                while True:
                    if w==1:
                        racesql.addmileage()
                        break
                    elif w==2:
                        racesql.addwincar()
                        break
                    else:
                        break
                break
            elif optioncar.lower() == "e":
                racesql.searchcar()
                break
                
            elif optioncar.lower() == "f":
                print("")
                print("Returning to menu....")
                print("")
                break
            else:
                print("")
                print("Enter a valid option!!!")
                print("")
                break

    elif option==3:
        print("")
        print("🏃‍"*20)
        print("")
        print("-> a <- to ADD driver.")
        print("-> b <- to REMOVE driver.")
        print("-> c <- to VIEW driver.")
        print("-> d <- to EDIT driver. ")
        print("-> e <- to SEARCH driver.")
        print("-> f <- to return to main menu.")
        print("")
        optiondriver=input("Enter your option::  ")
        print("")
        print("🏃‍"*20)
        print("")
        while True:

            if optiondriver.lower() == "a":
                racesql.adddriver()
                break
                
            elif optiondriver.lower() == "b":
                racesql.removedrivers()
                break
            elif optiondriver.lower() == "c":
                racesql.displaydrivers()
                break
            elif optiondriver.lower() == "d":
                print("")
                w=int(input("👉 1 to add distance.\n 👉 2 to add win.\n 👉 3 to go back.\n Enter your option: "))
                print("")
                while True:
                    if w==1:
                        racesql.adddist()
                        break
                    elif w==2:
                        racesql.addwin()
                        break
                    else:
                        break
                
            elif optiondriver.lower() == "e":
                racesql.searchdriver()
                break
                
            elif optiondriver.lower() == "f":
                print("Returning to menu....")
                break
            
            else:
                print("Enter a valid option!!!")  
                break
    elif option==4:
        print("")
        print("-> a <- for positions")
        print("-> b <- to sort.")
        print("-> c <- financial stats.")
        print("-> d <- upcoming events. ")
        print("-> e <- finished events.")
        print("-> f <- to return to main menu.")
        print("")
        optionstats=input("Enter your option::  ")
        print("")
        while True:

            if optionstats.lower() == "a":
                racesql.positions()
                break
                
            elif optionstats.lower() == "b":
                racesql.sort()
                break
                
            elif optionstats.lower() == "c":
                racesql.financial()
                break
                
            elif optionstats.lower() == "d":
                racesql.upcomming()
                break
            elif optionstats.lower() == "e":
                racesql.finished()
                break
            elif optionstats.lower() == "f":
                print("")
                print("Returning to menu....")
                print("")
                break
            
            else:
                print("")
                print("Enter a valid option!!!")
                print("")
                break
    elif option==5:
        print("")
        print("_`````🚗🚗🚗``````_Auto select driver and cars_`````🚗🚗🚗`````_")
        print("")
        racesql.auto()
        

    elif option== 6:
        print("")
        break
    else:
        print("Enter a valid option!!!")
        break

        
