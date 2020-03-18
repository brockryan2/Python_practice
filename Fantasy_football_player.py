# Python Project - Fantasy Football

from datetime import datetime


class Player(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.status = "Active"
        self.pass_yards = 0
        self.pass_td = 0
        self.rush_yards = 0
        self.rush_td = 0
        self.rec_yards = 0
        self.rec_td = 0
        self.num_recs = 0
        self.int = 0
        self.fumbles = 0
        self.points = 0

    def __str__(self):
        text = str(self.name)
        text += "\nPosition: " + str(self.position)
        text += "\nStatus: " + str(self.status)

        return text

    def get_stats(self):
        stats = [str(self.yards), str(self.touchdowns)]
        stats.append(str(self.points))
        label = ["Passing yards: ", "\nTD: ", "\nPoints: "]
        text = label[0] + stats[0] + label[1] + stats[1] + label[2] + stats[2]

        return text

    def add_yards(self, yards):
        try:
            assert type(yards) == int or type(yards) == float

            self.yards += yards
            self.points += 0.04 * yards

        except AssertionError as error:
            print("Error!  You did not provide valid input.")
            print("\nPlease input a number between -100 and 100")
            print("number can be either an integer or a decimal")
            print(error)

            f = open("C:\\Users\\bryan\\Desktop\\error_msg.txt", 'a+')
            f.write("Assertion error raised at " + str(datetime.now()) + ".")
            f.write("\nUser input was: " + str(yards))
            f.write("\nInput type: " + str(type(yards)))
            f.close()

    def touchdown(self):
        self.touchdowns += 1
        self.points += 6

    def update_status(self, update):
        self.status = update

    def update_yards(self, yards):
        self.yards = yards
        self.points = 0.04 * self.yards + (self.touchdowns * 6)

    def calculate_points(self):
        return 0.04 * self.yards + (self.touchdowns * 6)


aaron_rodgers = Player("Aaron Rodgers", "QB")
derrick_henry = Player("Derrick_Henry", "RB")
