import random
class Student(object):

  def __init__(self, name, number):
    self.name = name
    self.scores = []
    for count in range(number):
      self.scores.append(100)
      
  def getName(self):
    return self.name
    
  def setScore(self, i, score):
    self.scores[i - 1] = score
  def getScore(self, i):
      
    return self.scores[i - 1]
  def getAverage(self):
      
    return sum(self.scores) / len(self._scores)
  def getHighScore(self):
      
    return max(self.scores)
  def __str__(self):
    return "Name of Student: " + self.name + "\nScores: " + \
         " ".join(map(str, self.scores))
         
  def __lt__(self, other):
    return self.name < other.name
    
  def __ge__(self, other):
    return self.name >= other.name
    
  def __eq__(self, other):
    if self is other:
      return True
    elif type(self) != type(other):
      return False
    else:
      return self.name == other.name
def main():
  List = []
  for count in reversed(range(9)):
    s = Student("Student" + str(count + 1), 10)
    List.append(s)
  print("Sorted list of students:")
  random.shuffle(List)
  List.sort()
  for obj in List:
    print(obj.__str__())
if __name__ == "__main__":

  main()