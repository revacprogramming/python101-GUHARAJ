# Conditional Execution


score = input("Enter Score: ")
S = float(score)
X = 'error'
if S >= 0.9:
   X = 'A'
elif S >= 0.8:
      X = 'B'
elif S >= 0.7:
      X = 'C'
elif S >= 0.6:
      X = 'd'
elif S < 0.6:
       S = 'F'
else:
     X = "out of range"
print (X)