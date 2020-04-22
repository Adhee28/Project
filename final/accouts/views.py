from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
#from.models import Feedback

# Create your views here.
#def Feedback(request):
    #name=request.POST["name"]
    #email=request.POST["email"]
    #description=request.POST["description"]

    #feedback=Feedback(name=name,email=email,description=description)
    #feedback.save()
            #return render (request,'home.html')






def login(request):
  if request.method=='POST':
      username = request.POST["username"]
      password = request.POST["password"]

      user=auth.authenticate(username=username,password=password)
      if user is not None:
        auth.login(request,user)
        print('invalid login')
        return redirect("/")
      else:
          return redirect('login')

  else:
      return render(request,'login.html')  






def register(request):

    if request.method =="POST":
      username = request.POST["username"]
      password1 = request.POST["password1"]
      password2 = request.POST["password2"]
      email = request.POST["email"]

      if password1==password2:
        if User.objects.filter(username=username).exists():
          print('Username is taken.Try with anthor username')
        else:
            
          user=User.objects.create_user(username=username,password=password1,email=email)
          user.save()
          print('Registered to the system')
          return redirect('login')
      else:
        print('Password is not matching')
      return redirect('/')

    else:
         return render(request,'Register.html')

def logout (request):
  auth.logout(request)
  return redirect('/')