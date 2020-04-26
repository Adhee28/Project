from django.shortcuts import render
from django.http import HttpResponse
from final import settings
from django.core.mail import send_mail

# Create your views here.
def mail(request):
    subject = "Test mail"
    msg = "Congratulations ,Email is done"
    to = "adheeshanavodi@gmail.com"
    res= send_mail(subject,msg, settings.EMAIL_HOST_USER, [to])

    if (res == 1):
        msg = "Mail sent"
    else:
            msg = "Mail couldn't send"

    return HttpResponse(msg)

