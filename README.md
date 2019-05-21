# Pipedesign-ml

This is a sample python flask API that is hosted on Microsoft Azure app service (free tier). The API consists of one method, `predict()` which returns the double of the given number.

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
