from django.shortcuts import render
from django.views import View
from company.models import Company
from review.models import Review
from review.forms import ReviewForm

class ReviewsByCompany(View):
    def get(self, request, pk):
        com  = Company.objects.get(id = pk)
        revs = Review.objects.filter(company = com)
        return render(request , 'reviewlist.html', {"compamy":com,"reviews":revs})


class GiveReview(View):
    def get(self, request):
        form = ReviewForm
        return render(request, 'companyreview.html', {'form': form})
    
    def post(self, request):
        form = ReviewForm(request.POST)
        print(form)
        if form.is_valid():
            
            print(' in review create')
            form.save(commit=True)
        else:
            print('in else')
            form = ReviewForm()
        return render(request, 'companyreview.html', {'form': form})
