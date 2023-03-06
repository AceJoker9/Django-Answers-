# The First problem was the toughest by far, coding the "DESC" is still the biggest hurdle to jump
#This is what I got for problem number 1 

Grade_point_average = Students.objects.filter(Student.Gpa)
for g in Grade_point_average:
 if Grade_point_average >= 3.0:
   print(f' {Student.Firstname}, {Student.Lastname}, {Student.Gpa}')





# Problem #2

 x = Instructor.objects.filter(Instructor.hire_date) 
  for y in x:
    if x <= '2010-01-01':
      print (f'Full Name: {Instructor.first_name} {Instructor.last_name} Hire Date: {Instructor.hire_date}')





#Problem #3
teacher = Instructor.object.get(pk=2)
  shared_course = Course.objects.filter(Course.instructor(pk=2))
  print(
              f' Instructor Name: {teacher}, Courses: {shared_course}')
  
 


#Problem #4

kids = Student.objects.count
  classes = Course.objects.count
  professors = Instructor.objects.count

  print
  ("Student Count: {kids}, Courses Count: {classes}, Instructors Count: {professors}")

#This is was a little tricky, cause the variables, dont light up showing that they belong to anything on the Django Python file. 






#problem #5 

new_student = Student.objects.create(Student.first_name("Cornelius"),Student.last_name("Phillips"), Student.year("2023", Student.gpa("4.0")) )








#Problem #6 

fredos = Student.objects.get(pk=11).update(Student.gpa("4.2"))
    cheetos = Student.objects.get(pk=11)
    print(cheetos)






#Problem #7 

Bread = Student.objects.get(pk=11) .delete