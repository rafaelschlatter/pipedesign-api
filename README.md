# Pipedesign-ml

This is a sample python flask API that is hosted on Microsoft Azure app service (free tier). The API consists of one method, `predict()` which atm returns the length of a parameter in the json file.

## Setup
Azure app service on linux needs a **requirements.txt** file for all dependencies except flask. A pipenv workflow probably fails (not tested).

Clone the repo and create a virtual environment with `virutalenv`:
````bash
git clone https://github.com/rafaelschlatter/pipedesign-ml.git
cd pipedesign-ml
virtualenv pipedesign-ml
````

Activate it and install dependencies:
````bash
source pipedesign-ml/bin/activate
pip install -r requirements.txt
````

## Usage in client application
The following code demonstrates usage with python 3:

````python
import requests

url = "http://rschlatter.azurewebsites.net/pipedesignml/api/predict"
r = requests.post(url, json={'number': 2})

print(r.json())
````

This should display the following response:
````javascript
{'prediction': 4}
````
