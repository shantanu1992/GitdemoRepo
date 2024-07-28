from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Registration_model


def home(request):
    users= Registration_model.objects.all()
    return render(request, 'home.html', {'users':users})

def userdetails(request):
    return render(request,'userdetails.html')

def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        dob = request.POST['dob']
        image = request.FILES['image']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if(password1!=password2):
            messages.info(request,'Password must be same')
            return redirect('./registration')
        if email == '':
            messages.info(request, 'Email can not be left blank')
            return redirect('./registration')
        if User.email == email:
            messages.info(request,'Email taken')
            return redirect('./registration')
        
        user = User.objects.create_user(first_name = firstname, last_name=lastname, username=email, email=email, password = password1)
        user.save()
        
        reg = Registration_model(user=user, dob=dob, image=image)
        reg.save()
        return redirect('/userhome')
      
    return render(request, 'registration.html' )

def loginuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('./userdetails')
        else:
            messages.info(request,'Incorrect username/password')
            return redirect('./login')
    else:
        return render(request, 'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('./login')


def contact_card(request):
    context={}
    data = Registration_model.objects.get(user__id=request.user.id)
    context['data'] = data
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        dob = request.POST['dob']
        image = request.FILES['image']

        usr = User.objects.get(id=request.user.id)
        usr.first_name=fn
        usr.last_name=ln
        usr.email=em
        usr.save()

        data.dob= dob
        data.image = image
        data.save()

        context['status'] = 'Changes saved successfully'
    return render(request, 'contact_card.html', context)
