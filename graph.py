# Imports that you are going to need to read a file
import pandas as pd
import datetime

# Read the file using pandas - so much easier than writing your own file I/O!
df_symbol_bar_Data = pd.read_csv("AAPL.csv")

# Show some of the data you read
df_symbol_bar_Data.head()
####### Import the library you need to create the chart
import plotly.graph_objs as go
data=[go.Candlestick(x=df_symbol_bar_Data['Date'],
                open=df_symbol_bar_Data['Open'],
                high=df_symbol_bar_Data['High'],
                low=df_symbol_bar_Data['Low'],
                close=df_symbol_bar_Data['Close'])]
figSignal = go.Figure(data=data)
figSignal.show()
# Create a basic layout that names the chart and each axis.
layout = dict(
        title="FB Facebook",
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title( text="Time")),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title( text="Price $ - US Dollars"))
)


# set the data from our data frame
data=[go.Candlestick(x=df_symbol_bar_Data['Date'],
                open=df_symbol_bar_Data['Open'],
                high=df_symbol_bar_Data['High'],
                low=df_symbol_bar_Data['Low'],
                close=df_symbol_bar_Data['Close'])]

# display the Candlestic chart with the optional layout
figSignal = go.Figure(data=data, layout=layout)
figSignal.show()
