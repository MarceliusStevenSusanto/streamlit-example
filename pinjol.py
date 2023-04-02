import streamlit as st

def total_pinjaman(gaji_bulanan, jumlah_tanggungan, durasi_pinjaman):
    """
    Fungsi ini bertujuan untuk menghitung total uang yang dapat dipinjam,
    sesuai dengan kondisi yang telah ditentukan.
    
    Parameters:
    gaji_bulanan (int): gaji bulanan yang diterima
    jumlah_tanggungan (int): jumlah tanggungan yang ada dalam keluarga
    durasi_pinjaman (int): lama waktu pinjaman yang diinginkan dalam bulan
    
    Returns:
    total uang yang dapat dipinjam (int)
    """
    try:
        gaji_bulanan = int(gaji_bulanan)
        jumlah_tanggungan = int(jumlah_tanggungan)
        durasi_pinjaman = int(durasi_pinjaman)
    except ValueError:
        return "Input parameters harus berupa angka"
    
    # kondisi handling untuk gaji bulanan
    if gaji_bulanan < 3000000:
        return "Gaji bulanan tidak mencukupi"
    
    # kondisi handling untuk jumlah tanggungan berdasarkan gaji bulanan
    if gaji_bulanan <= 3000000:
        if jumlah_tanggungan > 2:
            return "Jumlah tanggungan terlalu banyak"
    elif gaji_bulanan < 5000000:
        if jumlah_tanggungan > 3:
            return "Jumlah tanggungan terlalu banyak"
    elif gaji_bulanan < 10000000:
        if jumlah_tanggungan > 4:
            return "Jumlah tanggungan terlalu banyak"
    elif gaji_bulanan < 15000000:
        if jumlah_tanggungan > 6:
            return "Jumlah tanggungan terlalu banyak"
    elif gaji_bulanan <= 20000000:
        if jumlah_tanggungan > 8:
            return "Jumlah tanggungan terlalu banyak"
    
    # kondisi handling untuk durasi pinjaman
    if durasi_pinjaman < 6 or durasi_pinjaman > 24:
        return "Durasi pinjaman tidak sesuai ketentuan"
    
    # kondisi handling untuk tingkat bunga berdasarkan gaji bulanan
    if gaji_bulanan < 5000000:
        tingkat_bunga = 0.25
    elif gaji_bulanan < 10000000:
        tingkat_bunga = 0.3
    else:
        tingkat_bunga = 0.4
    
    # hitung total uang yang dapat dipinjam
    pinjaman = gaji_bulanan * durasi_pinjaman * tingkat_bunga
    return pinjaman

st.title('Kalkulator Pinjol')
st.set_page_config(page_title="Kalkulator Pinjaman", page_icon=":money_with_wings:", layout="wide", theme="light")
st.markdown("Ini adalah aplikasi sederhana untuk menghitung jumlah pinjaman yang dapat Anda ambil.")

with st.form('input_form'):
    st.write('Silahkan masukkan nilai-nilai berikut:')
    gaji_bulanan = st.number_input('Gaji Bulanan', min_value=0)
    jumlah_tanggungan = st.number_input('Jumlah Tanggungan', min_value=0)
    durasi_pinjaman = st.slider('Durasi Pinjaman (bulan)', min_value=6, max_value=24, value=12)
    submitted = st.form_submit_button('Hitung')

if submitted:
    pinjaman = total_pinjaman(gaji_bulanan, jumlah_tanggungan, durasi_pinjaman)
    st.write(f'Total uang yang dapat dipinjam: {pinjaman}')
    
