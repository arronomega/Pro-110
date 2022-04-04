import pandas as pd 
import csv 
import random as rand
import statistics as st
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv("medium_data.csv")
df.head()
data = df["claps"].tolist()
pop_mean = st.mean(data)
fig = ff.create_distplot([data],["claps"],show_hist = False)
fig.show()
pop_dev = st.stdev(data)
pop_med=st.median(data)
pop_mode = st.mode(data)
dataset =[]
for i in range(0,100):
    index = rand.randint(0,len(data))
    value = data[index]
    dataset.append(value)
sp_mean = st.mean(dataset)
sp_stdev = st.stdev(dataset)
def random_set_of_data(counter):
    dataset =[]
    for i in range(0,counter):
        index = rand.randint(0,len(data)-1)
        value1 = data[index]
        dataset.append(value1)
    sp_mean = st.mean(dataset)
    return sp_mean
def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode ="lines",name = "MEAN"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_data(10)
        mean_list.append(set_of_means)
    mean = st.mean(mean_list)
    print("Mean of sampling distribution of Math score :-",mean )
setup()
def standard_dev():
    mean_list =[]
    for i in range(0,1000):
        set_of_means = random_set_of_data(100)
        mean_list.append(set_of_means)
    std_deviation = st.stdev(mean_list)
    print("Standard deviation of sampling distribution:-",std_deviation)
standard_dev()
