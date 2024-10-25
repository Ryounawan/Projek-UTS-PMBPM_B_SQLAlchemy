import os
import pickle

import streamlit as st
from streamlit_option_menu import option_menu

model_path = 'BestModel_CLF_RandomForest_SQLAlchemy.pkl'
model_path2 = 'BestModel_REG_RandomForest_SQLAlchemy.pkl'

model = os.path.join(model_path, 'rb')
with open(model, 'rb') as f:
    lr_model = pickle.load(f)

model2 = os.path.join(model_path2, 'rb')
with open(model2, 'rb') as f:
    svr_model = pickle.load(f)

# with open(lr_model_path, 'rb') as f:
#     lr_model = pickle.load(f)

# with open(svr_model_path, 'rb') as f:
#     svr_model = pickle.load(f)

with st.sidebar:
    selected = option_menu('Tutorial Desain Streamlit UTS ML 24/25',
                            ['Klasifikasi', 'Regresi', 'Catatan'],
                            default_index=0)

if selected == 'Klasifikasi':
    st.title('Klasifikasi')

    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader('Masukkan File', type=['csv', 'txt'])

    LuasTanah = st.number_input('Input luas tanah dalam meter persegi (squaremeters): ', 0)
    JumlahKamar = st.slider('Input Jumlah Kamar (numberofrooms): ', 0, 100)
    Halaman = st.radio('Apakah memiliki halaman (hasyard)?', ['Yes', 'No'])
    KolamRenang = st.radio('Apakah memiliki kolam renang (haspool)?', ['Yes', 'No'])
    JumlahLantai = st.slider('Input Jumlah Lantai (floors): ', 0, 100)
    KodeLokasi = st.number_input('Input Kode Lokasi (citycode): ', 0)
    CityPartRange = st.slider('Input Ekslusivitas Kawasan (citypartrange): ', 0, 10)
    JumlahPemilik = st.slider('Jumlah Pemilik Sebelumnya (numprevowners): ', 0, 10)
    TahunPembuatan = st.number_input('Input Tahun Pembuatan (made): ', 0)
    GedungBaru = st.radio('Apakah gedung baru atau bukan (isnewbuilt)?', ['Old', 'New'])
    PelindungBadai = st.radio('Apakah memiliki pelindung badai (hasstormprotector)?', ['Yes', 'No'])
    Basement = st.number_input('Input luas basement (basement): ', 0)
    Loteng = st.number_input('Input luas loteng (attic): ', 0)
    Garasi = st.number_input('Input luas garasi (garage): ', 0)
    Gudang = st.radio('Apakah memiliki Gudang (hasstorageroom)?', ['Yes', 'No'])
    RuangTamu = st.slider('Input Ruang Tamu (hasguestroom): ', 0, 10)

    input_halamanY = 1 if Halaman == "Yes" else 0
    input_kolamRenangY = 1 if KolamRenang == "Yes" else 0
    input_gedungBaruY = 1 if GedungBaru == "New" else 0
    input_pelindungBadaiY = 1 if PelindungBadai == "Yes" else 0
    input_gudangY = 1 if Gudang == "Yes" else 0

    input_data = [[
        LuasTanah, JumlahKamar, input_halamanY, 1 - input_halamanY, input_kolamRenangY, 1 - input_kolamRenangY,
        JumlahLantai, KodeLokasi, CityPartRange, JumlahPemilik, TahunPembuatan, 
        input_gedungBaruY, 1 - input_gedungBaruY, input_pelindungBadaiY, 1 - input_pelindungBadaiY, 
        Basement, Loteng, Garasi, input_gudangY, 1 - input_gudangY, RuangTamu
    ]]

    st.write(f"Shape of input data: {len(input_data[0])} features")
    
    if st.button("Cek Kategori"):
            lr_model_prediction = lr_model.predict(input_data)
            st.write(f"Prediksi Model : {lr_model_prediction}")


