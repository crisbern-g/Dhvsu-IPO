import imp
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Copyright.models import CopyRightApplicationModel
from Patent.models import PatentApplicationModel
from Utility_Model.models import UtilityModelApplicationModel
from Industrial_Design.models import IndustrialDesignApplicationModel
from Trademark.models import TrademarkApplicationModel
from ISSN.models import IssnApplicationModel

# Create your views here.

class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'Site/index.html')