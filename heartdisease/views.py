from unicodedata import numeric
from django.shortcuts import render
from joblib import load
import numpy as np
model=load('./savedmodel/model.joblib')

def home(request):
    return render(request,'index.html')


def predict(request):
    age=request.GET['age']
    sex=request.GET['sex']
    cp=request.GET['cp']
    trestbps=request.GET['trestbps']
    chol=request.GET['chol']
    fbs=request.GET['fbs']
    restecg=request.GET['restecg']
    thalach=request.GET['thalach']
    exang=request.GET['exang']
    oldpeak=request.GET['oldpeak']
    slope=request.GET['slope']
    ca=request.GET['ca']
    thal=request.GET['thal']

    a=(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    b = np.array(a, dtype=float) ##because oldpeak is a float so we change whole in in float instead of this 
                                ##model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    b=b.reshape(1,-1)
    pred=model.predict(b)
    if  pred==1:
       pred='Patient Has Heart disease'
    else:
        pred='Patient does not have Heart disease'   
    return render(request,'index.html',{'result':pred})