from imports import *

fake = faker.Faker()
time_start = datetime.strptime("2024-01-01", '%Y-%m-%d')
time_end = datetime.strptime("2025-01-01", '%Y-%m-%d')
time_now = time_start
total_days = (time_end - time_start).days

initial_cust = 1000
current_cust = initial_cust

Region = ["Rural", "Urban"]
Category = ["Common", "Digital", "Luxury", "Specialty"]

cust_hist = []
merch_hist = []

df = {
    "Date": [],
    "Customer ID": [],
    "Merchant ID": [],
    "Merchant Region": [],
    "Amount": [],
    "Category": []
}

def gen_inc(amount):
    var = 0.05 * np.random.random() + 0.01
    return (var/(amount*var)) * np.random.random() + (var/(amount*var))

def add_row(data, new_row):
    for key in new_row:
        if key in data:
            data[key].append(new_row[key])

for i in range(total_days):
    cust_buy = np.random.randint(0, current_cust)
    for j in range(cust_buy):
        if j >= len(cust_hist):
            cust_hist.append(fake.uuid4())
            merch_hist.append(fake.uuid4())
            
        reg = np.random.choice(Region)
        
        if reg == "Rural":
            probs = skewnorm.rvs(a = np.random.random(), size=4)
        else:
            probs = skewnorm.rvs(a = -1 * np.random.random(), size=4)
            
        probs = probs - min(probs) 
        probs = probs / sum(probs)
        
        cat = np.random.choice(Category, p=probs)
        mu = 0.001 + 0.001 * (Region.index(reg) * 0.4 + Category.index(cat) * 0.15)
        sigma = 0.1*np.random.random() + 1
        
        new_row = {
        "Date": time_now,
        "Customer ID": np.random.choice(cust_hist),
        "Merchant ID": np.random.choice(merch_hist),
        "Merchant Region": reg,
        "Category": cat,
        "Amount": abs(np.random.normal(mu, sigma))
        }
        
        add_row(df, new_row)
    time_now = time_now + timedelta(1)
    current_cust = current_cust + round(gen_inc(current_cust) * current_cust)

df = pd.DataFrame(df)

df['Date'] = pd.to_datetime(df['Date'])

amount_threshold = df['Amount'].quantile(0.95)  
df['High_Amount'] = (df['Amount'] >= amount_threshold).astype(int)
df['Transaction_Count'] = df.groupby(['Customer ID', df['Date'].dt.date])['Date'].transform('count')

transaction_count_threshold = df['Transaction_Count'].quantile(0.95)
df['Frequent_Transactions'] = (df['Transaction_Count'] >= transaction_count_threshold).astype(int)

features = df[['Amount', 'High_Amount', 'Transaction_Count', 'Frequent_Transactions']]
iso_forest = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
iso_forest.fit(features)

df['Is_Fraud'] = iso_forest.predict(features)
df['Is_Fraud'] = df['Is_Fraud'].apply(lambda x: 1 if x == -1 else 0)
df.drop(["High_Amount", "Transaction_Count", "Frequent_Transactions"], axis=1, inplace=True)

df.to_csv("./synthdata.csv")
