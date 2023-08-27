from django.shortcuts import render
from .forms import CForm
import numpy as np
import tflite_runtime.interpreter as tflite
interpreter = tflite.Interpreter(model_path=r'/home/TejaH/m.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
floating_model = input_details[0]['dtype']

def calculate(v):
    interpreter.set_tensor(input_details[0]['index'], np.array(v,dtype=floating_model))
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

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
    u=str(int(calculate([[v]])))
  else:
   u="error"
 return render(request,'predict_score/prediction.html',{'input':u,'form':info})

def index(request):
 return render(request, 'predict_score/index.html')
