from django.shortcuts import render, redirect
import requests
import os
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from .forms import SignupForm
key = os.environ.get('weather_api_key')
#print(key)

def index(request):
    if request.method == 'POST': 
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + str(key)
        #city = 'Sofia'
        #print(url)
        try: 
            weather_data = requests.get(url.format(city)).json()
            weather = {
                'city' : city,
                "country_code": weather_data['sys']['country'], 
                'temperature' : str(weather_data['main']['temp']) + "° C",
                'description' : weather_data['weather'][0]['description'],
                'icon' : weather_data['weather'][0]['icon']
            }
        except:
            weather = { 'city': "The given place could not be found" }

    else:
        weather = []
    context = {'weather' : weather}
    return render(request, 'weather/index.html', context) 

# # signup page
# def register_request(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# # login page
# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')    
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("main:home")
#             else:
#                 messages.error(request,"Invalid username or password.")
#         else:
#             messages.error(request,"Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form":form})

# # logout page
# def user_logout(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect('login')