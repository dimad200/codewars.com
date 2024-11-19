# Python is now supported on Codewars!
#
# For those of us who are not very familiar with Python,
# let's handle the very basic challenge of creating a class named Python.
# We want to give our Pythons a name, so it should take a name argument that we
# can retrieve later.
#
# For example:
#
# bubba = Python('Bubba')
# bubba.name # should return 'Bubba'
# Fundamentals
class Python:
    def __init__(self, tarakan, massa=100):
    # def (self, tarakan, massa=100):
        self.name = tarakan
        self.massa= massa

bubba = Python('Bubba',)
print(bubba.name)
print(bubba.massa)
