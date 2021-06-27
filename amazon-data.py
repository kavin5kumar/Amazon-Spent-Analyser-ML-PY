# getting data from Pandas
# importing Pandas
import pandas as pd

# importing file and visit only top 5 data from the file
df = pd.read_csv('amazon-orders.csv')
df.head()

# full size of our data set
df.shape

# Cleaning the Data
df = df.fillna(0)
df.head()

df["Total Charged"] = df["Total Charged"].str.replace('$', '').astype(float)
df.head()

# Calculating the Total Amount of Money Spent on Amazon
df["Total Charged"].sum()

# Calculating Average Spend on Amazon
df["Total Charged"].mean()

# Calculating Median Spend on Amazon
df["Total Charged"].median()

# Calculating Smallest Purchase on Amazon
df["Total Charged"].max()

# Calculating Smallest Purchase on Amazon
df["Total Charged"].min()

# Finding out How Much Have I Paid in Sales Tax

# Cleaning the Data
df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df.head()

# total amount of money paid in tax
df["Tax Charged"].sum()

# overall tax rate
df["Tax Charged"].sum() / df["Total Charged"].sum()

# Analyzing Amazon Spending Over Time

# convert order date to a datetime data type
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()

# bar graph 
df.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize = (20, 10))

# grouping by how much was spent each day
daily_orders = df.groupby('Order Date').sum()["Total Charged"]
daily_orders.head()

# making this the bar graph
daily_orders.plot.bar(figsize=(20,10), color='#61D199')