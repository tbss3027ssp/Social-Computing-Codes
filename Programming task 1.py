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
# 
# 

# In[16]:


# Import Libraries
import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import clustering, degree_assortativity_coefficient
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


##### Import Files
df_edges = pd.read_csv('edges.csv')
df_nodes = pd.read_csv('nodelist.csv')


# In[4]:


def ObtainEdges(df):
    edges_list = [];
    for index, info in df.iterrows():
        edges_list.append((info[0], info[1]))
    return edges_list


# In[5]:


G = nx.Graph()


# In[6]:


edges_list = ObtainEdges(df_edges)


# In[7]:


G.add_edges_from(edges_list)


# In[8]:


G.nodes(data=True)


# In[9]:


nx.draw_networkx(G)


# In[10]:


def ObtainAttr(df):
    attr_dict = dict()
    for index, info in df.iterrows():
        attr_dict[info[0]] = info[1];
    return attr_dict


# In[11]:


attr_dict= ObtainAttr(df_nodes)


# In[12]:


nx.set_node_attributes(G, attr_dict, 'club')


# In[13]:


G.nodes(data=True)


# In[14]:


color_map = []

size_map = []
median_degree = np.median(np.array([list(nx.degree_centrality(G).values())]))

for node, value in G.nodes(data=True):
    if value['club'] == df_nodes.club.unique()[0]:
        color_map.append('green')
    elif value['club'] == df_nodes.club.unique()[1]:
        color_map.append('red')

for node, deg in nx.degree_centrality(G).items():
    if deg > median_degree:
        size_map.append(700)
    else:
        size_map.append(200)

nx.draw(G, node_color=color_map, with_labels=True, node_size=size_map)


# In[15]:


# Task 4: calculate measures
print('1.')
print('Density:', nx.density(G), sep='\n')
print()

print('Diameter:', nx.diameter(G), sep='\n')
print()

print('2. Centralities')
print('Degree:', nx.degree_centrality(G), sep='\n')
print()

print('Betweenness:', nx.betweenness_centrality(G), sep='\n')
print()

print('Closeness:', nx.closeness_centrality(G), sep='\n')
print()

print('Eigenvector:', nx.eigenvector_centrality(G), sep='\n')
print()


# In[ ]:




