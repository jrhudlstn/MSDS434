this project began at https://github.com/jrhudlstn/MSDS434_WebApp circleCI. git Actions
# MSDS434
MSDS434 course assignment
The data set comes from Googles BigQuery data sets https://cloud.google.com/bigquery/public-data/ and is uploaded to the Google Cloud Storage where the data is manipulated with SQL in Google BigQuery for predictions. The data set is entitled German Credit Data. This is to predict fraud in an application process. 
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

2. The tables are uploaed BigQuery and R-code, R-Studio was used to do EDA on the sets and the results are in in the next figure below![image](https://user-images.githubusercontent.com/6859309/111098761-26b16e80-8512-11eb-8413-b1eb2a524244.png)

3. The check or test to determine if the working query resulted in a responed query is the SQL 
SELECT count (distinct uniqueID)
FROM `cbergman.germanCreditData.allData`
where response = 2;  

With a result 
![image](https://user-images.githubusercontent.com/6859309/111099239-1352d300-8513-11eb-962c-3e98f6526995.png)

4. In constructing the fraud model is the requirement for catching the most fraud in money automatically, and second to choose an algorithm that 'you' believe will be a good predictor, in this case  API method Logistic Regression is chosen.  The SQL used to test this model and examine if it fits the train and test data is 
# Create a base model as 
CREATE OR REPLACE MODEL cbergman.germanCreditData.baseModel OPTIONS(input_label_cols=['response'], model_type='logistic_reg') AS 
SELECT * EXCEPT (uniqueID) 
FROM `cbergman.germanCreditData.trainData`;
# To fit the model on the train data
SELECT *
FROM ML.EVALUATE(MODEL `cbergman.germanCreditData.baseModel`, 
(
  SELECT * EXCEPT (uniqueID)
  FROM `cbergman.germanCreditData.trainData`);
# To test the models fit on the test data
SELECT *
FROM ML.EVALUATE(MODEL `cbergman.germanCreditData.baseModel`, 
(
  SELECT * EXCEPT (uniqueID)
  FROM `cbergman.germanCreditData.testData`);

Next Steps:
The next steps in this analysis is to use algorithms to BigQuery ML: multi-class Logistic Regression and Tensorflow.

References

Christy Bergman. Lessons Learned Using Google Cloud BigQuery ML. Start-to-finish ML demo using German Credit Data. Nov 6, 2019. Retrieved from https://towardsdatascience.com/lessons-learned-using-google-cloud-bigquery-ml-dfd4763463c 


