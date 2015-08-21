# Modified from http://groups.google.com/group/networkx-discuss/browse_thread/thread/170624d22c4b0ee6?pli=1 

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import numpy as np

def draw_network(G,pos,sg=None,node_color=None,cmap=None):
    f = plt.figure()
    ax = f.gca()

    for n in G:
        if node_color is None or cmap is None:
            color = (0,0,0)
        else:
            color = cmap(node_color[n])

        c=Circle(pos[n],radius=0.13,alpha=0.5,color=color,ec='k')
        x, y = pos[n]
        plt.text(x, y, n,
                horizontalalignment='center',
                verticalalignment='center',
                color='k',
                fontsize=20,
                )
        plt.text(x, y, n,
                 horizontalalignment='center',
                 verticalalignment='center',
                 color='w',
                 fontsize=18,
                 )
        ax.add_patch(c)
        G.node[n]['patch']=c
        x,y=pos[n]
    seen={}
    for (u,v,d) in G.edges(data=True):
        n1=G.node[u]['patch']
        n2=G.node[v]['patch']
        rad=0.1
        if (u,v) in seen:
            rad=seen.get((u,v))
            rad=(rad + np.sign(rad)*0.1)*-1
        alpha=0.5
        color = 'k'
        e = FancyArrowPatch(n1.center,n2.center,patchA=n1,patchB=n2,
                            arrowstyle='-|>',
                            connectionstyle='arc3,rad=%s'%rad,
                            mutation_scale=15.0,
                            lw=2,
                            alpha=alpha,
                            color=color)
        seen[(u,v)]=rad
        ax.add_patch(e)

    ax.autoscale()
    plt.axis('equal')
    plt.axis('off')

    return e

if __name__ == "__main__":
    import networkx as nx
    G=nx.MultiDiGraph([(1,2),(1,2),(2,3),(3,4),(2,4),
                    (1,2),(1,2),(1,2),(2,3),(3,4),(2,4)]
                    )

    pos=nx.spring_layout(G)
    ax=plt.gca()
    draw_network(G,pos,ax)
    ax.autoscale()
    plt.axis('equal')
    plt.axis('off')
    plt.savefig("graph.pdf")
    plt.show() 
