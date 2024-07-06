from django.shortcuts import render, HttpResponse,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    #usually we fetch from database and send it to context
    # context = {'variable':"this is sent"}          #context is a set of variables which is sent to template 
    #write {{variable}} in template where you wnat to send variable
    # return render(request, 'index.html',context)
    return render(request, 'index.html')
#     #return HttpResponse("this is homepage")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the form data to the database or send an email, etc.
        
        # Set a success message
        messages.success(request, 'Your message was sent successfully!')
        
        # Redirect to the home page
        return redirect('home')  # 'home' is the name of the URL pattern for your home page

    return render(request, 'contact.html')

# def contact(request):
#     #return HttpResponse("this is contact page")
#     return render(request, "contact.html")
    
def order(request):
    #return HttpResponse("We offer following services:")
    return render(request, "order.html")

# def login(request):
#     #return HttpResponse("We offer following services:")
#     return render(request, "login.html")
def designer_detail(request):
    #return HttpResponse("We offer following services:")
    return render(request, "designer-detail.html")
def design_list(request):
    #return HttpResponse("We offer following services:")
    return render(request, "design-list.html")
def myaccount(request):
    #return HttpResponse("We offer following services:")
    return render(request, "my-account.html")

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')