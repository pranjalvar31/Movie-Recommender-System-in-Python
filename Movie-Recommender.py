
import tkinter as tk
  
root = tk.Tk() 
frame = tk.Frame(root) 
frame.pack() 

tk.Label(root, text="Movie Recommender").pack()
root.geometry("680x500")

import pandas as pd
pd.set_option('mode.chained_assignment', None)
dataset =pd.read_csv('IMDB-Movie-Data.csv')
impdataset=dataset.iloc[:,[1,2,6,8,10,11]]
impdataset['Action']=0
impdataset['Comedy']=0
impdataset['Sci-Fi']=0
impdataset['Adventure']=0
impdataset['Drama']=0
impdataset['Horror']=0
impdataset['Thriller']=0
impdataset['Animation']=0
impdataset['Romance']=0
impdataset['Fantasy']=0
impdataset['Family']=0
impdataset['History']=0
impdataset['Biography']=0
impdataset['Music']=0
impdataset['Mystery']=0
impdataset['Crime']=0
l='Action'
a='Comedy'
b='Sci-Fi'
c='Adventure'
d='Drama'
e='Horror'
f='Thriller'
g='Animation'
h='Romance'
i='Fantasy'
j='Family'
k='History'
m='Biography'
n='Music'
o='Mystery'
z='Crime'
index=0

while(index<1000):
    x=impdataset.loc[index].Genre.rfind(l)
    if(x!=-1):
        impdataset.loc[index,l]=impdataset.loc[index,l]+1
        
    x=impdataset.loc[index].Genre.rfind(a)
    if(x!=-1):
        impdataset.loc[index,a]=impdataset.loc[index,a]+1   
       
    x=impdataset.loc[index].Genre.rfind(b)
    if(x!=-1):
        impdataset.loc[index,b]=impdataset.loc[index,b]+1
       
    x=impdataset.loc[index].Genre.rfind(c)
    if(x!=-1):
        impdataset.loc[index,c]=impdataset.loc[index,c]+1   
       
    x=impdataset.loc[index].Genre.rfind(d)
    if(x!=-1):
        impdataset.loc[index,d]=impdataset.loc[index,d]+1
       
    x=impdataset.loc[index].Genre.rfind(e)
    if(x!=-1):
        impdataset.loc[index,e]=impdataset.loc[index,e]+1   
       
    x=impdataset.loc[index].Genre.rfind(f)
    if(x!=-1):
        impdataset.loc[index,f]=impdataset.loc[index,f]+1
       
    x=impdataset.loc[index].Genre.rfind(g)
    if(x!=-1):
        impdataset.loc[index,g]=impdataset.loc[index,g]+1 
       
    x=impdataset.loc[index].Genre.rfind(h)
    if(x!=-1):
        impdataset.loc[index,h]=impdataset.loc[index,h]+1
        
    x=impdataset.loc[index].Genre.rfind(i)
    if(x!=-1):
        impdataset.loc[index,i]=impdataset.loc[index,i]+1  
     
    x=impdataset.loc[index].Genre.rfind(j)
    if(x!=-1):
        impdataset.loc[index,j]=impdataset.loc[index,j]+1
     
    x=impdataset.loc[index].Genre.rfind(k)
    if(x!=-1):
        impdataset.loc[index,k]=impdataset.loc[index,k]+1 
     
    x=impdataset.loc[index].Genre.rfind(m)
    if(x!=-1):
        impdataset.loc[index,m]=impdataset.loc[index,m]+1
      
    x=impdataset.loc[index].Genre.rfind(n)
    if(x!=-1):
        impdataset.loc[index,n]=impdataset.loc[index,n]+1   
        
    x=impdataset.loc[index].Genre.rfind(o)
    if(x!=-1):
        impdataset.loc[index,o]=impdataset.loc[index,o]+1
    
    x=impdataset.loc[index].Genre.rfind(z)
    if(x!=-1):
        impdataset.loc[index,z]=impdataset.loc[index,z]+1  
    index=index+1
impdataset2=impdataset  
j=0
labels=[]
while(j<1000):  
  labels.append(j)
  j=j+1  
def sortt(byy):
  global impdataset
  global impdataset2
  global u
  global v
  impdataset.sort_values( by=byy, axis=0, ascending=True, inplace=True, kind='quicksort', na_position='last') 
  impdataset2.sort_values( by=byy, axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')    
  u=impdataset.reset_index(level=None)["index"]        
  v=impdataset2.reset_index(level=None)["index"]  
sortt("Rating")
i=0
Lb = tk.Listbox(root,selectmode='multiple',width="600",height="450") 
while(i<1000):
  Lb.insert(i+1,impdataset.loc[u[i]].values[0]) 
  i=i+1
pp=[]  
def func():
   global pp 
   global Lb
   global b
   pp=Lb.curselection()
   global traindata
   traindata2=impdataset.iloc[[i for i in pp],:]
   traindata2['ratingbyme']=[1 for i in pp]
   traindata=traindata.append(traindata2,sort=False)
   i=0
   Lb.delete(0,999)
   while(i<1000):
     Lb.insert(i+1,impdataset2.loc[v[999-i]].values[0]) 
     i=i+1
   b.configure( text="Select the movie you hate", command=func2)
   print(pp)
   print(traindata)
   

def func2():
   global pp
   global b
   pp=Lb.curselection()
   global traindata
   traindata2=impdataset2.iloc[[999-i for i in pp],:]
   traindata2['ratingbyme']=[-1 for i in pp] 
   traindata=traindata.append(traindata2,sort=False)
   b.configure( text="Ad3", command=myfun)
   print(traindata2)
   myfun()
      
 
b = tk.Button(root, text="Select the movie you like", command=func)

b.pack(side='top')
Lb.pack(side='top',)  

traindata=impdataset.iloc[[i for i in pp],:] 
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(18, input_dim=16,kernel_initializer='normal',activation='tanh'))
model.add(Dense(12,kernel_initializer='normal',activation='tanh'))
model.add(Dense(8,kernel_initializer='normal',activation='tanh'))
model.add(Dense(1,kernel_initializer='normal',activation='tanh'))
def myfun(): 
  global b
  global impdataset
  global impdataset2  
  global traindata
  X=traindata.iloc[:,6:22].values
  y=traindata.iloc[:,22].values
  print(X)
  print("jnjn")  
  model.compile(loss='mean_absolute_error', optimizer='adam',metrics=['accuracy'])
# fit the keras model on the dataset
  model.fit(X, y, epochs=1500, batch_size=10, verbose=0)
# make class predictions with the model
  predictions = model.predict_classes(impdataset.iloc[:,6:22])      
  impdataset['ratingbyme']=predictions
  index=0
  while(index<1000):
    metascore=impdataset.loc[index,'Metascore']
    sc=((20*impdataset.loc[index,'Rating'])+metascore)
    impdataset.loc[index,'finalscore']=impdataset.loc[index,'ratingbyme']*sc
    index=index+1
  i=0  
  Lb.delete(0,999)
  impdataset2=impdataset
  sortt("finalscore")
  while(i<1000):
    Lb.insert(i+1,impdataset.loc[u[i]].values[0]) 
    i=i+1
  b.configure( text="Recommended Movies, Proceed until you find a good one", command=func)
  
 
      
   
root.mainloop()  
