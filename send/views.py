from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):
    send_mail('test email',
              'Hello this is a test message',
              'iperezmba@gmail.com', ['iperezmba@gmail.com'],
              fail_silently=False)

    return render(request, 'send/index.html ')
