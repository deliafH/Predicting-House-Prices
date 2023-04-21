import joblib
import os
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

model = joblib.load("C:\\Users\\Quang Huy\\OneDrive\\Máy tính\\TEST\\model.sav")


# Create your models here.
class IndexView(View):
    template_name = 'index.html'

    def __init__(self, **kwargs):
        super(IndexView).__init__(**kwargs)

    def get(self, request):
        context = {
            'image_url': os.path.join('/static', 'diamond.png')
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        val1 = request.POST['value1']
        val2 = request.POST['value2']
        val3 = request.POST['value3']
        val4 = request.POST['value4']
        val5 = request.POST['value5']
        val6 = request.POST['value6']
        val7 = request.POST['value7']
        val8 = request.POST['value8']
        val9 = request.POST['value9']

        value = np.array([[val1, val2, val3, val4, val5, val6, val7, val8, val9]], dtype=float)
        answer = model.predict(value)
        data = {
            'answer': str(answer[0])
        }
        return JsonResponse(data)
