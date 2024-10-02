from doctor import Doctor

class Administrator():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def make_appointment(self, doctor : Doctor, day, time):
        if (doctor._have_free_time(day)):
            doctor._add_to_scedule(day, time)
            return "Successful appointent."
        else:
            return f"I can't make appointment that, {doctor.name} is busy on {day}."