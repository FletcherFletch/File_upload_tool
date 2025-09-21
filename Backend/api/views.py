from django.shortcuts import render
from .forms import ImageForm

# Create your views here.

def home_view(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {
                'form': ImageForm(),
                'success': True
            })
    
    else:
        form = ImageForm()
    
    return render(request, 'home.html', {'form': form})