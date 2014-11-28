"""
===========================
 Project: hong-rean
    Part: Program Structure
Language: Python 2.7.8
 Created: 28 November, 2014
===========================
"""
class Students(object):
    """add description"""
    def __init__(self, firstname, lastname, number, grade):
        """variables for receive information"""
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.grade = grade
    def get_information(self):
        """..."""
        data = list()
        data.append(self.firstname)
        data.append(self.lastname)
        data.append(self.number)
        data.append(self.grade)
        return data
def main():
    """For use in testcase only
    The actual will be use in app.ui branches"""
    data = list()
    for _ in xrange(input()):
        data.append(Students(raw_input(), raw_input(), input(), raw_input()).get_information())
    return data
print main()
