class Jug:
  def __init__(self, capacity, fill = 0):
    self.capacity = capacity
    self.fill = min(fill, capacity)

  def pourInto(self, jug):
    transfer = min(self.fill, jug.capacity - jug.fill)
    self.fill -= transfer
    jug.fill += transfer

jugs = [Jug(8, 8), Jug(5), Jug(3)]
turn = 0

while(jugs[0].fill != 4 or jugs[1].fill != 4):
  print(turn, f"0:({jugs[0].fill}/8) 1:({jugs[1].fill}/5) 2:({jugs[2].fill}/3)")
  spill = int(input("spill from jug:"))
  into = int(input("into jug:"))
  jugs[spill].pourInto(jugs[into])
  turn += 1
print(f"Congrats you solved it in {turn} moves!")
