from django.shortcuts import render
from .forms import CForm
import pandas as pd
import statsmodels.api as sm
import numpy as np

def calculate(v):
 df=pd.read_csv("predict_score\score.csv")
 x=df['Hours']
 y=df['Scores']
 x=sm.add_constant(x)
 model=sm.OLS(y,x).fit()
 return model.predict(np.array([1,v]))

def prediction(request):
 u='this is output'
 info = CForm()
 if(request.method=='POST'):
  info=CForm(request.POST)
  if(info.is_valid()):
   u=info.cleaned_data.get('data')
   f=0
   try:
    v=float(u)
    if(v<0 or v>10):
     u="Please enter a number between 0 and 10"
     f=1
   except:
    u="Invalid number"
    f=1
   if(f==0):
    u=str(int(calculate(v)))
  else:
   u="error"
 return render(request,'predict_score/prediction.html',{'input':u,'form':info})

def index(request):
 return render(request, 'predict_score/index.html')
