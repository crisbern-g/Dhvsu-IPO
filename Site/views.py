from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Authentication.models import UserPicture

# Create your views here.

class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'Site/index.html')