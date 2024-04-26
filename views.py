from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import LabelEncoder 

class PredictView(APIView): 
    def post(self, request): 
        # Extract input values from request 
        v1 = request.data.get('v1') 
        v2 = request.data.get('v2') 
        v3 = request.data.get('v3') 
        v4 = request.data.get('v4') 
        v5 = request.data.get('v5') 
        v6 = request.data.get('v6') 
        v7 = request.data.get('v7')
         
        # Check if any value is None 
        if None in [v1, v2, v3, v4, v5,v6,v7]: 
            return Response({'error': 'One or more values are missing'}, status=status.HTTP_400_BAD_REQUEST) 
 
        # Convert values to float 
        try: 
            v1 = float(v1) 
            v2 = float(v2) 
            v3 = float(v3) 
            v4 = float(v4) 
            v5 = float(v5) 
            v6 = float(v6) 
            v7 = float(v7) 
        except ValueError: 
            return Response({'error': 'One or more values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST) 
 
        # Load the trained model and preprocess data 
        data = pd.read_csv("C:\\Users\\sugan\\Downloads\\Used_Bikes.csv\\Used_Bikes.csv")
       
        data["price"] = pd.to_numeric(data["price"])

        label_encoder = LabelEncoder()
        data['bike_name'] = label_encoder.fit_transform(data['bike_name'])
        data['owner'] = label_encoder.fit_transform(data['owner'])
        data['city'] = label_encoder.fit_transform(data['city'])
        data['brand'] = label_encoder.fit_transform(data['brand'])
        
        features=['bike_name',	'city',	'kms_driven'	,'owner'	'age','power';	'brand']
        X =data[features]
        y = data['price']

        model = LinearRegression()
        model.fit(X,y)

        # Make predictions 
        out = model.predict(np.array([v1, v2, v3, v4, v5,v6,v7]).reshape(1, -1)) 
        prediction = int(out[0]) 
 
        # Return the prediction 
        return Response({'prediction':prediction}, status=status.HTTP_200_OK)
