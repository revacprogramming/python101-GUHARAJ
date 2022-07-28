 w=int(input("Enter 1 for Gross Pay\nEnter 2 for Grade \n"))
if(w==1):
  
  hrs = input("Enter Hours:")
  hrs=float(hrs)
  rate=input("Enter Rate:")
  rate=float(rate)
  if hrs<=40 and hrs>=0:
      gpay=hrs*rate
  if hrs>40:
      hrs1=hrs-40
      rate1=1.5*rate
      gpay1=hrs1*rate1
      gpay=40*rate+gpay1
  else:
    print("Enter Valid Hours.")
  print(gpay)