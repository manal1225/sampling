import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv



df= pd.read_csv("data.csv")
data=df['temp'].tolist()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("mean of population is ",population_mean)
print("std_deviation is", std_deviation)

fig = ff.create_distplot([data],["temp"],show_hist= False)
fig.show()



#one sample containing 100 random elements
dataset = []

for i in range(0,100):

    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

sample_mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("mean of sample is ",sample_mean)
print("std_deviation is", std_deviation)

