import pandas as pd
from faker import Faker
import random

# Initialize faker
fake = Faker()

# Number of dummy data entries
num_entries = 1000

# Generate Produk data
produk_data = {
    "ID_Produk": [fake.uuid4() for _ in range(num_entries)],
    "nama_produk": [fake.word() for _ in range(num_entries)],
    "kategori_produk": [fake.word() for _ in range(num_entries)],
    "harga_produk": [round(random.uniform(10, 1000), 2) for _ in range(num_entries)],
    "tanggal_rilis": [fake.date_this_decade() for _ in range(num_entries)],
    "penjualan_unit": [random.randint(1, 1000) for _ in range(num_entries)],
    "margin_keuntungan": [round(random.uniform(1, 100), 2) for _ in range(num_entries)]
}

# Generate Pelanggan data
pelanggan_data = {
    "ID_Pelanggan": [fake.uuid4() for _ in range(num_entries)],
    "nama_pelanggan": [fake.name() for _ in range(num_entries)],
    "alamat_pelanggan": [fake.address() for _ in range(num_entries)],
    "email_pelanggan": [fake.email() for _ in range(num_entries)],
    "no_telepon_pelanggan": [fake.phone_number() for _ in range(num_entries)]
}

# Generate Karyawan data
karyawan_data = {
    "ID_Karyawan": [fake.uuid4() for _ in range(num_entries)],
    "nama_karyawan": [fake.name() for _ in range(num_entries)],
    "departemen_karyawan": [fake.job() for _ in range(num_entries)],
    "jabatan_karyawan": [fake.job() for _ in range(num_entries)],
    "gaji_karyawan": [round(random.uniform(3000, 10000), 2) for _ in range(num_entries)]
}

# Generate Toko data
toko_data = {
    "ID_Toko": [fake.uuid4() for _ in range(num_entries)],
    "nama_toko": [fake.company() for _ in range(num_entries)],
    "alamat_toko": [fake.address() for _ in range(num_entries)],
    "email_toko": [fake.company_email() for _ in range(num_entries)],
    "no_telepon_toko": [fake.phone_number() for _ in range(num_entries)]
}

# Generate Penjualan data
penjualan_data = {
    "ID_Penjualan": [fake.uuid4() for _ in range(num_entries)],
    "ID_Produk": [random.choice(produk_data['ID_Produk']) for _ in range(num_entries)],
    "ID_Toko": [random.choice(toko_data['ID_Toko']) for _ in range(num_entries)],
    "tanggal_penjualan": [fake.date_this_year() for _ in range(num_entries)],
    "kuantitas_penjualan": [random.randint(1, 100) for _ in range(num_entries)],
    "harga_penjualan": [round(random.uniform(20, 200), 2) for _ in range(num_entries)],
    "wilayah_penjualan": [fake.city() for _ in range(num_entries)]
}

# Convert to DataFrame
produk_df = pd.DataFrame(produk_data)
pelanggan_df = pd.DataFrame(pelanggan_data)
karyawan_df = pd.DataFrame(karyawan_data)
toko_df = pd.DataFrame(toko_data)
penjualan_df = pd.DataFrame(penjualan_data)

# Save to CSV
produk_df.to_csv('produk.csv', index=False)
pelanggan_df.to_csv('pelanggan.csv', index=False)
karyawan_df.to_csv('karyawan.csv', index=False)
toko_df.to_csv('toko.csv', index=False)
penjualan_df.to_csv('penjualan.csv', index=False)
