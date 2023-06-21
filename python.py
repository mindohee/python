#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def f(x):
    return x*(x-2)


# In[3]:


print(f(np.array([0,2,-10,5])))


# In[4]:


x = np.linspace(-5,5,10)


# In[18]:


def f2(x):
    r = -2*x**3 - x**2 + 20*x
    return r

x = np.linspace(-3,3,100)
plt.plot(x,f2(x))
plt.show()


# In[11]:





# In[ ]:




