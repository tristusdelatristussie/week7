# Employee Churn Prediction

This repository contains a project to predict employee churn. The project uses a dataset of employee data to train two machine learning models: a random forest classifier and an XGBoost classifier. The models are then deployed as a Flask API.

## Summary

A company wants to know how to predict which employees are likely to leave. The dataset contains the following features:

| Feature | Type |
|---|---|
| Education | Object |
| JoiningYear | Integer |
| City | Object |
| PaymentTier | Integer |
| Age | Integer |
| Gender | Object |
| EverBenched | Object |
| ExperienceInCurrentDomain | Integer |
| LeaveOrNot | Integer |

## Methodology

The project follows the following methodology:
All preprocessing, training and tuning and saving models is in eda_tune_train.py 
(no necessary needed to launch it again, models are ever in container)


1. **EDA**

The first step is to perform exploratory data analysis (EDA) on the dataset. This includes checking for missing values, outliers, and data types.

2. **Data Preprocessing**

The next step is to preprocess the data. This includes encoding categorical features and splitting the data into train and test sets.

3. **Model Training**

The models are then trained using the train set. The random forest classifier is trained using the `sklearn.ensemble.RandomForestClassifier()` class. The XGBoost classifier is trained using the `xgboost.XGBClassifier()` class.

4. **Model Evaluation**

The models are evaluated using the test set. The accuracy, precision, and recall of each model are calculated.

5. **Model Deployment**

The models are then deployed as a Flask API. The API can be used to predict whether an employee is likely to leave.

## Usage

To use the API, you can use the following command:


curl -X POST -H "Content-Type: application/json" -d '{"education": "Master's degree", "joining_year": 2022, "city": "Paris", "payment_tier": 3, "age": 35, "gender": "Male", "ever_benched": "Yes", "experience_in_current_domain": 5}' localhost:9797/predict
```

The API will return a JSON response with the predicted probability that the employee will leave.

## How to use the app

To use the app, you will need to have Docker installed.

1. Clone the repository:

```
git clone https://github.com/[YOUR_USERNAME]/employee-churn-prediction.git
```

2. Change into the repository directory:

```
cd employee-churn-prediction
```

3. Build the image:

```
docker build -t api_flask .
```

4. Run the container:

```
docker run api_flask
```

5. Query the API:

```
pipenv python request_api.py


This will run the `request_api.py` script, which will query the API and print the response.

## References

* [EDA](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
* [Random forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
* [XGBoost](https://xgboost.readthedocs.io/en/stable/)

