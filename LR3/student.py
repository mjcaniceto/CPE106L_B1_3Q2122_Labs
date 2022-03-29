class Student(object):

  # Constructor
  def __init__(self, name, number):
    self.name = name
    self.scores = []
    for count in range(number):
      self.scores.append(0)

  # Get name
  def getName(self):
    return self.name

  # Set score
  def setScore(self, i, score):
    self.scores[i - 1] = score

  # Get score
  def getScore(self, i):
    return self.scores[i - 1]

  # Get average
  def getAverage(self):
    return sum(self.scores) / len(self._scores)

  # Get high score
  def getHighScore(self):
      return max(self.scores)

  # Print strings method
  def __str__(self):
    return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores)) + "\n"

  # Equality
  def __eq__(self,other):
    return self.name == other.name
   
  # Less than
  def __lt__(self,other):
    return self.name < other.name
 
  # Greater than or equal
  def __ge__(self,other):
    return self.name >= other.name
    

# Main
def main():
  # First student
  student = Student("Spongebob", 5)
  print(student)
  print("\nList populated..")
  for i in range(1, 6):
    student.setScore(i, 100)
  print(student)
  

  # Second student
  student2= Student("Patrick",5)
  print(student2)
  print("\nList populated..")
  for i in range(1, 6):
    student2.setScore(i, 100)
  print(student2)

  # Checking comparisons
  print("\nEquality Method: ")
  print(student==student2)

  print("\nLess than Method: ")
  print(student<student2)

  print("\nGreater than or Equal Method: ")
  print(student>=student2)

# Calling main
if __name__ == "__main__":

  main()
