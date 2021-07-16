#!/usr/bin/env python
# coding: utf-8

# # The Multidimensional Knapsack Problem

# Mohammed Alagha, July 2021
# 
# Glasgow, UK

# A mathematical model for the MKP problem.

# Modeled using IBM CPLEX 

# In[1]:


# Importing relevant libraries
import cplex
from docplex.mp.model import Model


# In[2]:


# # Import the reading function
import MKP_populate_function as rdmkp


# In[11]:


# Call the function on a given instance
instance = 'mknap07_1.txt'
c, A, b = rdmkp.MKPpopulate(instance)

# Define the ranges for variables and constraints
nCols, nRows = range(len(c)), range(len(b))


# In[12]:


# Create an empty model
mkp = Model('Mkp')


# In[13]:


# Define decision variables
x = mkp.binary_var_list(nCols, lb = 0, ub = 1, name = 'x')


# In[14]:


# Define constraints
constraints = mkp.add_constraints(sum(A[i][j] * x[j] for j in nCols) <= b[i] for i in nRows)


# In[15]:


# Define objective function
profit = mkp.sum(c[j] * x[j] for j in nCols)


# In[16]:


# Add objective function as a kpi to the model
mkp.add_kpi(profit, 'profit')

# Set objective sense to 'maximization'
objective = mkp.maximize(profit)


# In[17]:


# Solving the model
mkp.solve()


# In[18]:


# Reporting results
mkp.report()


# In[ ]:




