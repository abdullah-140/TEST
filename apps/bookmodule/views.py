from django.shortcuts import render,redirect
from .forms import InputForm


# Create your views here.


def index(request):
   
        
        
    return render(request, 'bookmodule/index.html')


# Create your views here.





def getBooks(request):
        
    return render(request, 'bookmodule/books.html', {'pcs' :__getPcslist()})

def book(request, bId):
    # book1= {'id':12344321, 'title': 'Continuous Delivery', 'author': '3. Humble and D. Farley'}
    # book2= {'id':56788765, 'title': 'Reversing: Secrets of Reverse Engineering', "author":'E. Ellam'}
    # PC 1
    pc1 = {
        "id": 1,
        "processor": "Intel Core i5-12600K",
        "ram": "16GB DDR4",
        "storage": "1TB NVMe SSD",
        "graphics": "NVIDIA GeForce RTX 3060",
        "motherboard": "ASUS ROG Strix Z690-A Gaming WiFi",
        "power_supply": "Corsair RM850x",
        "case": "NZXT H510i"
    }

    # PC 2
    pc2 = {
        "id": 2,
        "processor": "AMD Ryzen 7 5800X",
        "ram": "32GB DDR4",
        "storage": "2TB NVMe SSD + 4TB HDD",
        "graphics": "AMD Radeon RX 6700 XT",
        "motherboard": "MSI MEG X570 Unify-X",
        "power_supply": "Seasonic Prime TX-850",
        "case": "Fractal Design Meshify C ATX Mid Tower Case"
    }

    # PC 3
    pc3 = {
        "id": 3,
        "processor": "Intel Core i7-12700K",
        "ram": "32GB DDR5",
        "storage": "2TB NVMe SSD",
        "graphics": "NVIDIA GeForce RTX 3080",
        "motherboard": "ASUS ROG Strix Z690-E Gaming WiFi",
        "power_supply": "Corsair RM1000x",
        "case": "Lian Li O11 Dynamic XL ATX Mid Tower Case"
    }

    # PC 4
    pc4 = {
        "id": 4,
        "processor": "AMD Ryzen 9 5950X",
        "ram": "64GB DDR4",
        "storage": "4TB NVMe SSD + 4TB HDD",
        "graphics": "AMD Radeon RX 6900 XT",
        "motherboard": "MSI MEG X570S Unify-X",
        "power_supply": "Seasonic Prime TX-1000",
        "case": "NZXT H710i"
    }

    # PC 5
    pc5 = {
        "id": 5,
        "processor": "Intel Core i9-12900K",
        "ram": "64GB DDR5",
        "storage": "4TB NVMe SSD",
        "graphics": "NVIDIA GeForce RTX 3090 Ti",
        "motherboard": "ASUS ROG Strix Z690-F Gaming WiFi",
        "power_supply": "Corsair RM1200x",
        "case": "Fractal Design Define 7 XL ATX Mid Tower Case"
    }

    
    # targetBook=None
    # if book1['id'] == bId: targetBook = book1
    # if book2 ['id'] == bId: targetBook = book2
    # if targetBook== None: return redirect('/books')
    # context = {'book':targetBook }
    # return render(request, 'bookmodule/book.html', context)
    targetBook=None
    if pc1['id'] == bId: targetBook = pc1
    if pc2 ['id'] == bId: targetBook = pc2
    if pc3['id'] == bId: targetBook = pc3
    if pc4 ['id'] == bId: targetBook = pc4
    if pc5 ['id'] == bId: targetBook = pc5
    if targetBook== None: return redirect('/books')
    context = {'book':targetBook }
    return render(request, 'bookmodule/book.html', context)


def getTags(request):
        
    return render(request, 'bookmodule/tags.html')

def getContactus(request):
        
    return render(request, 'bookmodule/contactus.html')


def getAboutus(request):
        
    return render(request, 'bookmodule/aboutus.html')

def __getPcslist():
        pcs = []
        pc1 = {
        "id": 1,
        "processor": "Intel Core i5-12600K",
        "ram": "16GB DDR4",
        "storage": "1TB NVMe SSD",
        "graphics_card": "NVIDIA GeForce RTX 3060",
        "motherboard": "ASUS ROG Strix Z690-A Gaming WiFi",
        "power_supply": "Corsair RM850x",
        "case": "NZXT H510i"
    }

    # PC 2
        pc2 = {
            "id": 2,
            "processor": "AMD Ryzen 7 5800X",
            "ram": "32GB DDR4",
            "storage": "2TB NVMe SSD + 4TB HDD",
            "graphics_card": "AMD Radeon RX 6700 XT",
            "motherboard": "MSI MEG X570 Unify-X",
            "power_supply": "Seasonic Prime TX-850",
            "case": "Fractal Design Meshify C ATX Mid Tower Case"
        }

        # PC 3
        pc3 = {
            "id": 3,
            "processor": "Intel Core i7-12700K",
            "ram": "32GB DDR5",
            "storage": "2TB NVMe SSD",
            "graphics_card": "NVIDIA GeForce RTX 3080",
            "motherboard": "ASUS ROG Strix Z690-E Gaming WiFi",
            "power_supply": "Corsair RM1000x",
            "case": "Lian Li O11 Dynamic XL ATX Mid Tower Case"
        }

        # PC 4
        pc4 = {
            "id": 4,
            "processor": "AMD Ryzen 9 5950X",
            "ram": "64GB DDR4",
            "storage": "4TB NVMe SSD + 4TB HDD",
            "graphics_card": "AMD Radeon RX 6900 XT",
            "motherboard": "MSI MEG X570S Unify-X",
            "power_supply": "Seasonic Prime TX-1000",
            "case": "NZXT H710i"
        }

        # PC 5
        pc5 = {
            "id": 5,
            "processor": "Intel Core i9-12900K",
            "ram": "64GB DDR5",
            "storage": "4TB NVMe SSD",
            "graphics_card": "NVIDIA GeForce RTX 3090 Ti",
            "motherboard": "ASUS ROG Strix Z690-F Gaming WiFi",
            "power_supply": "Corsair RM1200x",
            "case": "Fractal Design Define 7 XL ATX Mid Tower Case"
        }
        pcs.append(pc1)
        pcs.append(pc2)
        pcs.append(pc3)
        pcs.append(pc4)
        pcs.append(pc5)
        return pcs
    

def get_search_pcs(request):

    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isGraphics_Card = request.POST.get('option1')
        isprocessor = request.POST.get('option2')
        # now filter
        pcs = __getPcslist()
        newpcs = []
        for item in pcs:
            contained = False
            if isGraphics_Card and string in item['graphics_card'].lower(): contained = True
            if not contained and isprocessor and string in item['processor'].lower():contained = True
            if contained: newpcs.append(item)
        return render(request, 'bookmodule/books.html', {'pcs':newpcs})
    return render(request , 'bookmodule/search.html')

def add_pc(request):
        context ={}
        context['forms']= InputForm()
        return render(request, 'bookmodule/addpc.html', context)
    
def update_pc(request):
        context ={}
        context['forms']= InputForm()
        return render(request, 'bookmodule/update.html', context)
    

    
    


    
        