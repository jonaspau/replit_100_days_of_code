class job:
    name = None
    salary = None
    hours = None

    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours

    def printJob(self):
        print(f"{self.name}\n{self.salary}\n{self.hours}\n")


class doctor(job):
    def __init__(self, salary, hours, experience, speciality):
        self.name = "Doctor"
        self.salary = salary
        self.hours = hours
        self.experience = experience
        self.speciality = speciality

    def printJob(self):
        print(
            f"{self.name}\n{self.salary}\n{self.hours}\n{self.speciality}\n{self.experience}\n"
        )


class teacher(job):
    def __init__(self, salary, hours, subject, position):
        self.name = "Teacher"
        self.salary = salary
        self.hours = hours
        self.subject = subject
        self.position = position

    def printJob(self):
        print(
            f"{self.name}\n{self.salary}\n{self.hours}\n{self.subject}\n{self.position}\n"
        )


teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
lawyer = job("Lawyer", "$100,000", "40")


teach.printJob()
doc.printJob()
lawyer.printJob()
