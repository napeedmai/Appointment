from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def feature(request):
    return render(request,'feature.html')
def appointment(request):
    return render(request,'appointment.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def error(request):
    return render(request,'error.html')
def doctor(request):
    return render(request,'doctor.html')

