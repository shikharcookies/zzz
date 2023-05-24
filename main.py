import datetime


class Person :
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        
        self.address=address
        self.telephone=telephone
        self.email=email
        
    def age(self):
        today=datetime.date.today()
        age=today.year - self.birthdate.year
    
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -=1
        return age
person = Person(
  "Virat",
  "Kohli",
  datetime.date(1988,11,5),
  "Gurgaon, NCR, Uttar Pradesh",
  "123 456 7890",
  "virat.kohli@gmail.com"
)
print(person.name, person.surname)
print(person.age())
print(person.email)