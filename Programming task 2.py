#!/usr/bin/env python
# coding: utf-8

# #### Python version: 3.8.3
# 
# #### Jupyter notebook version: 6.0.3
# 
# #### Networkx version: 2.4
# 
# #### Files used: Provided by instructors, edges.csv, nodelist.csv
# ##### - Please put the files under sharing the same directory with this notebook-
# 
# #### Student Name: POON Sze Sen
# 
# #### Student Number: 3035752729

# In[1]:


import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import clustering, attribute_assortativity_coefficient, transitivity
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 30})


# In[2]:


##### Import Files
df_edges = pd.read_csv('edges.csv')
df_nodes = pd.read_csv('nodelist.csv')


# In[3]:


def obtainEdges(df):
    edges_list = [];
    for index, info in df.iterrows():
        edges_list.append((info[0], info[1]))
    return edges_list


# In[4]:


def obtainAttr(df):
    attr_dict = dict()
    for index, info in df.iterrows():
        attr_dict[info[0]] = info[1];
    return attr_dict


# In[5]:


def obtainLargestCosine(df):
    
    largest = 0;
    
    for col in range(len(df.columns)):
        for row in range(len(df.index)):
            
            value = df.iloc[col,row]
            
            if (col!=row) & (value >= largest):
                largest = value;

    return largest


# In[6]:


def obtainPairsCosine(largest_cos, df):
    
    pairs = []
    
    for col in range(len(df.columns)):
        for row in range(len(df.index)):
            
            value = df.iloc[col,row]
            
            if (col!=row) & (value == largest_cos):
                pairs.append((col, row))
        
    return pairs


# In[7]:


def obtainPairsJaccard(largest_jac, data):
    
    pairs = []
    
    for i in data:
        if i[2] == largest_jac:
            pairs.append((i[0],i[1]))
            
    return pairs
        


# ##### Create Graph

# In[8]:


G = nx.Graph()


# In[9]:


edges_list = obtainEdges(df_edges)


# In[10]:


G.add_edges_from(edges_list)


# In[11]:


G.nodes(data=True)


# ##### Task1: Assortativity Computation

# In[12]:


attr_dict= obtainAttr(df_nodes)


# In[13]:


nx.set_node_attributes(G, attr_dict, 'club')


# In[14]:


G.nodes(data=True)


# In[15]:


attribute_assortativity_coefficient(G, 'club')


# ##### Task2: Add Local Clustering Coefficient

# In[16]:


attr_cluster = clustering(G)


# In[17]:


nx.set_node_attributes(G, attr_cluster, 'cluster')


# In[18]:


G.nodes(data=True)


# ##### Task3: Pair of nodes with largest Cosine/ Jaccard

# In[19]:


c_s = cosine_similarity(nx.to_numpy_matrix(G)).tolist()


# In[20]:


df_c_s = pd.DataFrame.from_records(c_s)


# In[21]:


obtainPairsCosine(obtainLargestCosine(df_c_s), df_c_s)


# In[22]:


largest_jac = max([i[2] for i in nx.jaccard_coefficient(G)])


# In[23]:


obtainPairsJaccard(largest_jac, nx.jaccard_coefficient(G))


# ##### Task4: Plot Scatter Figure

# In[24]:


deg_centrality = list(nx.degree_centrality(G).values())


# In[25]:


cluster_coef = list(attr_cluster.values())


# In[26]:


fig , ax = plt.subplots(figsize=(8,6))

plt.style.use('seaborn')

plt.grid(True)

ax.set_xlabel('degree centrality')
ax.set_ylabel('local clustering')
ax.scatter(x=deg_centrality, y=cluster_coef)


# In[ ]:




