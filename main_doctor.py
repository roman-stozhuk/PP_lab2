from doctor import Doctor
from administrator import Administrator

class Main_doctor(Doctor, Administrator):
    def __init__(self, name, surname, specialization):
        super().__init__(name, surname, specialization)

    def get_doctors_info(self):
        return f"{str(super().get_doctors_info())[:-1]} and administrator at the same time."
  