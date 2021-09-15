from django.http import HttpResponse
from django.core.mail import send_mail

def hello(request):
    send_mail(
        'Subject here',
        'We did it. END OF PROJECt',
        'amritansh131001@outlook.com',
        ['aryanjunagade5@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Hello baby!")
    