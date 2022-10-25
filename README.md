# PARDON

Pardon is a Python library developed as a machine learning (ML) and data transformation accelerator, to rapidly prepare data as well as test and deploy supervised ML models, by massively reducing the amount of code required during development.

The library can be used to perform data cleansing and transformation, as well as model and feature selection, data visualisations, and prediction auditing. Data can be quickly prepared for use with ML algorithms, and all data transformations are recorded in a 'script'. This 'script' is then automatically applied to data prior to predictions, which ensures data consistency, transparency, and removes the need for multi-stage data engineering while reducing the chances of error.

The intention of this library is not to replace or automate the work of a data scientist, but to enable integration work to begin early by rapidly deploying a working machine learning model. This then allows the data science work to be completed in parallel, with the final model being deployed on completion.

The pardon library functionality includes:
•	Data transformation
•	Data cleansing
•	Feature selection
•	Feature engineering
•	Model selection
•	Class balancing
•	Prediction auditing
•	Principal Component Analysis
•	Data scaling
•	Data encoding
•	Sentiment analysis
•	Hyperparameter tuning
•	Model “explainability”
•	Model performance metrics
•	Model training, testing and validation
•	Identifying data outliers
•	Testing model output in a REST API
•	Data visualisation
•	Use unsupervised learning to cluster data


## Installation

The easiest way to install and use pardon is to pip install using pip or pip using the latest pardon package whl file
```bash
pip install pardon
```
```bash
pip install pardon-1.0.0-py3-none-any.whl
```

## Usage

```python
import pardon

# create a new ML Data object. The minimum requirements are a data file or data stream, and the name of the column you're trying to predict.
paml = pardon.Pardon(data='\\your\\specified\\directory\\data_file.csv', target='column_name_to_predict')

# rapid ml will perform the following steps by default:
# -> 1. Perform the minimum required data cleansing and transformation to prepare your data for model training.
# -> 2. Trains multiple models using the data and selects the best performing model.
# -> 3. Where applicable, display a summary of the model performance.
# -> 4. Save the model as a .pkl file to the location specified. You must ensure the filename is a .pkl file.
# -> 5. Display the output scores of all the models tested.
paml.rapid_ml(model_fullpath='\\your\\specified\\directory\\your_model_name.pkl')

# you can run a test on the localhost to see the API output
pardon.TestAPI(model_fullpath='\\your\\specified\\directory\\your_model_name.pkl')
```

## Contributing
For changes, please contact pardonaccelerator@gmail.com to discuss your amendments or requirements.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
