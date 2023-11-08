class Player():
    def __init__(self, name="N/A", age="N/A", position="DH", prev_salary="- ", expected_salary="- ", team="N/A", hand=["R","R"]):
        self.name = name
        self.age = age
        self.position = position
        self.bats = hand[0]
        self.throws = hand[1]
        if expected_salary != '- ':
            self.salary = expected_salary
        else:
            self.salary = prev_salary
        self.team = team

    def general_position(self):
        if self.position in ["C", "1B", "2B", "3B", "SS"]:
            return "infielder"
        elif self.position in ["LF", "RF", "OF"]:
            return "outfielder"
        elif self.position == "SP":
            return "starting pitcher"
        elif self.position == "RP":
            return "relief pitcher"
        elif self.position == "DH":
            return "designated hitter"
        
    def is_signed(self):
        return self.team != "-"

    def __str__(self):
        if self.is_signed():
            return f"{self.name} is a {self.position} for the {self.team} with an AAV of {self.salary}."
        else:
            return f"{self.name} is a free agent {self.position} and is expected to have an AAV of {self.salary}"
        
