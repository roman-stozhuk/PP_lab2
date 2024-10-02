class Doctor():
    __number_of_doctors = 0

    def __init__(self, name, surname, specialization):
        self.name = name
        self.surname = surname
        self.specialization = specialization
        self.__scedule = dict()
        Doctor.__number_of_doctors += 1

    def get_doctors_info(self):
        return f"I am {self.name} {self.surname} and work here as {self.specialization}."

    def _have_free_time(self, day):
        return (self.__scedule.get(day, 0) == 0)
    
    def ask_for_appointment(self, day):
        if (self._have_free_time(day)):
            return f"I am free on {day}."
        else:
            return f"I am busy on {day}."
        
    def _add_to_scedule(self, day, time):
        self.__scedule[day] = time 

    @staticmethod
    def get_number_of_doctors():
        if(Doctor.__number_of_doctors == 0):
            return F"There are no doctors."
        elif(Doctor.__number_of_doctors == 1):
            return "There is 1 doctor."
        else:
            return F"There are {Doctor.__number_of_doctors} doctors."