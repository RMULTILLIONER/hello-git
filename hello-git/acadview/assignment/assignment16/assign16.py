#Question 1
import mysql.connector
config = {
'user': 'admin',
'password': 'admin',
'host': 'localhost',
'port': '8080',
'database': 'db',
'raise_on_warnings': True}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

try:
    cursor = cnx.cursor()
    query6 = '''Create table Authors15(AuthorID int primary key,FirstName varchar(300),MiddleName varchar(300),LastName varchar(300))'''
    cursor.execute(query6)
    query4 = '''Create table Zip_Codes15(Zip_Code_ID int primary key,City varchar(300),State varchar(300),Zip_Code int)'''
    cursor.execute(query4)
    query3 = '''Create table Publishers15(Publisher_ID int primary key,Name varchar(300),Street_Address varchar(300),Suite_Number int,Zip_Code_ID int,foreign key(Zip_Code_ID) references Zip_Codes(Zip_Code_ID))'''
    cursor.execute(query3)
    query2 = '''Create table Titles15(TitleId int primary key,Title varchar(60),ISBN int,Publisher_ID int,Publication_Year int,foreign key(Publisher_ID) references Publishers(Publisher_ID))'''
    cursor.execute(query2)
    query1 = '''Create table Books15(BookId int primary key,TitleId int,Location varchar(300),Genre varchar(300),foreign key(TitleId) references Titles(TitleId))'''
    cursor.execute(query1)
    query5 = '''Create table Authors_Titles12(Author_Title_ID int primary key,AuthorID int ,TitleId int,foreign key(AuthorID) references Authors(AuthorID),foreign key(TitleId) references Titles(TitleId))'''
    cursor.execute(query5)
    print('TABLE MANUFACTURATION DONE')
except mysql.connector.DatabaseError as e:
    if cnx:
        cnx.rollback()
    print('OH! Problem occured. Please check: ', e)
finally:
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()





#Question 2
insert_into1 = '''INSERT INTO Authors15(AuthorID, FirstName, MiddleName, LastName) VALUES ();'''
insert_into2 = '''INSERT INTO Zip_Codes15(Zip_Code_ID, City, State, Zip_Code) VALUES ();'''
insert_into3 = '''INSERT INTO Publishers15(Publisher_ID, Street_Address, Suite_Number, Zip_Code_ID) VALUES ();'''
insert_into4 = '''INSERT INTO Titles15(TitleId, Title, ISBN, Publisher_ID , Publication_Year) VALUES ();'''

print('INSERT :         ',cursor.execute(insert_into1))
print('INSERT :         ',cursor.execute(insert_into2))
print('INSERT : 	',cursor.execute(insert_into3))
print('INSERT : 	',cursor.execute(insert_into4))
cnx.commit()
print(cursor.fetchall())


#Q3
update_query = '''UPDATE Authors15 SET AuthorID = '1080' where FirstName = VAB DECODA '''





