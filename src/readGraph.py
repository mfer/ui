#!/usr/bin/env python
from igraph import *

def dist(g,v,u):
    return ((g.vs[u]["x"]-g.vs[v]["x"]) ** 2 + (g.vs[u]["y"]-g.vs[v]["y"]) ** 2) ** 0.5

file_graph = "netherlands.osm.graph.100"
file_xyz = "netherlands.osm.xyz"

NODES=2216688
g = Graph(NODES)

#reading node position
with open(file_xyz) as f:
    content = f.readlines()
n=0
for c in content:
    nodes = c.split(' ')
    x = float(nodes[0])
    y = float(nodes[1])
    g.vs[n]["id"]=n
    g.vs[n]["x"]=x
    g.vs[n]["y"]=y
    n=n+1

#reading connections between nodes
with open(file_graph) as f:
    content = f.readlines()
for c in content:
    nodes = c.split(' ')
    #print "%d - %s" %(len(nodes)-1, c)
    for m in range(1,len(nodes)):
        a = int(nodes[0])-1
        b = int(nodes[m])-1
        #print "%d %d %d"%(a,b,dist(g,a,b))
        g[a,b]=dist(g,a,b)

#for n in range(0,NODES):
    #print g.vs[n].degree()
#    if g.vs[n].degree() == 0:
#        g.delete_vertices(n)


plot(g.clusters(),"g.png",vertex_size=5)

#layout=[]
#for n in range(0,NODES):
#    layout.append((g.vs[n]["x"],g.vs[n]["y"]))
#plot(g,"g.png",vertex_size=2, layout=layout)
