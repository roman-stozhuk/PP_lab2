from doctor import Doctor

class Surgeon(Doctor):
    def __init__(self, name, surname, specialization):
        super().__init__(name, surname, specialization)

    def get_doctors_info(self):
        return f"{str(super().get_doctors_info())[:-1]} and surgeon at the same time."

    def perform_surgery(self, body_part):
        return f"I am performing {body_part} surgery right now."