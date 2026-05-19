class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.fam = last_name

    def print_name(self):
        return self.name
    
    def print_fam(self):
        return self.fam
    
    def print_namefam(self):
        return f"фамилия {self.fam}, имя {self.name}"
