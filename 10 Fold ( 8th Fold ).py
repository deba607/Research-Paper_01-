


print("8th fold")
import numpy

import pandas as pd
df = pd.read_excel(r'E:\college project\NEW Modified college project.xlsx')
#print(df)




y0 = df['death_yn']
y00 = y0.to_list()
#print(y00)

y000=0
l11=[]
for i in range(0,3640):
    l11.append(y00[i])
    
    
for i in range(4160,5200):
    l11.append(y00[i])
#print(l11)
#print("Zero count: ",l11[:4500].count(0)," One Count: ",l11[:4500].count(1)," Two Count: ",l11[:2600].count(2))

for i in range(0,4679):
    y000=y000+l11[i]
avg00=y000/len(l11)
print("Death Average: ",avg00)
D1 = numpy.std(l11)





x0 = df['sex']
x00 = x0.to_list()
#print(x00)

sum00=0
l12=[]
for i in range(0,3640):
    l12.append(x00[i])
    
for i in range(4160,5200):
    l12.append(x00[i])
    
for i in range(0,4679):    
    sum00=sum00+l12[i]
avg000=sum00/len(l12) 
#print("Sex Mean: ",avg000)  
l1=[]
for i in range(0,4679):
   a=l12[i]-avg000
   b=l11[i]-avg00
   #print(a,b)
   c=a*a
   d=a*b
   #print(c,d)
   a0=d/c
   l1.append(a0)
   #print(l1)
b1=sum(l1)/len(l1)
#print("Zero count: ",x00[:2600].count(0)," One Count: ",x00[:2600].count(1))
print("Sex-Death Relation: ",b1)





x1 = df['current_status']
x01 = x1.to_list()
# print(x01)
sum01=0
l13=[]
for i in range(0,3640):
    l13.append(x01[i])
    
for i in range(4160,5200):
    l13.append(x01[i])
    
for i in range(0,4679):    
    sum01=sum01+l13[i]
avg001=sum01/len(l13)
l2=[]    
for i in range(0,4679):
   
   a20=l13[i]-avg001
   b20=l11[i]-avg00
   c20=a20*a20
   d20=a20*b20
   a1=d20/c20
   l2.append(a1)
b2=sum(l2)/len(l2)
#print("Zero count: ",x01[:2600].count(0)," One Count: ",x01[:2600].count(1))
print("Death-Current: ",b2)


'''
x2 = df['Race and ethnicity (combined)']
x02 = x2.to_list()
#print(x02)
sum02=0
for i in range(1500):
    sum02=sum02+x02[i]
avg002=sum02/1500 
l3=[]   
for i in range(1500):
   
   a30=x02[i]-avg002
   b30=y00[i]-y000
   c30=a30*a30
   d30=a30*b30
   a2=d30/c30
   l3.append(a2)
b2=sum(l3)/1500

print("Race And Ethnicity: ",b2)



'''
x3 = df['hosp_yn']
x03 = x3.to_list()
#print(x03)
sum03=0
l14=[]
for i in range(0,3640):
    l14.append(x03[i])
    
for i in range(4160,5200):
    l14.append(x03[i])
    
for i in range(0,4679):    
    sum03=sum03+l14[i]
avg003=sum03/len(l14)
l4=[]    
for i in range(0,4679):
   
   a40=l14[i]-avg003
   b40=l11[i]-avg00
   c40=a40*a40
   d40=a40*b40
   a3=d40/c40
   l4.append(a3)
b3=sum(l4)/len(l4)
#print("Zero count: ",x03[:2600].count(0)," One Count: ",x03[:2600].count(1))
print("Death-Hospitalised Condition:", b3)




x4 = df['icu_yn']
x04 = x4.to_list()
#print(x04)
sum04=0
l15=[]
for i in range(0,3640):
    l15.append(x04[i])
    
for i in range(4160,5200):
    l15.append(x04[i])
    
for i in range(0,4679):    
    sum04=sum04+l15[i]
avg004=sum04/len(l15)
l5=[]
for i in range(0,4679):
   
   a50=l15[i]-avg004
   b50=l11[i]-avg00
   c50=a50*a50
   d50=a50*b50
   a4=d50/c50
   l5.append(a4)
b4=sum(l5)/len(l5)
#print("Zero count: ",x04[:2600].count(0)," One Count: ",x04[:2600].count(1))
print("Death-Icu Relation:", b4)





x5 = df['medcond_yn']
x05 = x5.to_list()
#print(x05)
sum05=0
l16=[]
for i in range(0,3640):
    l16.append(x05[i])
    
for i in range(4160,5200):
    l16.append(x05[i])
    
for i in range(0,4679):
    sum05=sum05+l16[i]
avg005=sum05/len(l16)
l6=[]    
for i in range(0,4679):
   
   a60=l16[i]-avg005
   b60=l11[i]-avg00
   c60=a60*a60
   d60=a60*b60
   a5=d60/c60
   l6.append(a5)
b5=sum(l6)/len(l6)
#print("Zero count: ",x05[:2600].count(0)," One Count: ",x05[:2600].count(1)," Two Count: ",x05[:2600].count(2))
print("Death-Medical condition:" ,b5)


b0=avg00-(b1*avg000+b2*avg001+b3*avg003+b4*avg004+b5*avg005)
print("b0=",b0)





e=2.718
count=0
l7=[]
l8=[]
tp=0
tn=0
fp=0
fn=0
for i in range(3640,4160):
    
    y=b0+b1*x00[i]+b2*x01[i]+b3*x03[i]+b4*x04[i]+b5*x05[i]
  
    #l7.append(y)
    if(y00[i]==0):
        tn=tn+1
    #print(y)
    #print(y,y00[i])
    
    
    y0f=1+pow(e,-y)
    yf=1/y0f
    #print(yf,y00[i])
    #l8.append(yf)
    #print(yf,y00[i])
    #c1=abs(yf-y00[i])
    if (yf>.5 and y00[i]==1):
        count=count+1
        tp=tp+1
    elif(yf>.5 and y00[i]==0):
        fp=fp+1
        '''elif(yf<.5 and y00[i]==0):
             tn=tn+1'''
    else:
        fn=fn+1        

print("Standerd Deviation: ",D1)        
accuracy=(count/520)*100
#print(l8)
print("The previous accuracy: ",accuracy)
print("TP= ",tp,"TN= ",tn,"FP= ",fp,"FN= ",fn)               

sensitivity=(tp/(tp+fn))*100
spec=(tn/(tn+fp))*100
Precision=(tp/(tp+fp))*100
Recall=(tp/(tp+fn))*100
F1_Score=((2*Recall*Precision)/(Recall+Precision))
print("Precision: ",Precision)
print("Recall: ",Recall)
print("F1_Score: ",F1_Score)
print("Sensitivity: ",sensitivity)
print("Specifecity: ",spec)
accuracygood=((tp+tn)/(tp+tn+fp+fn))*100
print("The new accuracy: ",accuracygood)

'''
print("For Death Column,")
print("Zero count: ",y00[2600:].count(0)," One Count: ",y00[2600:].count(1),"Two Count: ",y00[2600:].count(2))

'''




        
