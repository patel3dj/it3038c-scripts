This is the project for calculating grades for students, it is very helpful to check there grade and average, # opening file which contains grades.

" my project has a textfile linked to it so to run the code you will need to download the textfile"course_marks.txt" after downloading that you will be able to run the code and a new file will be generated which will be called course grades."
just keep following all the steps as per the comments and you will be guided to the destination smoothly.
file = open("course_marks.txt", 'r')
# opening file to write grades
fileout = open("CourseGrade.txt", 'w')
# writing header of file
fileout.write("{}  {}   {}\n".format("ID", "AVG", "GRADE"))
content = file.readline()
std_count = 0
a_grade = 0
b_grade = 0
c_grade = 0
d_grade = 0
f_grade = 0
lowest_avg = 100
high_avg = 0

while True:
    content = file.readline()
    # exiting if no content found
    if not content:
        break
    # processing file to calculate avg , grade, highest avg etc.
    values = content.split()
    avg = round((float(values[1])*0.15) + (float(values[2])*0.20) + (float(values[3])*0.25) + (float(values[4])*0.20) + (float(values[5])*0.20))
    std_count += 1
    if lowest_avg > avg:
        lowest_avg = avg
    if high_avg < avg:
        high_avg = avg
    if avg >= 90:
        grade = 'A'
        a_grade += 1
    elif avg >= 80:
        grade = 'B'
        b_grade += 1
    elif avg >= 70:
        grade = 'C'
        c_grade += 1
    elif avg >= 60:
        grade = 'D'
        d_grade += 1
    else:
        grade = 'F'
        f_grade += 1
    # writing result in file
    fileout.write("{}    {}    {}\n".format(values[0], avg, grade))
# displaying statistics of result
print("total number of students :- ", std_count)
print("number of students got A grade:- ", a_grade)
print("number of students got B grade:- ", b_grade)
print("number of students got C grade:- ", c_grade)
print("number of students got D grade:- ", d_grade)
print("number of students got F grade:- ", a_grade)
print("average of students got A grade:- ", (std_count/a_grade))
print("average of students got B grade:- ", (std_count/b_grade))
print("average of students got C grade:- ", (std_count/c_grade))
print("average of students got D grade:- ", (std_count/d_grade))
print("average of students got F grade:- ", (std_count/f_grade))
print("lowest average marks of student :- ", lowest_avg)
print("highest average marks of students :- ", high_avg)
# closing file
file.close()
fileout.close()
