import streamlit as st

st.header('Kalkulator Sederhana')

a = st.number_input ('Masukan angka a')
b = st.number_input ('Masukan angka b')

perkalian = a * b
penjumlahan = a + b
perpangkatan = a ** b 
pengurangan = a - b 

if b !=0:
    pembagian = a / b 

if st.button('Jumlahkan'):
    st.success(perkalian)
    st.success(penjumlahan)
    st.success(perpangkatan)
    st.success(pengurangan)
    st.success(pembagian)
   


