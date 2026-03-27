print("AI Health & Wellbeing Advisor")  
print("1. BMI & Diet Advisor") 
print("2. Symptom Checker")
Choice = input(" choose option(1/2): ")
# BMI Module
if Choice == "1":
  Weight= float(input("Enter your weight in kg: "))
  height= float(input("Enter your height in cm:"))
  height= height/100
  BMI= Weight/(height*height)
  print("Your BMI is:",round(BMI/2))
  if BMI < 18.5:
    print("Category : Underweight")
    print("Advise: Increase calorie intake and protien rich food")
  elif BMI < 25:
    print("Category : Normal")
    print("Advise: Maintain balanced diet and exercise")
  elif BMI < 30:
    print("Category : Overweight")
    print("Advise: Reduce sugar and fried food, exercise more")
  else:
    print("Category : Obese")
    print("Advise: Follw controlled diet and regular exercise")

#Symptom Checker
elif Choice=="2":
  fever= input("Do you have fever?(yes/no): ")
  cough= input("Do you have cough?(yes/no): ")
  headache=input("Do you have headache?(yes/no): ")
  if fever == "yes" and cough =="yes":
    print("Possible condition :Flu")
    print("Advise: Take rest and drink fluids")
  elif  fever =="yes" and headache =="yes":
    print("Possible condition : Viral infection")
    print("Advise: Take rest and stay hydrated")
  elif cough =="yes" :
    print("Possible condition : Cold") 
    print("Advise: Warm fluids and rest")
  else:
    print("Symptoms unclear. Please consult a doctor.")
else:
  print("Invalid choice")    

