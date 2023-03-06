# The First problem was the toughest by far, coding the "DESC" is still the biggest hurdle to jump
#This is what I got for problem number 1 

 x = Instructor.objects.filter(Instructor.hire_date) 
  for y in x:
    if x <= '2010-01-01':
      print (f'Full Name: {Instructor.first_name} {Instructor.last_name} Hire Date: {Instructor.hire_date}')



# Problem #2

teacher = Instructor.object.get(pk=2)
  shared_course = Course.objects.filter(Course.instructor(pk=2))
  print(
              f' Instructor Name: {teacher}, Courses: {shared_course}')


#Problem #3

  kids = Student.objects.count
  classes = Course.objects.count
  professors = Instructor.objects.count

  print
  ("Student Count: {kids}, Courses Count: {classes}, Instructors Count: {professors}")

#This is was a little tricky, cause the variables, dont light up showing that they belong to anything on the Django Python file. 


#Problem #4

