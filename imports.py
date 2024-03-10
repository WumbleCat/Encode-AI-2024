import pickle
import faker
from scipy.stats import skewnorm
import pandas as pd
from datetime import date, datetime, timedelta
import numpy as np

from sklearn.ensemble import IsolationForest
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
