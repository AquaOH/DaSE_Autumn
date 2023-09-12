import math

weight = input("请输入你的体重(kg): ")
weight = float(weight)
height = input("请输入你的身高(m): ")
height = float(height)
BMI = weight / math.pow(height, 2)
if BMI < 18.5:
    print("轻体重")
elif BMI >= 28:
    print("肥胖")
elif 24 <= BMI < 28:
    print("超重")
elif 18.5 <= BMI < 24:
    print("正常")
