import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df_day = pd.read_csv("Bike-sharing-dataset/day.csv")
df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")

# Data Cleaning
df_day["dteday"] = pd.to_datetime(df_day["dteday"])
df_hour["dteday"] = pd.to_datetime(df_hour["dteday"])

# Title and description
st.title("Analisis Data Peminjaman Sepeda")
st.markdown("""
    Dashboard ini menampilkan hasil analisis data peminjaman sepeda berdasarkan cuaca, hari dalam seminggu, dan jam dalam sehari.
""")

# Informasi Umum dan Statistik Deskriptif
st.header("Informasi Umum dan Statistik Deskriptif")

st.subheader("Dataframe df_day")
st.write(df_day.describe())
st.subheader("Dataframe df_hour")
st.write(df_hour.describe())

# Distribusi Variabel Kategori pada Dataframe df_day
st.header("Distribusi Variabel Kategori pada Dataframe df_day")
fig1, ax1 = plt.subplots(figsize=(15, 10))
plt.suptitle('Distribusi Variabel pada Dataframe df_day', fontsize=16)
for i, column in enumerate(['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']):
    plt.subplot(2, 4, i+1)
    sns.countplot(data=df_day, x=column)
    plt.title(f'Distribusi {column}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
st.pyplot(fig1)

# Distribusi Variabel Kategori pada Dataframe df_hour
st.header("Distribusi Variabel Kategori pada Dataframe df_hour")
fig2, ax2 = plt.subplots(figsize=(20, 15))
plt.suptitle('Distribusi Variabel pada Dataframe df_hour', fontsize=16)
for i, column in enumerate(['season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']):
    plt.subplot(3, 3, i+1)
    sns.countplot(data=df_hour, x=column)
    plt.title(f'Distribusi {column}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
st.pyplot(fig2)

# Korelasi Antar Variabel di df_day
st.header("Korelasi Antar Variabel di df_day")
corr_day = df_day.corr()
fig3, ax3 = plt.subplots(figsize=(15, 10))
sns.heatmap(corr_day, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax3)
plt.title('Heatmap Korelasi Antar Variabel di df_day')
st.pyplot(fig3)

# Korelasi Antar Variabel di df_hour
st.header("Korelasi Antar Variabel di df_hour")
corr_hour = df_hour.corr()
fig4, ax4 = plt.subplots(figsize=(15, 10))
sns.heatmap(corr_hour, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax4)
plt.title('Heatmap Korelasi Antar Variabel di df_hour')
st.pyplot(fig4)

# Pertanyaan 1: Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda
st.header("Pertanyaan 1: Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda")
weather_counts = df_day.groupby('weathersit')['cnt'].mean().reset_index()
weather_counts.columns = ['Weather Situation', 'Average Count']
weather_conditions = {
    1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
    3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
    4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'
}
weather_counts['Weather Situation'] = weather_counts['Weather Situation'].map(weather_conditions)
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.barplot(x='Weather Situation', y='Average Count', data=weather_counts, ax=ax5)
ax5.set_title('Average Number of Bike Rentals by Weather Condition')
ax5.set_xlabel('Weather Condition')
ax5.set_ylabel('Average Number of Bike Rentals')
plt.xticks(rotation=45)
st.pyplot(fig5)

# Pertanyaan 2: Tren Peminjaman Sepeda Berdasarkan Hari dalam Seminggu dan Jam dalam Sehari
st.header("Pertanyaan 2: Tren Peminjaman Sepeda Berdasarkan Hari dalam Seminggu dan Jam dalam Sehari")
# Analisis Berdasarkan Hari dalam Seminggu
weekday_counts = df_hour.groupby('weekday')['cnt'].mean().reset_index()
weekday_counts.columns = ['Weekday', 'Average Count']
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.barplot(x='Weekday', y='Average Count', data=weekday_counts, ax=ax6)
ax6.set_title('Average Number of Bike Rentals by Day of the Week')
ax6.set_xlabel('Day of the Week')
ax6.set_ylabel('Average Number of Bike Rentals')
st.pyplot(fig6)
# Analisis Berdasarkan Jam dalam Sehari
hour_counts = df_hour.groupby('hr')['cnt'].mean().reset_index()
hour_counts.columns = ['Hour', 'Average Count']
fig7, ax7 = plt.subplots(figsize=(10, 5))
sns.lineplot(x='Hour', y='Average Count', data=hour_counts, ax=ax7)
ax7.set_title('Average Number of Bike Rentals by Hour of the Day')
ax7.set_xlabel('Hour of the Day')
ax7.set_ylabel('Average Number of Bike Rentals')
st.pyplot(fig7)

# Menampilkan DataFrame untuk Eksplorasi Lanjutan
st.header("DataFrame untuk Eksplorasi Lanjutan")
option = st.selectbox(
    'Pilih DataFrame yang ingin Anda lihat:',
    ('df_day', 'df_hour')
)
if option == 'df_day':
    st.write(df_day)
else:
    st.write(df_hour)

# Copyright
st.markdown("""
    ---
    © 2024 Naufal Rafid Muhammad Faddila
""")
