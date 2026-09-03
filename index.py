Data=float(input("Enter used GB: "))

Used_Data = Data-120.000

if Used_Data<=15.000:
     print("Low data balance recharge your data balance")
     
else:
      print("Your data balance is:", Used_Data,"GB")