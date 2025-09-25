from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import uupload

# Create your views here.

def home_view(request):
    
    if request.method == "POST": # the user submits the form 

        form = ImageForm(request.POST, request.FILES)
        # this is creating bount form instance
        # request.POST -> the submmitted form data
        # request.FILES the uploaded file data 
        # basically giving django the form data and uploaded files and binding them to thsi form instance
        #so djanog can validate and process it 

        #request.POST contains all the non-file fields in the form ex. <input type="text" name="title" value="My Image"> then in django request.POST['title']  → "My Image"
        
        #request.FILES contains all the uplaoded files <input type="file" name="image"> then in django request.FILES['image']  → <InMemoryUploadedFile: myphoto.jpg>
        if form.is_valid():
            image_instance = form.save()
            # this creates and saves a new row in your database based on the validated form data 
            # image_instance is now a model instance ,  not just form data 
            # instance includes a reference to the uploaded file, so image_instance.image.url will return the path to the saved file
        
            return render (request,'home.html', {
                'form': ImageForm(), # brand new empty form
                'success': True, # flagging a success message
                'upload_image': image_instance #the saved object so you can show the uploaded image
            })
        
    else: # the user just opened the page
        form = ImageForm()
    
    return render(request, 'home.html', {'form': form})
            
# If someone submits the form (via POST),  it gets validated and saved
# If someone just visits the page (opening the URL / or /upload in the browser) then that is a GET request and form = ImageForm() creates a new, blank form instance 
# return render(request, 'home.html', {'form': form}) this renders the template and sends the empy form to the browser so the user can fill it out

