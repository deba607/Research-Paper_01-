
print("Mean And Standard Deviation Of All Independent Fields")

import numpy

import pandas as pd
df = pd.read_excel(r'E:\college project\NEW Modified college project.xlsx')


y0 = df['death_yn']
y00 = y0.to_list()
#print(y00)

y000=0
for i in range(0,5200):
    y000=y000+y00[i]
avg_y000=y000/len(y00)
print("Death Mean: ",avg_y000)
D1 = numpy.std(y00)
print("Standard Deviation: ",D1)



x0 = df['sex']
x00 = x0.to_list()
#print(x00)
sum00=0
for i in range(0,5200):
    sum00=sum00+x00[i]
avg000=sum00/len(x00) 
print("Sex Mean: ",avg000) 
D2 = numpy.std(x00)
print("Standard Deviation: ",D2)


x1 = df['current_status']
x01 = x1.to_list()
# print(x01)
sum01=0
for i in range(0,5200):
    sum01=sum01+x01[i]
avg001=sum01/len(x01)
print("Current Status Mean: ",avg001)
D3 = numpy.std(x01)
print("Standard Deviation: ",D3)


x3 = df['hosp_yn']
x03 = x3.to_list()
#print(x03)
sum03=0
for i in range(0,5200):
    sum03=sum03+x03[i]
avg003=sum03/len(x03)
print("Hospitalised Condition Mean: ",avg003)
D4 = numpy.std(x03)
print("Standard Deviation: ",D4)


x4 = df['icu_yn']
x04 = x4.to_list()
#print(x04)
sum04=0
for i in range(0,5200):
    sum04=sum04+x04[i]
avg004=sum04/len(x04)
print("ICU Condition Mean: ",avg004)
D5 = numpy.std(x04)
print("Standard Deviation: ",D5)



x5 = df['medcond_yn']
x05 = x5.to_list()
#print(x05)
sum05=0
for i in range(0,5200):
    sum05=sum05+x05[i]
avg005=sum05/len(x05)
print("Medical Condition Mean: ",avg005)
D6 = numpy.std(x05)
print("Standard Deviation: ",D6)