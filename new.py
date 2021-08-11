# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 00:15:08 2021

@author: HP
"""

import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "gWOW3Y6cMzSVB21HbLMa6CXZ13U6qciPnZdESOZOKF8a"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Cement","Blast Furnace Slag","Fly Ash","Water","Superplasticizer","Coarse Aggregate","Fine Aggregate","Age","Concrete compressive strength"]], "values": [[540,0,0,162,2.5,1040,676,28 ]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/734beb40-93bb-4135-9b9f-6ce77fe5aadc/predictions?version=2021-08-03', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json()['predictions'][0]['values'][0][0])