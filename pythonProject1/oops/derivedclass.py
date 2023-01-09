class Person(object):
    def getGender(self):
        return "Unknown"
class Male(Person):
    def getGender(self):
        return "male"
class Female(Person):
    def getGender(self):
        return "female"

aMale=Male()
aFemale=Female()
print(aMale.getGender())
print(aFemale.getGender())

