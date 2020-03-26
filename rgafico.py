#!/usr/bin/env python
# coding: utf-8

# In[7]:


import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
#


# In[3]:


def andamento_json():
    grezzi = pd.read_json("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json")
    return grezzi


# In[10]:


df=andamento_json()
df.head()


# In[25]:


fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.data,
                y=df['totale_ospedalizzati'],
                name="Ospedalizzati",
                line=dict(color='#ABD71F', width=4),
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.data,
                y=df['terapia_intensiva'],
                name="Ricoverati in terapia intensiva",
                line=dict(color='#1FD7A7', width=4),
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.data,
                y=df['isolamento_domiciliare'],
                name="Isolamento domiciliare",
                line=dict(color='#4B1FD7', width=4),
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.data,
                y=df['dimessi_guariti'],
                name="Dimessi guariti",
                line=dict(color='#D71F4F', width=4),
                opacity=0.8))

# Use date string to set xaxis range
fig.update_layout(xaxis_range=[df.data.iloc[0],df.data.iloc[-1]],
                  title_text="Ospedalizzati e guariti"
                 )


# In[26]:


plot(fig,filename='Ospedalizzati e guariti.html')


# In[ ]:




