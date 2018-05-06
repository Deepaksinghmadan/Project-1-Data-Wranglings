
# coding: utf-8

# In[14]:

import numpy as np
b=np.full([4,3],2)
c=np.empty([4,3])
np.copyto(c,b)
print(c)


# In[16]:

d=np.reshape(c,[6,2])
print(d)


# In[17]:

np.ravel(d)


# In[23]:

d.flat[2]


# In[25]:

d.flatten('F')


# In[28]:

f=np.arange(1,7).reshape(2,3)


# In[29]:

print(f)


# In[34]:

g=np.moveaxis(f,1,0)
print(g)


# In[35]:

g.T


# In[39]:

np.transpose(g.T)


# In[40]:

np.atleast_1d(g)


# In[56]:

np.atleast_3d(g)


# In[57]:

np.broadcast(g)


# In[53]:

h=np.broadcast_to(g,[3,2])
print(h)


# In[61]:

k=np.expand_dims(g,1)
print(k)


# In[62]:

np.squeeze(k)


# In[63]:

np.asarray(g)


# In[64]:

np.asanyarray(g)


# In[65]:

np.asmatrix(g)


# In[66]:

np.asfarray(g)


# In[67]:

np.asfortranarray(g)


# In[68]:

np.ascontiguousarray(g)


# In[69]:

np.asarray_chkfinite(g)


# In[78]:

a=np.asarray([3],1)
np.asscalar(a)


# In[79]:

np.require(g)


# In[ ]:



