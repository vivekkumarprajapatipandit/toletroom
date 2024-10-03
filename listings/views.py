from django.shortcuts import render,redirect,HttpResponse
from .models import rentar,details,contact_team
from twilio.rest import Client
from .forms import SearchForm
from django.db.models import Q
from django.contrib import messages

def index(request):
    imgs=rentar.objects.all()
    return render(request,"index.html",{"imgs":imgs})

def header(request):
    return render(request,"header_navbar.html")

def home(request):
    image=rentar.objects.all()
    return render(request,"home.html",{"image":image})

def display(request):
    return render(request,"display.html")



 # Make sure to import your model

def register(request):
    alert_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        Mnumber = request.POST.get("Mnumber")
        if not username or not email or not password or not Mnumber:
            alert_message = "All fields are required."
            return redirect('home')  
        
        try:
            data = details(Name=username, Email=email, Password=password, Mnumber=Mnumber)
            data.save()
            alert_message = "Registration successful!and you can login"
        except Exception as e:
            alert_message = f"Registration failed: {str(e)}"
            return redirect('home')  

    return render(request, "register.html", {'alert_message': alert_message})


# this is login form 


    







def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        m_no = request.POST.get("M_no")
        
        # Save data to the database
        data = contact_team(Name=name, Email=email, Subject=subject, Message=message, M_No=m_no)
        data.save()
        
        # Send SMS using Twilio
        account_sid = 'your_twilio_account_sid'
        auth_token = 'your_twilio_auth_token'
        client = Client(account_sid, auth_token)
        
        try:
            message = client.messages.create(
                body=f"Thank you {name} for contacting us. We have received your message.",
                from_='your_twilio_phone_number',
                to=m_no
            )
            print("Message sent successfully")
        except Exception as e:
            print(f"Failed to send message: {e}")
            
        return HttpResponse("Your information is saved and a message has been sent to your mobile number.")
    
    return render(request, "contact.html")





def about(request):
    return render(request,"About.html")
def login(request):

    if request.method=="POST":
        email=request.get("email")
        pws=request.get("password")

        if pws==details:
            return render("home")
        else:
            return HttpResponse("password is incorrect!")
    return render(request,"login.html")


def rental(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        addr=request. POST.get("add")
        state=request.POST.get("state")
        dist=request.POST.get("district")
        img=request.POST.get("imgs")
        data=rentar(name=name,phone=phone,add=addr,state=state,dist=dist,images=img)
        data.save()
    image=rentar.objects.all()
    return render(request,"renter.html",{"image":image})

def customer(request):
    return render(request,"customer.html")


def search(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            query_object = Q(name__icontains=query) | Q(add__icontains=query) | Q(state__icontains=query) | Q(dist__icontains=query) | Q(images__icontains=query)
            results =rentar.objects.filter(query_object)
            if not results: 
                return HttpResponse("🤙 your searching  in not found please check another")
        else:
            return HttpResponse("Form is not valid")
    else:
        return HttpResponse("Query not found in request")

    return render(request, 'search.html', {'form': form, 'results': results})