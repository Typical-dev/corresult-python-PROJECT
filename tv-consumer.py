import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    Size_of_TV = []
    Average_time_on_TV = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row["Size of TV"]))
            Average_time_on_TV.append(float(row["Average time on TV"]))
        return{"x": Size_of_TV, "y":Average_time_on_TV}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(f"correlation coefficient is {correlation}")
def setup():
    data_path = "tv-consumer.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()