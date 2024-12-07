#!/usr/bin/env python
# coding: utf-8

# In[3]:


pwd


# In[11]:


file_object = open('Me.txt',mode='r')
print(file_object)
file_object.close()
# File same folder ma j hoy


# In[13]:


file_object = open('abc.txt',mode='r')
print(file_object)
file_object.close()
# folder change hoy


# In[18]:


file_object = open('D:\\B3\\abc.txt',mode='r')
print(file_object)
file_object.close()
# folder change hoy tyare path aapvo pade file found karva


# In[25]:


f=open('Me.txt','r')
x=f.read()
print(x)
y=f.read()
print(">",y)
f.write("Hello")
f.close()


# In[32]:


f=open('Me.txt','r+')
x=f.read()
print(x)
f.write("Vishal10")
y=f.read()
print(y)
f.close()


# In[43]:


f=open('Me.txt','r+')
f.write("Parth")
f.close()


# In[47]:


f=open('Me.txt','w')
f.write("All Clear")
f.close()
# mode=W karo tyare file aakhi clear thai jay che pasi je write karo e j aave.


# In[49]:


f=open('Me.txt','w')
f.write("All Clear")
f.read()
f.close()


# In[67]:


f=open('Me.txt','w+')
x=f.read()
print(x)
f.write("Parth")
f.close()


# In[69]:


f=open('pqr.txt','w+')
# Jo name na male file nu to new file auto-create thai jay.


# In[76]:


f=open('Me.txt','a')
f.write(" Patel is Best.")
f.close()


# In[77]:


f=open('Me.txt','a')
f.write(" Patel is Best.")
f.read()
f.close()


# In[83]:


f=open('pqr.txt','a')
print(f.name)
print(f.mode)
print(f.closed)
print(f.readable())
print(f.writable())
f.close()
print(f.closed)


# In[94]:


f=open('Me.txt','w')
f.write("Hello")
f.writelines(['\nA\n','B\n','C'])
f.close()


# In[98]:


f=open('Ex.txt','r')
print(f.read())
f.close()


# In[120]:


f=open('Ex.txt','r')
print(f.read(2))
print(f.read(5))
print(f.read())
f.close()
# ahi () je lakhso e byte ma read karse means character ma read karse.
# line puri thay pasi last ma \n aave te-ne 1-byte ni jem Levano. (  \n = 1-ch  )
# niche ni line ma read karva jase.


# In[119]:


f=open('Ex.txt','r')
print(f.readline())
print(f.readline(2))
print(f.readline(5))
print(f.readline())
f.close()
# readline ma line pate pasi niche ni line ma na jay.


# In[134]:


f=open('Ex.txt','r')
print(f.readlines())
f.close()
#  readlines ma ek line ma je hoy e list ma ek string ni jem aave.


# In[132]:


f=open('Ex.txt','r')
print(f.readlines(7))    
print(f.readlines(1))
print(f.readlines())
f.close()


# In[131]:


f=open('Ex.txt')
for i in f:
    print(i)
f.close()


# In[135]:


# space taave tya thi alag karo

f=open('Ex.txt')
for i in f:
    for j in i.split():
        print(j)
f.close()


# In[3]:





# In[32]:


# Counting

f=open('Me.txt')
print("No. of Lines :-",len(f.readlines()))
f.seek(0)
print("No. of Character :-",len(f.read()))
f.seek(0)
print("No. of word :-",len(f.read().split()))
f.close()


# In[50]:


#   '#' new file ma na aavva joy
#     f.seek(0) :- Pointer ne first leter pr lai ne jay.

f=open('Me.txt','r')
f1=open('Ex1.txt','w+')

for i in f:
    n=i.find('#')
    if n==-1:
        f1.write(i)
    elif i[0]=='#':
        f1.write("")
    else:
        f1.write(i[:n]+'\n')
        
f.seek(0)
f1.seek(0)

print(f.read())
print("------New File------")
print(f1.read())

f.close()
f1.close()


# In[57]:


#  2-File no Diffrence find karo ane line-column aapo.

f1=open('Me.txt')
f2=open('Ex.txt')
l1=f1.readlines()
l2=f2.readlines()

