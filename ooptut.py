class Student():
	def __init__(self, name, class_, rollNo):
		self.name = name
		self.class_ = class_
		self.rollNo = rollNo

	def getAnwser(self, question):
		return 'I dont have time to answer you'

students = []
students.append(Student('Creation Duwal', 8, 2))

for student in students:
	print(student.name)
	print(student.getAnwser('this is a question'))
