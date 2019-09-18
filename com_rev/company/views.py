from django.shortcuts import render
from company.forms import CompanyForm
from django.views import View
from company.models import Company
from django.http import HttpResponse






class GetIndex(View):
    def get(self, request):
        return render(request, 'index.html')




class CompanyView(View):
    
    def get(self, request):
        form = CompanyForm()
        return render(request, 'company.html', {'form': form})

    def post(self, request):
        form = CompanyForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
        
        else:
            form = CompanyForm()
        return render(request, 'company.html', {'form': form})


class CompanyAll(View):
    def get(self, request):
        com = Company.objects.all()
        
        if com != []:
            return render(request, 'companylist.html',{'data':com})
        else:
            return HttpResponse("NO COMPANYS IS ADDED YET!!")


