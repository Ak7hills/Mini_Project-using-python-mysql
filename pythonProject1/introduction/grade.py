marks = int(input("enter the marks of the student :"))
if marks>=80:
    print("you have got an A grade ")
elif marks<80 and marks>=60:
    print("you have got B grade")
elif marks<60 and marks>=50:
    print("you have got C grade")
elif marks<50 and marks>=45:
    print("you have got D grade")
elif marks<45 and marks>=25:
    print("you have got E grade")
else:
    print("you have failed the exam")