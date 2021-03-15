# MSDS434
MSDS434 course assignment
The data set comes from Googles BigQuery data sets https://cloud.google.com/bigquery/public-data/ and is uploaded to the Google Cloud Storage where the data is manipulated with SQL in Google BigQuery for predictions. The data set is entitled German Credit Data.
The data was also run by spliting the data into train/valid/test, as 80/20 train/test and also tried cross-validation technique to stretch out the train into train/validate. 

![image](https://user-images.githubusercontent.com/6859309/111093459-f7493480-8506-11eb-902d-c82df615595b.png)

This app is deployed as a web application that runs on App Engine, to predict from BigQuery and return a result to the user. 
![image](https://user-images.githubusercontent.com/6859309/111092165-4ab98380-8503-11eb-98dd-f654da473c95.png)
The user enters an input in the text box of the home application page from this published url : https://msds434-webapp.uc.r.appspot.com/ 
![image](https://user-images.githubusercontent.com/6859309/111096239-121ea780-850d-11eb-9021-5b386b75a194.png)

Examples of the SQL data Queries needed in this project that is not included in the GitHub repo fils are below
1. The first testing of data requires a trainData.csv and testData.csv in a random sample modeling for rows from the allData.csv file each of which are in the GitHub repo. 

CREATE TABLE cbergman.germanCreditData.testData AS
SELECT *
FROM `cbergman.germanCreditData.allData`
WHERE MOD(ABS(FARM_FINGERPRINT(CAST(uniqueID AS STRING))), 5) = 0;

CREATE OR REPLACE TABLE cbergman.germanCreditData.trainData AS
SELECT *
FROM `cbergman.germanCreditData.allData`
WHERE NOT uniqueID IN (
  SELECT DISTINCT uniqueID FROM `cbergman.germanCreditData.testData`
);

2. The tables are uploaed BigQuery and R-code, R-Studio was used to do EDA on the sets and the results are in in the next figure below

![image](https://user-images.githubusercontent.com/6859309/111098657-f79afd00-8511-11eb-89bc-d509f5b9fdfd.png)



