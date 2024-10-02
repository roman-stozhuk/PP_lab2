from administrator import Administrator
from doctor import Doctor
from main_doctor import Main_doctor
from surgeon import Surgeon

def main():
    Bob = Doctor("Bob", "Lewis", "cardiologist")
    John = Doctor("John", "Miller", "neurologist")
    Emma = Surgeon("Emma", "Johnson", "oncologist")
    Michael = Administrator("Michael", "Thompson")
    David = Main_doctor("David", "Clark", "neurologist")


    print(Bob.get_doctors_info())
    print(John.get_doctors_info())
    print(John.ask_for_appointment("Monday"))
    print(Emma.perform_surgery("brain"))
    print(Emma.get_doctors_info())
    print(Michael.make_appointment(John, "Monday", "10 AM"))
    print(John.ask_for_appointment("Monday"))
    print(David.make_appointment(John, "Monday", "10 AM"))  
    print(David.get_doctors_info())


main()