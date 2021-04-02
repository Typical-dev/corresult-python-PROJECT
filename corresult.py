import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cold_drink_sales.append(float(row("Ice-cream Sales")))
            ice_cream_sales.append(float(row("Temperature")))
        return{"x": ice_cream_sales, "y": cold_drink_sales}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(f"correlation coefficient is {correlation}")
def setup():
    data_path = "ice-cream.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()