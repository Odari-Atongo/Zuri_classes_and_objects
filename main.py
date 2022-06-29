class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = str(track)
        self.score = float(score)

    def change_name(self, new_name):
        self.name=str(new_name)
        print(f"changed name to  {new_name}")

    def change_age(self, new_age):
        self.name=int(new_age)
        print(f"Changed age to {new_age}")

    def add_track(self, new_track):
        self.track=str(new_track)
        print(f"Changed track to {new_track}")

    def get_score(self, new_score):
        self.track=float(new_score)
        print(f"Changed score to {new_score}")


Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score(4.7))
