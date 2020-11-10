import mysql.connector
import datetime
from tabulate import tabulate
conn=mysql.connector.connect(host='localhost',user='root',passwd='123',charset="utf8")
cur=conn.cursor()
cur.execute("create database if not exists project")
cur.execute("use project")

def showtables():

    cur.execute("show tables")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id','Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="grid"))


    
cur.execute("create table if not exists events(Event_id int  primary key AUTO_INCREMENT,\
Event_name varchar(200) not null,\
Event_stage varchar(20),\
Event_date date,\
Total_distance int(100),\
Event_type varchar(20),\
Event_position int(10),\
Event_pricemoney int(20)\
,Event_expenses int(20))")
conn.commit()
cur.execute("alter table events auto_increment=100")
conn.commit()

cur.execute("create table if not exists car\
(Car_id int(200) primary key auto_increment,\
Car_name varchar(20) not null,\
Car_make varchar(20),\
Buy_date date,\
mileage int(100),\
Car_type varchar(200),\
Car_price int(200),No_of_wins int(20))")
conn.commit()
cur.execute("alter table car auto_increment=1000")
conn.commit()

cur.execute("create table if not exists driver\
(Driver_id int(200) primary key auto_increment,\
Driver_name varchar(20) not null,\
Joined_on date,\
DOB varchar(200),\
Total_km_raced int(100),\
Driver_type varchar(20),Driver_salary int(20),No_of_wins int(20))")
conn.commit()
cur.execute("alter table driver auto_increment=10000")
conn.commit()


print("SQL connected and tables created succesfully!!")


def obtaindate():
    try:
        print("--Year Month and Date--")
        y=int(input("Year        = "))
        m=int(input("Month       = "))
        d=int(input("Day         = "))
        x = datetime.datetime(y, m, d)
        return x #.strftime("%Y %m %d")
    except:
        print("Error entering date..")

def addevent():
    
    eventname=input("Enter the event name           :")
    eventstage=input("Enter the place/stage of event :")
    eventdate=obtaindate()
    eventdist=int(input("Enter the total distance           :"))
    eventtype=input("Enter the event type                  :")
        
    c="insert into events (Event_name,Event_stage,Event_date,Total_distance,Event_type)\
    values('{}','{}','{}',{},'{}')".format(eventname,eventstage,eventdate,eventdist,eventtype)
    cur.execute(c)
    conn.commit()
    print("")
    print("Event added succesfully!!!!")
        
       
       

def displayevents():
    cur.execute("select * from events")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id','Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="pretty"))

def removeevents():
    d=input("Enter the event name to be deleted:  ")
    cur.execute("delete from events where Event_name='{}'".format(d))
    conn.commit()
    print("Event Remmoved!!!")
    
def addposition():
    d=input("Enter the completed event's name:  ")
    pos=int(input('Enter the position after the race:  '))
    cur.execute("update table events set Event_position ={} where Event_name='{}'".format(pos,d))
    conn.commit()
    print("Position added!!!")

def addprizemoney():
    d=input("Enter the completed event     :  ")
    mon=int(input("Enter the recieved price money:  "))
    cur.execute("update table events set Event_pricemoney={} where Event_name='{}'".format(mon,d))
    conn.commit()
    print("Price money added!!!")

def addexpenses():
    d=input("Enter the completed event:  ")
    mon=int(input("Enter the race expenses  :  "))
    cur.execute("update table events set Event_expenses={} where Event_name='{}'".format(mon,d))
    conn.commit()
    print("Expenses added!!!")
    
def searchevent():
    d=input("Enter the name of event to be searched:  ")
    cur.execute("select * from events where Event_name like '%'{}'' ".format(d))
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id','Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="grid"))


def addcar():
     while True:
        print("")
        
        carname=input("Enter the car name        :")
        print("Manufacturing date::⬇👇⬇")
        carmake=obtaindate()
        print("Bought on date::⬇👇⬇")
        buydate=obtaindate()
        cardist=int(input("Enter the total mileage done:"))
        cartype=input("Enter the car type         :")
        carprice=int(input("Enter the car price        :"))
        
        cur.execute("insert into car (Car_name,Car_make,Buy_date,mileage,Car_type,Car_price) values('{}','{}','{}',{},'{}',{})".format(carname,carmake,buydate,cardist,cartype,carprice))
        conn.commit()
        print("")
        print("Car added succesfully!!!")
        print("-----👉👉👉 1 to add more cars 👈👈👈-------👉👉👉 2 to leave 👈👈👈------")
        print("")
        op=int(input("Enter your option:  "))
        print("")
        if op==2:
            break


def displaycars():
    cur.execute("select * from car")
    r=[]
    for i in cur:
        r.append(i)
    h=['Car_id','Car_name','Car_make','Buy_date','mileage','Car_type','Car_price']        
    print(tabulate(r,headers=h,tablefmt="grid"))

        


