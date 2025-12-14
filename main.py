import mysql.connector
import random as r
# connection
db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="admin",      
    database="MovieTicket"
)
cursor=db.cursor()

def user_login():
    cust_name = input("Enter your name: ")
    query = "select * from customer where name=%s"
    cursor.execute(query, [cust_name])
    result = cursor.fetchall()
    try:
        return result[0][0]
    except IndexError:
        print("USER DOESNT EXIST, PLEASE SIGNUP")
        
        
def user_signup():
    random_id = r.randint(1, 1000000)
    cust_name=input('enter your name : ')  
    query = "insert into customer values(%s, %s)"
    cursor.execute(query, [random_id, cust_name.lower()])
    db.commit()
    query = "select * from customer where name=%s"
    cursor.execute(query, [cust_name])
    result = cursor.fetchall()
    return result[0][0]
    print("USER SIGNED IN SUCCESSFULLY!! PLEASE CONTINUE: ID", random_id)

def view_movies():
    cursor.execute("SELECT * FROM movies")
    result = cursor.fetchall()
    print("available movies are : ")
    for i in result:
        print(i)


def view_shows():
    cursor.execute("SELECT * FROM shows")
    result = cursor.fetchall()
    print("available shows are : ")
    for i in result:
        print(i)


def view_booking():
    cursor.execute("SELECT * FROM booking")
    result = cursor.fetchall()
    if result==[]:
        print('no bookings yet')
    else:
        print("current bookings : ")
        for i in result:
            print(i)
            
def book_ticket(uId):
    random_id = r.randint(1, 1000000)
    mov_id = int(input("Enter movie id: "))
    t = input("Enter movie time: ")
    s_name = input("Enter screen name: ")
    seat_number = input("Enter seat number: ")
    query = "INSERT INTO BOOKING VALUES(%s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, [random_id, uId, mov_id, t, s_name, seat_number])
        print(f"TICKET BOOKED: {uId}: {mov_id}: {s_name}: {t}: {seat_number}")
    except mysql.connector.errors.ProgrammingError:
        print(f"{mysql.connector.errors.ProgrammingError}")
      
choice = int(input('Enter 1. Login 2. Signup : '))
if(choice == 1): 
    userID = user_login()
    while True:
        print('WELCOME TO THE MOVIE TICKET MANAGEMENT SYSTEM')
        print('HERE ARE SOME OPTIONS FOR YOU : ')
        print('1. MOVIES LIST')
        print('2. AVAILABLE SHOWS')
        print('3. BOOK YOUR TICKET')
        print('4. YOUR BOOKINGS')
        print('5. EXIT')

        choice=int(input('enter your choice : '))
        if choice==1:
            view_movies()
        elif choice==2:
            view_shows()
        elif choice==3:
            book_ticket(userID)
        elif choice==4:
            view_booking()
        elif choice==5:
            print('THANKYOU!!')
            break
elif(choice == 2): 
    userID = user_signup() 
    
    while True:
        print('WELCOME TO THE MOVIE TICKET MANAGEMENT SYSTEM')
        print('HERE ARE SOME OPTIONS FOR YOU : ')
        print('1. MOVIES LIST')
        print('2. AVAILABLE SHOWS')
        print('3. YOUR BOOKINGS')
        print('4. BOOK YOUR TICKET')
        print('5. EXIT')

        choice=int(input('enter your choice : '))
        if choice==1:
            view_movies()
        elif choice==2:
            view_shows()
        elif choice==3:
            view_booking()
        elif choice==4:
            book_ticket(userID)
        elif choice==5:
            print('THANKYOU!!')
            break
