class Student:
  def_int_(self,name,roll_numbee,cgpa):
  self.name = name 
  self.roll_number = roll_number
  self.cgpa=cgpa

def sort_students(student_list):
sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
 return sorted_students 