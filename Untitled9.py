#!/usr/bin/env python
# coding: utf-8

# In[2]:


def square_num(n):
    return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))
           


# In[3]:



nums= (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))


# In[4]:


r = lambda a : a+25 
print(r(10))


# In[ ]:




