import mysql.connector
import datetime

conn=mysql.connector.connect(host='localhost',user='root',passwd='123',charset="utf8")
cur=conn.cursor()
cur.execute("create database if not exists project")
cur.execute("use project")
cur.execute("show tables")

    
cur.execute("create table if not exists events(Event_id int auto_increment primary key,\
Event_name varchar(200) not null,\
Event_stage varchar(20),\
Event_date date,\
Total_distance int(100),\
Event_type varchar(20),\
Event_position int(10),\
Event_pricemoney int(20)\
,Event_expenses int(20))")
cur.commit()

cur.execute("create if not exists table car\
(Car_id int(200) primary key auto_increment,\
Car_name varchar(20) not null,\
Car_make varchar(20),\
Buy_date date,\
mileage int(100),\
Car_type varchar(200),\
Car_price int(200),No_of_wins int(20))")
cur.commit()

cur.execute("create if not exists table driver\
(Driver_id int(200) primary key auto_increment,\
Driver_name varchar(20) not null,\
Joined_on date,\
DOB varchar(200),\
Total_km_raced int(100),\
Driver_type varchar(20),Driver_salary int(20),No_of_wins int(20))")
cur.commit()



print("SQL connected and tables created succesfully!!")

def obtaindate():
    y=int(input("Year    = "))
    m=int(input("Month= "))
    d=int(input("Day    = "))
    x = datetime.datetime(y, m, d)
    return x.strftime("%y","%m","%d")

def addevent():
     while True:
        #eventid=int(input("Enter the event id:  "))
        eventname=input("Enter the event name              :  ")
        eventstage=input("Enter the place/stage of event:  ")
        eventdate=obtaindate()
        eventdist=int(input("Enter the total distance           :  "))
        eventtype=input("Enter the event type                  :  ")
        x=[eventid,eventname,eventstage,eventdate,eventdist,eventtype]
        cur.execute("insert into events (Event_name,Event_stage,Event_date,Total_distance,Event_type)values('{}','{}','{}','{}','{}')".format(eventname,eventstage,eventdate,eventdist,eventtype))
        cur.commit()
        print("Enter '1' to add more events.")
        print("Enter '2' to return to main menu.")
        op=int(input("Enter your option:  "))
        if op==2:
            break

def displayevents():
    cur.execute("select * from events")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_id','Event_name','Event_stage','Event_date','Total_distance','Event_type',sep="\t")
            print(i,sep="\t")

def removeevents():
    d=input("Enter the event ID to be deleted:  ")
    cur.execute("delete from events where Event_id='{}'".format(d,))
    cur.commit()
    
def addposition():
    d=input("Enter the completed event's name:  ")
    pos=int(input('Enter the position after the race:  '))
    cur.execute("update table events set Event_position ='{}' where Event_name='{}'".format(pos,d))
    cur.commit()

def addprizemoney():
    d=input("Enter the completed event:  ")
    mon=int(input("Enter the recieved price money:  "))
    cur.execute("update table events set Event_pricemoney='{}' where Event_name='{}'".format(mon,d))
    cur.commit()

def addexpenses():
    d=input("Enter the completed event:  ")
    mon=int(input("Enter the race expenses:  "))
    cur.execute("update table events set Event_expenses='{}''{}' where Event_name='{}'".format(mon,d))
    cur.commit()
    
def searchevent():
    d=input("Enter the name of event to be searched:  ")
    cur.execute("select * from events where Event_name like '%'{}'' ".format(d,))
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type',sep="\t")
            print(i,sep='\t')

def addcar():
     while True:
        #carid=int(input("Enter the car id:  "))
        carname=input("Enter the car name:  ")
        carmake=obtaindate()
        buydate=obtaindate()
        cardist=int(input("Enter the total mileage done:  "))
        cartype=input("Enter the car type:  ")
        carprice=int(input("Enter the car price:  "))
        
        cur.execute("insert into car (Car_name,Car_make,Buy_date,mileage,Car_type,Car_price) values('{}','{}','{}','{}','{}','{}')".format(carname,carmake,buydate,cardist,cartype,carprice))
        cur.commit()
        print("Enter '1' to add more cars.")
        print("Enter '2' to return to menu.")
        op=int(input("Enter your option:  "))
        if op==2:
            break

def displaycars():
    cur.execute("select * from cars")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Carid','Carname','Carmake','Buydate','cardist','cartype','carprice',sep="\t")
            print(i,sep="\t")

        


