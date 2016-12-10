from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import simplejson as json

from .forms import RegisterForm, LoginForm
from .models import user_game_status

# Create your views here.

def index(request):
    # Get top 10 scores to put on the leaderboard
    score_list = user_game_status.objects.order_by('-score').all()[:10]
    context = {
        'page_name':"Bit Clicker: Home",
        'score_list':score_list,
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_status = user_game_status(the_user=user, score=0, double_upgrades_owned=0)
            user_status.save()
            user = authenticate(username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {
        'form':form,
        "page_name":"Bit Clicker: Register",
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form = LoginForm()
                context = {
                    'form':form,
                    "page_name":"Bit Clicker: Login"
                }
                return render(request, 'login_error.html', context)
    else:
        form = LoginForm()

    context = {
        'form':form,
        "page_name":"Bit Clicker: Login"
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def game(request):
    # User has to be authenticated in order to access the game
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    score_list = user_game_status.objects.order_by('-score').all()[:10]
    context = {
        'page_name':"Bit Clicker: Game",
        'score_list':score_list,
    }
    return render(request, 'game.html', context)

def save_view(request):
    if request.method == 'POST':
        current_user = User.objects.get(username=request.user.username)
        current_user.user_game_status.score = request.POST['score']
        current_user.user_game_status.double_upgrades_owned = request.POST['double_upgrades_owned']
        current_user.user_game_status.save()
        return JsonResponse({'save':'complete'})
    else:
        return HttpResponseRedirect('/')

def top_scores(request):
    if request.method == 'GET':
        scores = user_game_status.objects.order_by('-score').all()[:10]
        s_list = []
        for s in scores:
            s_dict = {}
            s_dict["id"] = s.the_user.id
            s_dict["user_name"] = s.the_user.username
            s_dict["score"] = s.score
            s_list += [s_dict]
        return JsonResponse({'scores': s_list})
    return HttpResponse("404")
