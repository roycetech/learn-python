from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html',
                  {'treasures': treasures, 'form': form})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


def home(request):
    return render(request, 'home.html')


def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=True)

    return HttpResponseRedirect('/')


# class Treasure:
#     def __init__(self, name, value, material, location, img_url):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#         self.img_url = img_url


# treasures = [
#     t = Treasure('Gold Nugget', 500.00, 'Gold', "Curly's Creek, NM", 'http://www.example.com/gold.png'),
#     Treasure("Fool's Gold", 0, 'Pyrite', "Fool's Falls, CO", 'http://www.example.com/gold.png'),
#     Treasure('Coffee Can', 20.00, 'Aluminum', 'Acme, CA', 'http://www.example.com/gold.png')
# ]
