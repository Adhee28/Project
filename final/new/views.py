from django.shortcuts import render,redirect
from new.forms import FeedbackForm,DataForm2
from new.models import Feedback2,DataModel
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'About.html')

def data(request):
    if request.method == "POST":
        form=DataForm2(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                    pass
    else:
        form=DataForm2()
    return render (request,'Data.html',{'form':form})

def ViewData(request):
    dataform=DataModel.objects.all()
    return render(request,'ViewData.html',{'dataform':dataform})

def deletedata(request,id):
     dataform=DataModel.objects.get(id=id)
     dataform.delete()
     return redirect ('/ViewData')

def editdata(request,id):
     dataform=DataModel.objects.get(id=id)
     return render(request,'editdata.html',{'dataform':dataform})

def Updatedata(request,id):
     dataform=DataModel.objects.all()
     return render(request,'Updatedate.html',{'dataform':dataform})
    
def dd(request):
    return render(request,'Disease Description.html')


def maps(request):
    return render(request,'Maps.html')

def prediction(request):
    return render(request,'Prediction.html')


def FeedbackView(request):
    if request.method == "POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                    pass
    else:
        form=FeedbackForm()
    return render (request,'Feedback.html',{'form':form})

def ViewFeedback(request):
    feedback=Feedback2.objects.all()
    return render(request,'ViewFeedback.html',{'feedback':feedback})

def deleteFeedback(request,id):
    feedback=Feedback2.objects.get(id=id)
    feedback.delete()
    return redirect ('/ViewFeedback')

def editfeedback(request,id):
    feedback=Feedback2.objects.get(id=id)
    return render(request,'editfeedback.html',{'feedback':feedback})

def UpdateFeedback(request,id):
    feedback=Feedback2.objects.all()
    return render(request,'UpdateFeedback.html',{'feedback':feedback})
