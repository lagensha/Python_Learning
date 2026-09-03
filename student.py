mark1=float(input("Enter first mark: "))
mark2=float(input("Enter second mark: "))
mark3=float(input("Enter third mark: "))

total_marks=mark1+mark2+mark3

average_marks=total_marks/3

if average_marks>=75:
    print("Student qualifies for the Dean's List")
else:
    print("Student does not qualify for the Dean's List")
