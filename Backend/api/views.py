from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import uupload

# Create your views here.

def home_view(request):

    if request.method == "POST":                                                                      
        #image = request.FILES['image']
        
        #uploaded =  uupload.objects.create(image=image)

        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_instance = form.save()
            return render(request, 'home.html', {
                'form': ImageForm(),
                'success': True,
                'upload_image': image_instance #pass image to display
            }) # {} conext passed to the template
    
    else:
        form = ImageForm()
    
    return render(request, 'home.html', {'form': form})

# def show_image(request, pk):
#      image = uupload.objects.get(pk=pk)
#      return render(request, 'home.html', {'upload_image': image})