if selected == 'Regresi':
    st.title('Regresi')

    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader('Masukkan File', type=['csv', 'txt'])

    LuasTanah = st.number_input('Input luas tanah dalam meter persegi (squaremeters): ', 0)
    JumlahKamar = st.slider('Input Jumlah Kamar (numberofrooms): ', 0, 100)
    Halaman = st.radio('Apakah memiliki halaman (hasyard)?', ['Yes', 'No'])
    KolamRenang = st.radio('Apakah memiliki kolam renang (haspool)?', ['Yes', 'No'])
    JumlahLantai = st.slider('Input Jumlah Lantai (floors): ', 0, 100)
    KodeLokasi = st.number_input('Input Kode Lokasi (citycode): ', 0)
    CityPartRange = st.slider('Input Ekslusivitas Kawasan (citypartrange): ', 0, 10)
    JumlahPemilik = st.slider('Jumlah Pemilik Sebelumnya (numprevowners): ', 0, 10)
    TahunPembuatan = st.number_input('Input Tahun Pembuatan (made): ', 0)
    GedungBaru = st.radio('Apakah gedung baru atau bukan (isnewbuilt)?', ['Old', 'New'])
    PelindungBadai = st.radio('Apakah memiliki pelindung badai (hasstormprotector)?', ['Yes', 'No'])
    Basement = st.number_input('Input luas basement (basement): ', 0)
    Loteng = st.number_input('Input luas loteng (attic): ', 0)
    Garasi = st.number_input('Input luas garasi (garage): ', 0)
    Gudang = st.radio('Apakah memiliki Gudang (hasstorageroom)?', ['Yes', 'No'])
    RuangTamu = st.slider('Input Ruang Tamu (hasguestroom): ', 0, 10)

    if Halaman == "Yes":
        input_halamanY = 1
        input_halamanN = 0
    else:
        input_halamanY = 0
        input_halamanN = 1

    if KolamRenang == "Yes":
        input_kolamRenangY = 1
        input_kolamRenangN = 0
    else:
        input_kolamRenangY = 0
        input_kolamRenangN = 1
    
    if GedungBaru == "New":
        input_gedungBaruY = 1
        input_gedungBaruN = 0
    elif GedungBaru == "Old":
        input_gedungBaruY = 0
        input_gedungBaruN = 1

    if PelindungBadai == "Yes":
        input_pelindungBadaiY = 1
        input_pelindungBadaiN = 0
    else:
        input_pelindungBadaiY = 0
        input_pelindungBadaiN = 1

    if Gudang == "Yes":
        input_gudangY = 1
        input_gudangN = 0
    else:
        input_gudangY = 0
        input_gudangN = 1

    input_data = [[
        LuasTanah, JumlahKamar, input_halamanY, input_halamanN, input_kolamRenangY, input_kolamRenangN,
        JumlahLantai, KodeLokasi, CityPartRange, JumlahPemilik, TahunPembuatan, 
        input_gedungBaruY, input_gedungBaruN, input_pelindungBadaiY, input_pelindungBadaiN, Basement, Loteng, Garasi, 
        input_gudangY, input_gudangN, RuangTamu
    ]]


    if st.button("Prediksi Price"):
        svr_model_prediction = svr_model.predict(input_data)
        st.markdown(f"Prediksi Harga properti : $ {svr_model_prediction[0]:.2f}")

if selected == 'Catatan':
    st.title('Catatan')
    st.write('Untuk memunculkan sidebar agar tidak error ketika di run, silahkan install library streamlit option menu dengan perintah "pip install streamlit-option-menu".')
    st.write('Pada contoh di atas ada 2 yaitu Klasifikasi dan Regresi.')
    st.write('Silahkan sesuaikan dengan arsitektur code anda pada notebook.')
    st.write('Untuk lebih lanjut bisa di akses pada https://streamlit.io/')
    st.write('Link desain streamlit dapat diakses pada https://aputsc-6jzfv4fiuzj84mfc7k7.streamlit.app/')
    st.write('Untuk requirements yang dibutuhkan untuk deploy online di github ada 5 yaitu streamlit, scikit-learn, pandas, numpy, streamlit-option-menu.')
