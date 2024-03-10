# Encode-AI-2024

-- Machine Learning Documentation --

imports.py = a list of all the modules and libraries used
datagen.py = code to generate synthetic data (fake data)
synthdata.csv = the exported fake data in a csv format
ML.py = the machine learning code (XGboost) to train on the data
model.pkl = the exported trained model
predict.py = contains code to predict individual data
__pycache__ = ignore this, a python thing

-- HOW TO USE --

if synthdata.csv doesn't exist. Open datagen.py and run the script
if model.pkl doesn't exist. Open ML.py and run the script (only if synthdata already exist)
if both exist, on your code, do:

"from predict import identify
"prediction = identify(dict)

dict = {"Customer ID": data1, "Merchant ID": data2, "Merchant Region": data3, "Category": data4, "Amount": data5}
prediction = 0 (not fraudulent), 1 (fraudulent)

