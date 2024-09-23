import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
avg_order_df = pd.read_csv('Data/avg_order_value_q3_2018.csv')
revenue_product_df = pd.read_csv('Data/combined_revenue_product_sales.csv')
review_df = pd.read_csv('Data/low_review_categories.csv')
payment_df = pd.read_csv('Data/payment_type_distribution_q3_2018.csv')
rfm_df = pd.read_csv('Data/rfm_data.csv')

sns.set(style="whitegrid")

# Filter section
st.sidebar.header("Filter Options")
selected_category = st.sidebar.multiselect("Select Product Category", revenue_product_df['product_category_name'].unique())

# Apply filters
if selected_category:
    revenue_product_df = revenue_product_df[revenue_product_df['product_category_name'].isin(selected_category)]


    # Filter untuk memilih rentang tanggal
    st.subheader('Filter by Date Range')
    start_date = st.date_input('Start date', value=pd.to_datetime('2018-01-01'))
    end_date = st.date_input('End date', value=pd.to_datetime('2018-12-31'))

    # Konversi kolom tanggal (misalnya 'quarter') ke tipe datetime
    revenue_product_df['quarter'] = pd.to_datetime(revenue_product_df['quarter'])

    # Filter data berdasarkan rentang tanggal yang dipilih
    filtered_revenue_product_df = revenue_product_df[(revenue_product_df['quarter'] >= pd.to_datetime(start_date)) & (revenue_product_df['quarter'] <= pd.to_datetime(end_date))]

# Plot total revenue per quarter
st.subheader('Total Revenue per Quarter')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='quarter', y='price_revenue', data=revenue_product_df, palette='Blues_d', ax=ax)
ax.set_title('Total Revenue per Quarter')
ax.set_xlabel('Quarter')
ax.set_ylabel('Revenue (in millions)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Plot top product categories by sales
st.subheader('Top 10 Product Categories by Sales')
fig, ax = plt.subplots(figsize=(10, 6))
top_product_categories = revenue_product_df.head(10)
sns.barplot(x='price_sales', y='product_category_name', data=top_product_categories, palette='Greens_d', ax=ax)
ax.set_title('Top 10 Product Categories by Sales')
ax.set_xlabel('Total Sales (in millions)')
ax.set_ylabel('Product Category')
st.pyplot(fig)

# Plot payment type distribution in Q3 2018
st.subheader('Payment Type Distribution in Q3 2018')
fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(payment_df['percentage'], labels=payment_df['payment_type'], autopct='%1.1f%%', colors=sns.color_palette("Spectral", n_colors=5))
ax.set_title('Payment Type Distribution in Q3 2018')
st.pyplot(fig)

# Plot average review scores per product category
st.subheader('Average Review Scores per Product Category')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='review_score', y='product_category_name', data=review_df.sort_values(by='review_score', ascending=False).head(), palette='Oranges_d', ax=ax)
ax.set_title('Average Review Scores per Product Category')
ax.set_xlabel('Average Review Score')
ax.set_ylabel('Product Category')
ax.axvline(x=4, color='red', linestyle='--')
st.pyplot(fig)

# Plot average order value for each payment type
st.subheader('Average Order Value per Payment Type in Q3 2018')
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='payment_value', y='payment_type', data=avg_order_df.sort_values(by='payment_value', ascending=False), palette='Purples_d', ax=ax)
ax.set_title('Average Order Value per Payment Type in Q3 2018')
ax.set_xlabel('Average Order Value')
ax.set_ylabel('Payment Type')
st.pyplot(fig)

# Plot distributions of Recency, Frequency, and Monetary
st.subheader('Recency, Frequency, and Monetary Distributions')
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

sns.histplot(rfm_df['Recency'], kde=True, ax=ax1, color='blue')
ax1.set_title('Recency Distribution')
ax1.set_xlabel('Days Since Last Purchase')

sns.histplot(rfm_df['Frequency'], kde=True, ax=ax2, color='green')
ax2.set_title('Frequency Distribution')
ax2.set_xlabel('Number of Purchases')

sns.histplot(rfm_df['Monetary'], kde=True, ax=ax3, color='red')
ax3.set_title('Monetary Distribution')
ax3.set_xlabel('Total Spent (in $)')

plt.tight_layout()
st.pyplot(fig)

# Plot customer segments based on RFM
st.subheader('Customer Segments Distribution')
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='Customer_Segment', data=rfm_df, order=rfm_df['Customer_Segment'].value_counts().index, palette='Set2', ax=ax)
ax.set_title('Customer Segments Distribution')
ax.set_xlabel('Customer Segment')
ax.set_ylabel('Count of Customers')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Ensure F_score, R_score, and M_score are numeric
rfm_df['F_score'] = pd.to_numeric(rfm_df['F_score'], errors='coerce')
rfm_df['R_score'] = pd.to_numeric(rfm_df['R_score'], errors='coerce')
rfm_df['M_score'] = pd.to_numeric(rfm_df['M_score'], errors='coerce')

# Drop missing values
rfm_df = rfm_df.dropna(subset=['F_score', 'R_score', 'M_score'])

# Create pivot table for RFM heatmap
rfm_heatmap = rfm_df.pivot_table(index='F_score', columns='R_score', values='M_score', aggfunc='mean')

# Plot heatmap
st.subheader('RFM Heatmap: Mean M Scores for Each F and R Group')
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(rfm_heatmap, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={'label': 'Mean Monetary Score'}, ax=ax)
ax.set_title('RFM Heatmap: Mean M Scores for Each F and R Group')
ax.set_xlabel('Recency Score')
ax.set_ylabel('Frequency Score')
st.pyplot(fig)

# Kesimpulan
st.markdown("""
### Kesimpulan:

**Peningkatan Pendapatan:**
- Untuk mencapai peningkatan total pendapatan sebesar 15% dalam tiga bulan ke depan, perusahaan dapat fokus pada kategori produk yang paling laris seperti *beleza_saude*, *relogios_presentes*, dan *cama_mesa_banho*. 
- Strategi diskon, promosi, atau peluncuran produk baru dalam kategori ini dapat meningkatkan pendapatan secara signifikan. 
- Selain itu, memperbaiki performa di kuartal dengan penurunan, seperti Q3 2018, dapat dilakukan melalui promosi yang lebih agresif atau peluncuran produk baru.

**Peningkatan Skor Ulasan:**
- Kategori dengan skor ulasan di bawah 4, seperti *telefonia_fixa* dan *artes*, memerlukan perhatian.
- Perbaikan kualitas produk, peningkatan layanan purna jual, atau komunikasi yang lebih baik dengan pelanggan dapat membantu meningkatkan skor ulasan rata-rata sebesar 0,5 poin dalam tiga bulan ke depan.

**Meningkatkan Penggunaan Pembayaran Elektronik:**
- Untuk meningkatkan penggunaan pembayaran elektronik sebesar 20%, perusahaan dapat menawarkan insentif atau diskon khusus bagi pengguna *debit card* dan *voucher*, karena metode pembayaran ini masih kurang populer dibandingkan kartu kredit. 
- Edukasi pelanggan mengenai kenyamanan dan kecepatan metode pembayaran elektronik juga dapat menjadi kunci.
""")
