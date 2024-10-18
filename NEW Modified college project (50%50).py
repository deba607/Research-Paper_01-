

print("50 % 50 split")


import pandas as pd
df = pd.read_excel(r'E:\college project\NEW Modified college project.xlsx')
#print(df)




y0 = df['death_yn']
y00 = y0.to_list()
#print(y00)

y000=0
for i in range(2600):
   if(i<2599):
       y000+=y00[i]
   else:
       y000+=y00[i]
       y000/=2600
print("Zero count: ",y00[:2600].count(0)," One Count: ",y00[:2600].count(1),"Two Count: ",y00[:2600].count(2))
print("Death Average: ",y000)





x0 = df['sex']
x00 = x0.to_list()
#print(x00)

sum00=0
for i in range(2600):
    sum00+=x00[i]
avg000=sum00/2600 
#print("Sex Mean: ",avg000)  
l1=[]
for i in range(2600):
   a=x00[i]-avg000
   b=y00[i]-y000
   #print(a,b)
   c=a*a
   d=a*b
   #print(c,d)
   a0=d/c
   l1.append(a0)
   #print(l1)
b1=sum(l1)/2600
print("Zero count: ",x00[:2600].count(0)," One Count: ",x00[:2600].count(1))
#print("Sex-Death Relation: ",b0)





x1 = df['current_status']
x01 = x1.to_list()
# print(x01)
sum01=0
for i in range(2600):
    sum01=sum01+x01[i]
avg001=sum01/2600
l2=[]    
for i in range(2600):
   
   a20=x01[i]-avg001
   b20=y00[i]-y000
   c20=a20*a20
   d20=a20*b20
   a1=d20/c20
   l2.append(a1)
b2=sum(l2)/2600
print("Zero count: ",x01[:2600].count(0)," One Count: ",x01[:2600].count(1))
print("Death-Current: ",b1)


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
for i in range(2600):
    sum03=sum03+x03[i]
avg003=sum03/2600
l4=[]    
for i in range(2600):
   
   a40=x03[i]-avg003
   b40=y00[i]-y000
   c40=a40*a40
   d40=a40*b40
   a3=d40/c40
   l4.append(a3)
b3=sum(l4)/2600
print("Zero count: ",x03[:2600].count(0)," One Count: ",x03[:2600].count(1))
print("Hospitalised Condition:", b3)




x4 = df['icu_yn']
x04 = x4.to_list()
#print(x04)
sum04=0
for i in range(2600):
    sum04=sum04+x04[i]
avg004=sum04/2600
l5=[]
for i in range(2600):
   
   a50=x04[i]-avg004
   b50=y00[i]-y000
   c50=a50*a50
   d50=a50*b50
   a4=d50/c50
   l5.append(a4)
b4=sum(l5)/2600
print("Zero count: ",x04[:2600].count(0)," One Count: ",x04[:2600].count(1))
print("Icu:", b4)





x5 = df['medcond_yn']
x05 = x5.to_list()
#print(x05)
sum05=0
for i in range(2600):
    sum05=sum05+x05[i]
avg005=sum05/2600
l6=[]    
for i in range(2600):
   
   a60=x05[i]-avg005
   b60=y00[i]-y000
   c60=a60*a60
   d60=a60*b60
   a5=d60/c60
   l6.append(a5)
b5=sum(l6)/2600
print("Zero count: ",x05[:2600].count(0)," One Count: ",x05[:2600].count(1)," Two Count: ",x05[:2600].count(2))
print("Medical condition:" ,b5)


b0=y000-(b1*avg000+b2*avg001+b3*avg003+b4*avg004+b5*avg005)
print(b0)





e=2.718
count=0
l7=[]
l8=[]
tp=0
tn=0
fp=0
fn=0
for i in range(2601,5200):
    
    y=b0+b1*x00[i]+b2*x01[i]+b3*x03[i]+b4*x04[i]+b5*x05[i]
  
    #l7.append(y)

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
    elif(yf<.5 and y00[i]==0):
        tn=tn+1
    else:
        fn=fn+1        
        
accuracy=(count/2600)*100
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


print("For Death Collum,")
print("Zero count: ",y00[2600:].count(0)," One Count: ",y00[2600:].count(1),"Two Count: ",y00[2600:].count(2))



'''
for i in range(2601,5200):
    
    print(y00[i])
'''





'''    
print("Zero count: ",y00[1501:3000].count(0)," One Count: ",y00[1501:3000].count(1))
  


l9=[]
for i in range(1501,3000):
    
    if l8[i]>0.5:
       k1=1
       l9.append(k1)
    else:
       k1=0
       l9.append(k1)

ly=[]
for i in range(1501,3000):
    ly.append(y00[i])
#print(ly)
    

#print(l9) 


for i in range(1499):
    if(ly[i]==l9[i]==1):
        tp=tp+1
    elif(ly[i]==l9[i]==0):
        tn=tn+1            
    elif(ly[i]==1,l9[i]==0):
        fp=fp+1
    elif(ly[i]==0,l9[i]==1):
        fn=fn+1 

  
    
    
  
    

        
'''