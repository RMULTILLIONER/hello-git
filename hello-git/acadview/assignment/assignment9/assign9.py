#Q1
print("\n\n Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.")

class Circle():   
    def __init__(self,radius):
        self.radius = radius
        
    def  getArea(self):
        print("Area is : " + str(3.14*self.radius*self.radius))

    def getCircumference(self):
        print("Circumference is : " + str(self.radius*2*3.14))
A = Circle(float(input("Enter radius : ")))
A.getArea()
A.getCircumference()


#Q2
print("\n\n Q.2- Create a Student class and initialize it with name and roll number. Make methods to : \n 1. Display - It should display all informations of the student.")

class Student():  
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll

    def Display(self):
        print(self.name)
        print(self.roll)        
A = Student(input("Enter name of student : "), input("Enter his/her roll no : "))
A.Display()


#Q3
print("\n\n Q.3- Create a Temprature class. Make two methods : \n1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.\n2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.")

class Temperature():

    def  convertFahrenhiet(self,celsius):
        print("Temperature in Fahrenhiet is : " + str((celsius*(9/5))+32))
        
    def convertCelsius(self,farenhiet):
        print("Temperature in Celsius is : " + str((farenhiet-32)*(5/9)))

A = Temperature()
A.convertFahrenhiet(int(input("Enter temperature in Celcius : ")))
A.convertCelsius(int(input("Enter temperature in Fahrenhiet : ")))


#Q4
print("\n\n Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .\n Make methods to\n1. Display-Display the details.\n2. Update- Update the movie details")

class MovieDetails():
    def __init__(self):
        self.moviename = input("Movie Name : ")
        self.artistname = input("Artist Name : ")
        self.year = int(input("Year : "))
        self.ratings = int(input("Ratings out of 10 : "))
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.year)
        print(self.ratings)
a = MovieDetails()
a.display()
x = input("Do you want to update the details. Yes or No.")
if x == "Yes":
    Update = MovieDetails()
    print(Update.display())
else:
     pass


#Q5
print("\n\n Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.\n1. Display expenditure and savings\n2. Calculate total salary\n3. Display salary ")

class expend:
         def __init__(self):
                    self.ex = int(input("enter total expenditure"))
                    self.sav = int(input("enter total savings"))
         def display(self):
                    print("expenditure is: ")
                    print(self.ex)
                    print("savings are: ")
                    print(self.sav)
         def total(self):
                    self.total = self.ex + self.sav
                    print('total salary is ')
                    print(self.total)
e1 = expend()
e1.display()
e1.total()
