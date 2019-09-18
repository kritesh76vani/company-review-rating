from django.shortcuts import render
from django.views import View
from custom_user.forms import CustomUserForm

class CreateUserView(View):

    def get(self, request):
        form = CustomUserForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
        else:
            form = CustomUserForm()
        return render(request, 'create_user.html', {'form': form})



