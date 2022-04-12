from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sendmail(request):

    if request.method == 'POST':

        email = request.POST['email']
        msg = request.POST['msg']
        print(email,msg)


        send_mail(
    'test',
    msg,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )

    return render(request,'send/sendmail.html')



