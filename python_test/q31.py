class Person:
    def __init__(self,name,age,gender):
        self._name=name
        self._age=age
        self._gender=gender
    def set_name(self,name):
        self._name=name
    def set_age(self,age):
        self._age=age
    def set_gender(self,gender):
        self._gender=gender
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_gender(self):
        return self._gender
person_object = Person(name="John", age=25, gender="Male")
print(person_object.get_name()," ",person_object.get_age()," ",person_object.get_gender())