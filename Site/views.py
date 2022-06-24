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
        copyrights = CopyRightApplicationModel.objects.all().count()
        patents = PatentApplicationModel.objects.all().count()
        utility_models = UtilityModelApplicationModel.objects.all().count()
        industrial_design = IndustrialDesignApplicationModel.objects.all().count()
        trademarks = TrademarkApplicationModel.objects.all().count()
        issns = IssnApplicationModel.objects.all().count()

        context = {
            'copyrights' : copyrights,
            'patents' : patents,
            'utility_models' : utility_models,
            'industrial_designs' : industrial_design,
            'trademarks' : trademarks,
            'issns' : issns
        }

        return render(request, 'Site/index.html', context)