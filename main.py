import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import time
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium
#add title
st.title('Accessibility Analysis')

#add a sidebar in streamlit
st.sidebar.header('Choose a city:')

location = 'Okemos, MI, USA'
#add a text input
location = st.sidebar.text_input('City Name:', location)

G = ox.graph_from_place(location, network_type='drive')

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

df_nodes = pd.DataFrame(gdf_nodes.drop(columns=["geometry"]))
df_edges = pd.DataFrame(gdf_edges.drop(columns=["geometry"]))
#st display geo data frame
#st.dataframe(df_nodes)
#st.dataframe(df_edges)

# explore nodes and edges together in a single map
nodes, edges = ox.graph_to_gdfs(G)
m = edges.explore(color="skyblue", tiles="cartodbdarkmatter")
nodes.explore(m=m, color="pink", 
              marker_kwds={"radius": 3}, 
              popup_hover=True, 
              popup_column="osmid",
              #show osmid labels for nodes
              annotate=True
              
              )

#st display the html file
st_folium(m, width=725)

#select a node from the folium map
# use networkx to calculate the shortest path between two nodes
origin_node = list(G.nodes())[0]
destination_node = list(G.nodes())[-1]
route = nx.shortest_path(G, origin_node, destination_node)

# plot the route with folium
# like above, you can pass keyword args along to folium PolyLine to style the lines
# plot the street network with folium
#m1 = ox.plot_graph_folium(G, popup_attribute="name", weight=2, color="#8b0000")
#m3 = ox.plot_route_folium(G, route, route_map=m1, popup_attribute="length", weight=7)
#st_folium(m1, width=725)