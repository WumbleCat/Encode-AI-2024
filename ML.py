from imports import *


df = pd.read_csv("./synthdata.csv")
label_encoders = {}
for col in ["Customer ID", "Merchant ID", "Merchant Region", "Category"]:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

X = df[["Customer ID", "Merchant ID", "Merchant Region", "Category", "Amount"]]
y = df["Is_Fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
