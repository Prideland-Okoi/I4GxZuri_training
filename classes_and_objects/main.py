class Student:

    # The init method or constructor
    def __init__(self, name, age, tracks, score):
        # Instance Variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

# Adds an instance variable
    def change_name(self, change_name):
        self.name = change_name
        print("Updated Information: My name is " + change_name)

    def change_age(self, change_age):
        self.age = change_age
        print("Updated Information: My age is ", change_age)

    def add_track(self, change_track):
        self.tracks = change_track
        print("Updated information: I am a student of track ", change_track)

# Retrieves instance variable
    def get_score(self):
        print("Information of Bob passed to Peter", self.score)
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Driver Code
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

