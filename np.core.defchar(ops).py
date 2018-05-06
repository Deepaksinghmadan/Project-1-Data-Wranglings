
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


# In[69]:

b=np.array('deepak ')
c=np.array('singh')
a=np.core.defchararray.add(b,c)
print(a)


# In[68]:

d=np.core.defchararray.multiply(b,3)
print(d)


# In[73]:

a=np.core.defchararray.center(b,10)
print(a)


# In[76]:

a=np.core.defchararray.encode(b)
print(a)


# In[78]:

a=np.core.defchararray.upper(b)
print(a)


# In[81]:

a=np.core.defchararray.rjust(b,7)
print(a)


# In[86]:

a=np.core.defchararray.strip(b)
print(a)


# In[87]:

a=np.core.defchararray.title(b)
print(a)


# In[ ]:



