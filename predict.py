from imports import *


def identify(kwargs):
  df = pd.read_csv("./synthdata.csv")
  label_encoders = {}
  for col in ["Customer ID", "Merchant ID", "Merchant Region", "Category"]:
    label_encoders[col] = LabelEncoder()
    kwargs[col] = label_encoders[col].fit_transform(df[col])[0]
  
  print(kwargs)
  x_vals = pd.DataFrame(kwargs, index=[0])
  with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

  return model.predict(x_vals)[0]

if __name__ == '__main__':
  is_it_fraud = identify({"Customer ID": "123", "Merchant ID": "321", "Merchant Region": "Rural", "Category": "Luxury", "Amount": 0.213})
  print(is_it_fraud)
