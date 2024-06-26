from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Events
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    items=Events.objects.all()
    return render(request,'blog.html',{'items':items})

def add_events(request):
    if  request.method=='POST':
        name = request.POST['event_name']
        image = request.FILES.get('event_image')   
        description = request.POST['event_description']
        cost =request.POST.get('event_cost')
        events=Events(Event_Name=name,Event_Image=image,Event_Description=description,Event_Cost=cost)
        events.save()
        return redirect('/')
    return render(request,"event.html")
                  
def edit(request,id):
    if request.method=="POST":
        items=Events.objects.get(id=id)
        items.Event_Name=request.POST['event_name']
        items.Event_Image=request.FILES.get('event_image')
        items.Event_Description=request.POST['event_description']
        items.Event_Cost=request.POST.get('event_cost')
        items.save()
        return redirect("/")
    
    
    events=Events.objects.get(id=id)
    return render(request,'edit.html',{'events':events})

def delete_product(request,id):
    events=Events.objects.filter(id=id)
    events.delete()
    return redirect("/")

def register(request):
    if request.method == "POST":
        fname = request.POST["firstName"]
        lname = request.POST["lastName"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["confirmPassword"]
        email = request.POST['email']
        profile_picture = request.FILES.get('profilePicture')  # Get profile picture
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists! Please try another one.")
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists! Please try another one.")
                return render(request, "register.html")
            else:
                # Create user
                user = User.objects.create_user(first_name=fname, last_name=lname, username=username,
                                                password=password1, email=email)
                
                # Save profile picture if provided
                # if profile_picture:
                #     user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture)
                #     user_profile.save()

                # messages.success(request, "Registration Successful! You can now login.")
                # return redirect("login")
        else:
            messages.error(request, "Password didn't match with Confirm Password")
    return render(request, "register.html")

def user_login(request):
     if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Enter Correct Credentials!")
            return redirect('login')
     return  render(request,'login.html')                  

def user_logout(request):
    logout(request)
    return render(request,'login.html')

@login_required
def index(request):
    items = Events.objects.all()
    user = request.user
    user_first_name = user.first_name
    user_last_name = user.last_name
    user_email = user.email
    # Do not include the password in the context
    return render(request, 'index.html', {'items': items, 'user_first_name': user_first_name, 'user_last_name': user_last_name, 'user_email': user_email})


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def about(request):
    return render(request, 'about.html')
def schedule(request):
    return render(request, 'schedule.html')
# def blog(request):
#     return render(request, 'blog.html')

def price(request):
    return render(request, 'price.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')
