from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render

def hello(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['content']
        recipients = [request.POST['recipient']]
        send_mail(subject, message, request.POST['sender'], recipients, False, request.POST['sender'], request.POST['sender_password'])
    return render(request, "mysite/index.html")
    