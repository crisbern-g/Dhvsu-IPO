from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'Authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('index-page')
        else:
            messages.success(request, 'Credentials did not match our records')
            return render(request, 'Authentication/login.html')

class LogoutView(View):
    def post(self, request):
        logout(request)

        return redirect('login')