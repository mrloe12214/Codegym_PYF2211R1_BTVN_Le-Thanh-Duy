import math

height = float(input("nhập chiều cao (m): cc= "))
weight = float(input("nhập cân nặng (kg): cn= "))
BMI = weight / (height*height)
print("Chiều cao =",height)
print("Cân nặng =",weight)
print("BMI =",BMI)
if BMI <16:
    print("Gầy độ III")
elif BMI >= 16 and BMI <17:
    print("Gầy độ II")
elif BMI >= 17 and BMI <18.5:
    print("Gầy độ I")
elif BMI >= 18.5 and BMI <25:
    print("Bình thường")
elif BMI >= 25 and BMI <30:
    print("Béo phì độ I")
elif BMI >= 35 and BMI <40:
    print("Béo phì độ II")
elif BMI >= 40:
    print("Béo phì độ III")
