
# coding: utf-8

# In[11]:

import numpy as np
a=np.array([[1,7],[2,5]])
print(a)


# In[29]:

b=np.array([[2,2],[4,5]])


# In[24]:

c=np.concatenate((a,b),axis=0)
print(c)


# In[30]:

d=np.stack((a,b),axis=0)
print(d)


# In[33]:

e=np.hstack((a,b))
print(e)


# In[34]:

f=np.split(e,1)
print(f)


# In[40]:

g=np.hsplit(e,4)
print(g)


# In[44]:

h=np.vsplit(e,2)
print(h)


# In[48]:

i=np.delete(f,6)
print(i)


# In[51]:

i=np.insert(f,1,6)
print(i)


# In[52]:

j=np.resize(g,[3,2])
print(j)


# In[53]:

k=np.trim_zeros(i)
print(k)


# In[54]:

k=np.unique(i)
print(k)


# In[57]:

l=np.flip(g,0)
print(l)


# In[63]:

m=np.rot90(a,1)
print(m)


# In[ ]:



