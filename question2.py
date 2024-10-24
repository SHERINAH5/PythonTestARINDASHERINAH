# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

score = int(input(f"Enter student's score "))
if 90<= score <=100:
    print("Grade A")
elif 80<= score <=89:
    print("Grade B")
elif 70<= score <=79:
    print("Grade C")
elif 60<= score <=69:
    print("Grade D")
elif 40<= score <=50:
    print("Grade E")
else:
    print("Fail")
    

        














