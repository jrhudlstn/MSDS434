from sklearn.model_selection import train_test_split
import pandas as pd
import os

dirname = os.path.dirname(__file__)


print("Reading data from German")
data_frame=pd.read_csv("germanCredit.csv")

print("Spliting data in train and test")
train, test = train_test_split(data_frame, test_size=0.2)

print("Storing train and test data")
train.to_csv("trainData.csv",index=False)
test.to_csv("testData.csv",index=False)
