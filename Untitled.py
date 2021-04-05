#!/usr/bin/env python
# coding: utf-8

# In[1]:


# item i1 to i5
arr = [0, 13, 14, 10, 20]


# In[2]:


def h(x):
    return x % 5


# In[3]:


hashTable = {x: [None, 0] for x in range(5)}


# In[4]:


def tableSize(table):
    size = 0
    for i in table.values():
        if i[0] != None:
            size += 1
    return size


# In[5]:


def insert(item):
    global hashTable
    
    hashCode = h(item)
    i = 0
    
    while (hashTable[(hashCode + i) % len(hashTable)][0] != None)                and (i < len(hashTable)):
        i += 1
                    
    if tableSize(hashTable) == len(hashTable):
        return
    else:
        hashTable[(hashCode + i) % len(hashTable)][0] = item
    
    return hashTable


# In[6]:


for i in arr:
    insert(i)


# In[7]:


def delete(idx):
    global hashTable
    
    hashTable[idx][0] = None
    hashTable[idx][1] = 1


# In[8]:


delete(0)


# In[9]:


hashTable


# In[10]:


def search(item):
    global hashTable
    
    hashCode = h(item)
    i = 0
        
    while ((hashTable[(hashCode + i) % len(hashTable)][0] != None)                and (i < len(hashTable))):
        
        if hashTable[(hashCode + i) % len(hashTable)][0] == item:
            message = "item is found at index {}".format((hashCode + i) % len(hashTable))
            return message
        
        i += 1
        
    return "Not found"


# In[11]:


search(10), search(20)


# In[ ]:




