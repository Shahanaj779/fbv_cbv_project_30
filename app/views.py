from django.shortcuts import render

# Create your views here.
from django.views.generic import View

def fbv_first(request):
    return render(request,'fbv_first.html')

class cbv_first(View):
    def get(self,request):
        return render(request,'cbv_first.html')