def removecars():
    d=input("Enter the Car_name to be deleted:")
    cur.execute("delete from car where Car_id='{}'".format(d))
    conn.commit()
    print("Car removed!!!")

def addmileage():
    cid=int(input("Enter the car id             :"))
    d=int(input("Enter the distance last raced:"))
    cur.execute("update car set mileage=mileage+{} where Car_id={}".format(d,cid))
    conn.commit()
    print("Mileage added!!!")

def searchcar():
    d=input("Enter the name of car to be searched:")
    cur.execute("select * from car where Car_name like '%'{}'' ".format(d))
    r=[]
    for i in cur:
        r.append(i)
    h=['Car_id','Car_name','Car_make','Buy_date','mileage','Car_type','Car_price']        
    print(tabulate(r,headers=h,tablefmt="grid"))

def addwincar():
    cid=int(input("Enter the car id:"))
    cur.execute("update car set No_of_wins int(20)=No_of_wins int(20)+1 where Car_id={}".format(cid))
    conn.commit()
    print("Number of win addded!!!")

def adddriver():
     while True:
        #driverid=int(input("Enter the driver id:  "))
        drivername=input("Enter the driver name:")
        print("Joined on:")
        joinedon=obtaindate()
        print("Date of birth:")
        dob=obtaindate()
        driverdist=int(input("Enter the total distance done by the driver:  "))
        drivertype=input("Enter the driver type:  ")
        driversalary=int(input("Enter the driver salary:  "))
        
        cur.execute("insert into driver (Driver_name,Joined_on,DOB,Total_km_raced,Driver_type,Driver_salary)\
            values('{}'','{}','{}',{},'{}',{})".format(\
                drivername,joinedon,dob,driverdist,drivertype,driversalary))
        conn.commit()
        print("")
        print("Driver added succesfully!!!")
        print("")
        print("-----👉👉👉 1 to add more drivers 👈👈👈-------👉👉👉 2 to leave 👈👈👈------")
        print("")
        op=int(input("Enter your option:  "))
        print("")
        if op==2:
            break


def displaydrivers():
    cur.execute("select * from driver")
    r=[]
    for i in cur:
        r.append(i)
    h=['Driver_id','Driver_name','Joined_on','DOB','Total_km_raced','Driver_type','Driver_salary']        
    print(tabulate(r,headers=h,tablefmt="grid"))



def removedrivers():
    d=input("Enter the driver ID to be removed:")
    cur.execute("delete from driver where Driver_id={}".format(d))
    conn.commit()
    print("Driver removed!!! ")

def adddist():
    did=int(input("Enter the driver id         :"))
    d=int(input("Enter the distance last raced:"))
    cur.execute("update driver set Total_km_raced=Total_km_raced+{} where Driver_id={}".format(d,did))
    conn.commit()
    print("Distance added!!!")

def addwin():
    did=int(input("Enter the driver id:"))
    cur.execute("update driver set No_of_wins int(20)=No_of_wins int(20)+1 where Driver_id={}".format(did))
    conn.commit()
    print("Number of win updated!!!")
def searchdriver():
    d=input("Enter the name driver to be searched:")
    print("")
    cur.execute("select * from driver where Driver_name like '%'{}'' ".format(d))
    r=[]
    for i in cur:
        r.append(i)
    h=['Driver_id','Driver_name','Joined_on','DOB','Total_km_raced','Driver_type','Driver_salary']        
    print(tabulate(r,headers=h,tablefmt="grid"))
   
def positions():
    cur.execute("select Event_name,Car_name,Driver_name,Event_position from driver,events,car where driver.Driver_type=\
    events.Event_type=car.Car_type order by Event_position ")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_name','Car_name','Driver_name','Event_position']        
    print(tabulate(r,headers=h,tablefmt="grid"))

def sort():
    cur.execute("select * from events order by Event_date")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="grid"))

def financial():
    cur.execute("select Event_name,Car_name,Event_pricemoney,Event_expenses,Car_price,Driver_salary,\
        Event_pricemoney - (Event_expenses + Car_price + Driver_salary)'Return'from driver,events,car where driver.Driver_type=\
    events.Event_type=car.Car_type order by Event_pricemoney")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_name','Car_name','Event_pricemoney','Event_expenses','Car_price','Driver_salary','Return']        
    print(tabulate(r,headers=h,tablefmt="grid"))

def upcomming():
    cur.execute("select * from events where Event_date>current_date()")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="grid"))

def finished():
    cur.execute("select * from events where Event_date < current_date()")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type']        
    print(tabulate(r,headers=h,tablefmt="grid"))
def auto():
    cur.execute("select Event_name,Car_name,Driver_name,Event_date from driver,events,car where driver.Driver_type=\
    events.Event_type=car.Car_type order by date ")
    r=[]
    for i in cur:
        r.append(i)
    h=['Event_name','Car_name','Driver_name','Event_date']        
    print(tabulate(r,headers=h,tablefmt="grid"))



