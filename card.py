class Card:
  def __init__(self,i):
    self.val=i

  def get_val(self):
    return self.val

def test_card(i):
  c=Card(i)
  v=c.get_val()
  print v

if __name__ == "__main__":
  test_card(4)
