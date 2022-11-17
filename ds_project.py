#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time

#import the data
data = pd.read_csv("gaikindo.csv")
image = Image.open("house.png")
st.title("Selamat Datang di Aplikasi cekhargarumah")
st.image(image, use_column_width=True)

#checking the data
st.write("Aplikasi ini dibuat untuk mengecek harga mobil menggunakan algoritma kecerdasan buatan. Let's try and see!")
check_data = st.checkbox("Lihat contoh data")
if check_data:
    st.write(data.head(10))
	
st.write("Mari kita lihat berapa harga mobilnya.")

#input the numbers
sqft_liv = st.slider("Berapa kapasitas mesin yang anda cari?",int(data.sqft_living.min()),int(data.sqft_living.max()),int(data.sqft_living.mean()) )
bath     = st.slider("Berapa banyak tempat duduk dibutuhkan?",int(data.bathrooms.min()),int(data.bathrooms.max()),int(data.bathrooms.mean()) )
bed      = st.slider("Berapa banyak jumlah pintu yang dibutuhkan?",int(data.bedrooms.min()),int(data.bedrooms.max()),int(data.bedrooms.mean()) )
floor    = st.slider("berapa tenaga mesin yang anda inginkan?",int(data.floors.min()),int(data.floors.max()),int(data.floors.mean()) )

#splitting your data
X = data.drop('price', axis = 1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#import your model
model=LinearRegression()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = model.predict([[sqft_liv,bath,bed,floor]])[0]

#checking prediction house price
if st.button("Cek Harga Mobil?"):
    st.header("Harga mobil berdasarkan kebutuhan anda adalah Rp {}".format(int(predictions)))
    st.subheader("Range perkiraan harga mobil anda adalah Rp {} - USD {}".format(int(predictions-errors),int(predictions+errors) ))
