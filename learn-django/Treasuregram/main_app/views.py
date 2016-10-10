from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
# , logout


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
        else:
            pass
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


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
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,
                                            'treasures': treasures})

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
