# A class is like a blueprint for creating objects. 
# An object has properties and methods(functions) associated with it. 
# Almost everything in Python is an object

# this is how you extend class
class Points:

    def __init__(self, totalPoints):
        self.totalPoints = totalPoints
    
    def getTotalPoints(self, numberOfCourses):
        self.totalPoints = numberOfCourses * 2
        return self.totalPoints
        

class User(Points):
    # constructor
    def __init__(self, userName, email, isPaid, totalCoursesRegistered):
        self.userName = userName
        self.email = email
        self.paid = isPaid
        self.totalCoursesRegistered = totalCoursesRegistered

    def addUser(self):

        if self.paid:
            print(f'Added user {self.userName} and email is: {self.email}')
        else:
            print(f'Cannot add user {self.userName} until paid')

    def isRegistered(self):
        if self.paid:
            print(f'{self.userName} registered for course')
        else:
            print(f'{self.userName} not registered yet')

satya = User('Satya', 'personal4kartheek@gmail.com', True, 4)
achanta = User('achanta', 'achanta@gmail.com', True, 2)

satya.addUser()
satya.isRegistered()
print(f'Total Points for {satya.userName} are {satya.getTotalPoints(satya.totalCoursesRegistered)}')

achanta.addUser()
achanta.isRegistered()
print(f'Total Points for {achanta.userName} are {achanta.getTotalPoints(achanta.totalCoursesRegistered)}')
