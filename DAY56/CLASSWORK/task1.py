class Robot:
    def __init__(self):
        self.water_level = 0  

    def fill_water(self, amount):
        """დავსხათ წყალი რობოტის საცავში"""
        if amount > 0:
            self.water_level += amount
            print(f"წყალი დასხმულია: {amount} ლიტრი. არსებული დონე: {self.water_level} ლიტრი.")
        else:
            print("არასწორი რაოდენობა წყლის დასხმაში.")

    def fetch_water(self):
        """მოიტანს წყლის რაოდენობას და გააგზავნის პირნიშანს"""
        if self.water_level > 0:
            print(f"მოიტანე {self.water_level} ლიტრი წყალი.")
            self.water_level = 0  
        else:
            print("წყალი არ არის!")


my_robot = Robot()
my_robot.fill_water(5) 
my_robot.fetch_water()
my_robot.fetch_water()