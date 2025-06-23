
import pandas as pd

# Load dataset
df = pd.read_csv('unilever_channel_delivery_data.csv')

# Convert date columns to datetime
df['Expected Delivery Date'] = pd.to_datetime(df['Expected Delivery Date'])
df['Actual Delivery Date'] = pd.to_datetime(df['Actual Delivery Date'])

# Calculate delay (again, for clarity)
df['Delay (Days)'] = (df['Actual Delivery Date'] - df['Expected Delivery Date']).dt.days

# Summary 1: Delay by Channel Partner
delay_by_partner = df.groupby('Channel Partner')['Delay (Days)'].agg(['mean', 'count']).reset_index()
print("Delay Summary by Channel Partner:")
print(delay_by_partner)

# Summary 2: Delay by City
delay_by_city = df.groupby('City')['Delay (Days)'].agg(['mean', 'count']).reset_index()
print("\nDelay Summary by City:")
print(delay_by_city)

# Optional: Save summaries to CSV
delay_by_partner.to_csv('delay_by_partner.csv', index=False)
delay_by_city.to_csv('delay_by_city.csv', index=False)
