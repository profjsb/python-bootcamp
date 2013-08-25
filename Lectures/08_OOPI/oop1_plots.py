import matplotlib.pyplot as plt
import numpy as np


data_vars = [ [0.2,0.7,'x'],
    [0.3,0.6,'y'],
    [0.22,0.5,'newx'],
    [0.21, 0.4,'coolest_y'],
    [0.19,0.24,'perimeter1' ] ]

code_vars = [ [0.2,0.7,'read_sensor()'],
    [0.20,0.5,'calculate_perimeter()'],
    [0.24,0.24,'generate_figure_for_nature_paper()' ] ]

def denude_plot():
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0,1)
    plt.ylim(0,1)

def show_background1():
    plt.figure(figsize=(11.5,8))
    #plt.gcf().clf()
    rect_data = plt.Rectangle((0.1,0.1), 0.3, 0.7, facecolor="#e0e0f0")
    plt.gca().add_patch( rect_data ) 
    rect_code = plt.Rectangle((0.6,0.1), 0.3, 0.7, facecolor="#e0e0f0")
    plt.gca().add_patch( rect_code ) 
    plt.text(0.25, 0.85, 'Data (i.e., numbers)', style='italic', size=16, horizontalalignment='center' )
    plt.text(0.75, 0.85, 'Code', style='italic', size=16, horizontalalignment='center' )
    for n,avar in enumerate(data_vars):
        plt.text( avar[0], avar[1], avar[2], size=10, rotation=np.random.rand()*10.0-5.0, ha="center", va="center", bbox = dict(boxstyle="round", ec=(0.8, 0.1, 1.0), fc=(0.8, 0.4, 1.0),))
    for n,avar in enumerate(code_vars):
        plt.text( avar[0]+0.5, avar[1], avar[2], size=10, rotation=np.random.rand()*10.0-5.0, ha="center", va="center", bbox = dict(boxstyle="round", ec=(1.0, 0.1, 0.8), fc=(1.0, 0.4, 0.8),))
    denude_plot()

def code_to_data():
    ax=plt.gca()
    ax.arrow( data_vars[0][0]+0.5, data_vars[0][1], -0.4, 0.0, head_width=0.01, head_length=0.01,fc='k',ec='k' )
    ax.arrow( data_vars[0][0]+0.5, data_vars[0][1], -0.35,-0.1, head_width=0.01, head_length=0.01,fc='k',ec='k' )
    
def data_to_code():
    ax=plt.gca()
    ax.arrow( data_vars[0][0]+0.0, data_vars[0][1], 0.38, -0.18, head_width=0.01, head_length=0.01,fc='k',ec='k' )
    ax.arrow( data_vars[1][0]+0.0, data_vars[1][1], 0.25, -0.08, head_width=0.01, head_length=0.01,fc='k',ec='k' )
    ax.arrow( code_vars[1][0]+0.5, code_vars[1][1], -0.4, -0.26, head_width=0.01, head_length=0.01,fc='k',ec='k' )
    plt.show()

def Procedural_programming():
    show_background1()
    plt.show()

def Function1():
    show_background1()
    code_to_data()

def Function2():
    show_background1()
    data_to_code()

def Objects():
    plt.figure(figsize=(11.5,8))
    rect_obj = plt.Rectangle((0.1,0.1), 0.4, 0.7, facecolor="#101080")
    plt.gca().add_patch( rect_obj ) 
    rect_data = plt.Rectangle((0.7,0.15), 0.2, 0.2, facecolor="#e0e0f0")
    plt.gca().add_patch( rect_data ) 
    rect_code = plt.Rectangle((0.7,0.55), 0.2, 0.2, facecolor="#e0e0f0")
    plt.gca().add_patch( rect_code ) 
    plt.text(0.3, 0.85, 'Objects', size=16, style='italic', horizontalalignment='center' )
    plt.text(0.8, 0.8, '...(Data)...', size=12, style='italic', horizontalalignment='center' )
    plt.text(0.8, 0.4, '...(Code)...', size=12, style='italic',horizontalalignment='center' )
    for n,avar in enumerate([code_vars[0],code_vars[2]]):
        msg= 'Polygon Sensor %d\n---------------\n<\$$RAWDATA$\$>\n----------\n- acquire_data()\n- calculate_perimeter()\n- make_Nobel_fig()'%n
        plt.text( avar[0], avar[1], msg, size=10, rotation=np.random.rand()*10.0-5.0, ha="left", va="center", bbox = dict(boxstyle="round", ec=(1.0, 1.0, 0.1), fc=(1.0, 1.0, 0.1),))
        #plt.text( avar[0], avar[1], 'Polygon Sensor %d\n---------------\n- acquire_data()\n- calculate_perimeter()'%n, size=10, rotation=np.random.rand()*10.0-5.0, ha="left", va="center", bbox = dict(boxstyle="round", ec=(1.0, 0.1, 0.8), fc=(1.0, 0.4, 0.8),))
    denude_plot()
