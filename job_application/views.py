from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(firstname=firstname,lastname=lastname,email=email,date=date,occupation=occupation)

            message_body = f"Hey {firstname}\n your application received\n"
            email = EmailMessage("Form Received Successfully", message_body, to=[email])
            email.send()

            messages.success(request, f"{firstname}, Your form submitted successfully")

    return render(request, "home.html")


def about(request):
    return render(request, 'about.html')
