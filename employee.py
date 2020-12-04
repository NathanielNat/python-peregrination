class Employee:
    """employee details class """
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.salary_raise = 500

    def give_raise(self,custom_raise=''):
        if custom_raise:
            self.salary += custom_raise
            
        else:
            self.salary += self.salary_raise
        print(self.salary)