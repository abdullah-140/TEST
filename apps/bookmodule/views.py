from django.shortcuts import render,redirect,HttpResponse
from .forms import InputForm,ContactForm
from .models import PCS
from .filters import PCSfilters



# Create your views here.


def index(request):
   
        
        
    return render(request, 'bookmodule/index.html')


# Create your views here.





def getBooks(request):
    
    obj = PCS.objects.all()
    PCS_filter=PCSfilters(request.GET,  queryset=obj)
    context = {
        "obj":obj,
        "filter":PCS_filter
    }
    return render(request, 'bookmodule/books.html', context)

def book(request, bId):
    
    obj = PCS.objects.get(id = bId)
    return render(request, 'bookmodule/book.html', {"obj":obj})



def getContactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("success")
    else:
        
      
        form = ContactForm()
                
    return render(request, 'bookmodule/contactus.html',{"form":form})



def success(request):
    return HttpResponse("Success!!!!")


def getAboutus(request):
        
    return render(request, 'bookmodule/aboutus.html')


    


def add_pc(request):
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        
        if form.is_valid():
             obj = form.save()
             return redirect('book', bId = obj.id )
    form = InputForm()
    return render(request, 'bookmodule/addpc.html', {"form":form})

       

    
def update_pc(request,bId):
        
    obj = PCS.objects.get(id = bId)
    if request.method == 'POST':
        form = InputForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('book', bId = obj.id )
        
    form = InputForm(instance=obj)
    return render(request, "bookmodule/update.html", {'form':form})
    

    
    


    
        