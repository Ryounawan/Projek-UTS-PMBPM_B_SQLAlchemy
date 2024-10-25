import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

model_path = 'BestModel_CLF_RandomForest_SQLAlchemy.pkl'
model_path2 = 'BestModel_REG_RandomForest_SQLAlchemy.pkl'

with open(model_path, 'rb') as f:
    lr_model = pickle.load(f)

with open(model_path2, 'rb') as f:
    svr_model = pickle.load(f)

with st.sidebar:
    selected = option_menu('SQLAlchemy UTS ML 24/25',
                            ['Klasifikasi', 'Regresi', 'Catatan'],
                            default_index=0)

if selected == 'Klasifikasi':
    st.title('Klasifikasi')
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

    if st.button("Cek Kategori"):
        lr_model_prediction = lr_model.predict(input_data)
        st.write(f"Prediksi Model : {lr_model_prediction}")

if selected == 'Regresi':
    st.title('Regresi')
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

    if st.button("Prediksi Price"):
        svr_model_prediction = svr_model.predict(input_data)
        st.markdown(f"Prediksi Harga properti : $ {svr_model_prediction[0]:.1f}")
