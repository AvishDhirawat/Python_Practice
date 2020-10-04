#Author - Avish Dhirawat
def bmi_calc(name,weight,height):
    bmi=weight/(height**2)
    print ("BMI : ")
    print (bmi)
    if bmi<25:
        print (name + " is Under Weighed")
    elif bmi>25:
        print (name + " is Overweighed")
    else :
        print (name + " is Equally Weighed")
a = input("Enter Name : ")
b = input("Enter Weight in KG : ")
c = input("Enter Height in M : ")
bmi_calc(a,b,c)