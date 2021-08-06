from pycaret.utils import check_metric
import streamlit as st
import os
import pandas as pd
from pycaret.regression import *
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
​
​
sns.set_style("darkgrid")
​
​
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn: ANd9GcRiHifL1e-eKEP3ZkcSDqj-jsfwVTZ5Qq5e6w & usqp=CAU")
​
​
example = pd.read_csv("unseen_data.csv")
st.info('File must be in the following format')
st.dataframe(example.head())
​
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)
if uploaded_file is None:
    st.info("Please upload a CSV")
    st.stop() 
​
​
df = pd.read_csv(uploaded_file)
st.write("Here is your dataset")
st.dataframe(df)
​
saved_final_rf = load_model('Final RF Model 08-04-2021')
new_prediction = predict_model(saved_final_rf, data=df)
st.write('Here are your predictions.  The predicted price is located in the Label column')
st.dataframe(new_prediction)
​
​
value = check_metric(new_prediction.price, new_prediction.Label, 'R2')
st.write("R2 of your Model")
st.write(value)
​
price_difference = new_prediction.price - new_prediction.Label
st.write('Price Difference Summary')
st.dataframe(price_difference.describe())
​
fig, ax = plt.subplots()
ax.scatter(new_prediction.Label.values, new_prediction.price.values)
​
# fig = new_prediction.plot.scatter(x="Label", y="price",figsize=(14,8))
st.pyplot(fig)