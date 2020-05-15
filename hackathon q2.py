import time
import pandas as pd
df = pd.read_excel("COVID DATA IN US STATES.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
a = list(df['A'])
b = list(df['B'])
c = list(df['C']) 
print("List of countries affected by covid-19:\nCountry:Number of people(15-25):")
for i in range(10):
  print("%12s%d"%(a[i],b[i]))
print("\n\n")
time.sleep(2)
for i in range(10):
  for j in range(9):
    if b[j]<b[j+1]:
      x=b[j]
      b[j]=b[j+1]
      b[j+1]=x
      y=a[j]
      a[j]=a[j+1]
      a[j+1]=y
      z=c[j]
      c[j]=c[j+1]
      c[j+1]=z
    
print("Top 5 countries which comes under the age 15-25:\nCountry:Number of people:")
for i in range(5):
  print("%12s%d"%(a[i],b[i]))
print("\n\n")
time.sleep(2)
for i in range(10):
  for j in range(9):
    if c[j]<c[j+1]:
      x=b[j]
      b[j]=b[j+1]
      b[j+1]=x
      y=a[j]
      a[j]=a[j+1]
      a[j+1]=y
      z=c[j]
      c[j]=c[j+1]
      c[j+1]=z
print("Top 5 countries affected by covid-19:\nCountry:Number of cases:")
for i in range(5):
  print("%12s%d"%(a[i],c[i]))
print("\n\n")
time.sleep(1)
print("Pictograph of number of cases:(# = 3 cases)")
for i in range(5):
  t=int(c[i]/3)
  print("%12s:"%a[i],end="")
  for j in range(t):
    print("#",end="")
  print("")
