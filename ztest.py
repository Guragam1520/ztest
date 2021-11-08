import statistics
import plotly.express as px
import pandas as pd
import random
import plotly.figure_factory as ff
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

population_mean=statistics.mean(data)
print("Mean = ", population_mean)
population_stdDeviation=statistics.stdev(data)
print("Standard Deviation = ", population_stdDeviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,1000):
        random_index=random.randint(0, len(data))
        value=data[random_index]
        dataset.append(value)
    return mean
mean=statistics.mean(dataset)


def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

first_standard_deviation_start, first_standard_deviation_end= mean-std_deviation, mean+std_deviation
second_standard_deviation_start, second_standard_deviation_end= mean-(2*std_deviation), mean+(2*std_deviation)
third_standard_deviation_start, third_standard_deviation_end= mean-(3*std_deviation), mean+(3*std_deviation)
print("std1", first_standard_deviation_start, first_standard_deviation_end)
print("std2", second_standard_deviation_start, second_standard_deviation_end)
print("std3", third_standard_deviation_start, third_standard_deviation_end)

fig=ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name="MEAN"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_start, first_standard_deviation_start], y=[0, 0.17], mode='lines', name="First Std Deviation start"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode='lines', name="First Std Deviation end"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_start, second_standard_deviation_start], y=[0, 0.17], mode='lines', name="Second Std Deviation start"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end, first_standard_deviation_end], y=[0, 0.17], mode='lines', name="Second Std Deviation end"))
fig.add_trace(go.Scatter(x=[third_standard_deviation_start, third_standard_deviation_start], y=[0, 0.17], mode='lines', name="Third Std Deviation start"))
fig.add_trace(go.Scatter(x=[third_standard_deviation_end, third_standard_deviation_end], y=[0, 0.17], mode='lines', name="Third Std Deviation end"))
fig.show()
