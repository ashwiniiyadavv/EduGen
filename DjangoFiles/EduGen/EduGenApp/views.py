from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REACT_BUILD_DIR = os.path.join(BASE_DIR, 'frontend')

# Create your views here.
def index(request):
    if request.method !="POST":
        return HttpResponse("This is Primary Page to take prompt")
    else:
        #Take the prompt from POST Body
        #Call Function or API ( To generate Video )
        #Meanwhile Display Animation 
        #Return Video to Home Page (Index) that means we have to pass video to same template ig
        return HttpResponse("This is your Video")


class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join('frontend/build/index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse("React build not found", status=501)


  

# def index(request):
#       return render(request, os.path.join(REACT_BUILD_DIR, 'index.html'))

def index(request):
    if request.method!='POST':
        return render(request,'index.html')
    else:
        
        concept = request.POST.get('concept')
        return render(request, 'index.html', {'concept': concept})
def feedback(request):
    if request.method=="POST":
        return HttpResponse(f"your Feedback: {request.POST['feedback']}",status=200)
    else:
        return HttpResponse(f"This is feedback posting page")