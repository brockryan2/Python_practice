# trying_out_classes


from pprint import pprint as pp

class Flight:
  def __init__(self, number, aircraft):
    if not number[:2].isalpha():
      raise ValueError("No airline code in '{}'".format(number))

    if not number[:2].isupper():
      raise ValueError("Invalid airline code '{}'".format(number))

    if not (number[2:].isdigit() and int(number[2:]) <= 9999):
      raise ValueError("Invalid route number '{}'".format(number))

    self._number = number
    self._aircraft = aircraft

    rows, seats = self._aircraft.seating_plan()
    self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

  def number(self):
    return self._number

  def airline(self):
    return self._number[:2]

  def aircraft_model(self):
    return self._aircraft.model()



class Aircraft:

  def __init__(self, registration):
    self._registration = registration

  def registration(self):
    return self._registration

  def num_seats(self):
    rows, row_seats = self.seating_plan()
    return len(rows) * len(row_seats)


class AirbusA319(Aircraft):


  def model(self):
    return "Airbus A319"

  def seating_plan(self):
    return range(1, 23), "ABCDEF"



class Boeing777(Aircraft):

  def model(self):
    return "Boeing 777"

  def seating_plan(self):
    return range(1, 56), "ABCDEFGHJK"


a1 = AirbusA319("A-IFHS")
a2 = Boeing777("B-UGVA")

pp(a1.model())
pp(a1.seating_plan())
pp(a1.num_seats())

pp(a2.model())
pp(a2.seating_plan())
pp(a2.num_seats())

f1 = Flight("AB1234", a1)
f2 = Flight("BG9876", a2)

#pp(f1._number)
pp(f1.airline())
#pp(aircraft_model(f1))