def removecars():
    d=input("Enter the car ID to be deleted:  ")
    cur.execute("delete from cars where Car_id='{}'".format(d,))
    cur.commit()

def addmileage():
    cid=int(input("Enter the car id"))
    d=int(input("Enter the distance last raced:  "))
    cur.execute("update cars set mileage=mileage+'{}' where Car_id='{}'".format(d,cid))
    cur.commit()

def searchcar():
    d=input("Enter the name of car to be searched:  ")
    cur.execute("select * from cars where Car_name like '%'{}'' ".format(d,))
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Carid','Carname','Carmake','Buydate','cardist','cartype','carprice',sep="\t")
            print(i,sep="\t")

def addwincar():
    cid=int(input("Enter the car id: "))
    cur.execute("update drivers set No_of_wins int(20)=No_of_wins int(20)+1 where Car_id='{}'".format(cid,))

def adddriver():
     while True:
        #driverid=int(input("Enter the driver id:  "))
        drivername=input("Enter the driver name:  ")
        joinedon=obtaindate()
        dob=obtaindate()
        driverdist=int(input("Enter the total distance done by the driver:  "))
        drivertype=input("Enter the driver type:  ")
        driversalary=int(input("Enter the driver salary:  "))
        
        cur.execute("insert into driver (Driver_name,Joined_on,DOB,Total_km_raced,Driver_type,Driver_salary)values('{}','{}','{}','{}','{}','{}')".format(driverid,drivername,joinedon,dob,driverdist,drivertype,driversalary))
        cur.commit()
        print("Enter '1' to add more drivers.")
        print("Enter '2' to return to menu.")
        op=int(input("Enter your option:  "))
        if op==2:
            break

def displaydrivers():
    cur.execute("select * from drivers")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Driver_id','Driver_name','Joined_on','DOB','Total_km_raced','Driver_type','Driver_salary',sep="\t")
            print(i,sep="\t")


def removedrivers():
    d=input("Enter the driver ID to be removed:  ")
    cur.execute("delete from driverss where Driver_id='{}'".format(d,))
    cur.commit()

def adddist():
    did=int(input("Enter the driver id: "))
    d=int(input("Enter the distance last raced:  "))
    cur.execute("update drivers set Total_km_raced=Total_km_raced+'{}' where Driver_id='{}'".format(d,did))
    cur.commit()

def addwin():
    did=int(input("Enter the driver id: "))
    cur.execute("update drivers set No_of_wins int(20)=No_of_wins int(20)+1 where Driver_id='{}'".format(did,))

def searchdriver():
    d=input("Enter the name driver to be searched:  ")
    cur.execute("select * from drivers where Driver_name like '%'{}'' ".format(d,))
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Driver_id','Driver_name','Joined_on','DOB','Total_km_raced','Driver_type','Driver_salary',sep="\t")
            print(i,sep="\t")
   
def positions():
    cur.execute("select Event_name,Car_name,Driver_name,Event_position from drivers,events,cars where drivers.Driver_type=\
    events.Event_type=cars.Car_type order by Event_position ")
    for i in cur.fetchall():
        for j in i:
            print('Event_name','Car_name','Driver_name','Event_position',sep='\t')

            print(j,sep='\t')

def sort():
    cur.execute("select * from events order by Event_date")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type',sep="\t")
            print(i,sep='\t')
def financial():
    cur.execute("select Event_name,Car_name,Event_pricemoney,Event_expenses,Car_price,Driver_salary,\
        Event_pricemoney - (Event_expenses + Car_price + Driver_salary)'Return'from drivers,events,cars where drivers.Driver_type=\
    events.Event_type=cars.Car_type order by Event_pricemoney")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_name','Car_name','Event_pricemoney','Event_expenses','Car_price','Driver_salary','Return',sep="\t")
            print(i,sep='\t')
def upcomming():
    cur.execute("select * from events where Event_date>current_date()")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type',sep="\t")
            print(i,sep='\t')
def finished():
    cur.execute("select * from events where Event_date<current_date()")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_id''Event_name','Event_stage','Event_date','Total_distance','Event_type',sep="\t")
            print(i,sep='\t')
def auto():
    cur.execute("select Event_name,Car_name,Driver_name,Event_date from drivers,events,cars where drivers.Driver_type=\
    events.Event_type=cars.Car_type order by date ")
    r=cur.fetchall()
    for i in r:
        for j in i:
            print('Event_name','Car_name','Driver_name','Event_date',sep="\t")
            print(i,sep='\t')

cur.close()
conn.close()