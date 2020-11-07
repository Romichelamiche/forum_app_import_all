from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forumapp.models import Membre, Probleme, Solution, Commentaire
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from forumapp.forms import ProblemeForm, CommentaireForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

from django.urls import reverse
import datetime


def problem_index(request, ):
    problem_list = Probleme.objects.all()
    page_number = request.GET.get('page', 1)

    paginator = Paginator(problem_list, 6)

    problems = paginator.page(page_number)

    #Compter le nombre de problemes en tout
    problem_count = problem_list.count()

    #Compter le nombre total de commentaires groupés par probleme
    comment_count_per_problem = Commentaire.objects.values('probleme__titre_probleme').annotate(com_count=Count('commentaire')).exclude(probleme__titre_probleme=None).order_by('-com_count')

    template = loader.get_template('forumapp/index.html')
    context = {'problems': problems,
               'count': problem_count,
               'problem_with_high_count': comment_count_per_problem,
               }
    return render(request, 'forumapp/index.html', context)

def problem_creation(request):
    if request.method == 'POST':
        form = ProblemeForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect ('forumapp:detail_problem', pk=post.pk)
    else:
        form = ProblemeForm()
    return render(request, 'forumapp/creation.html', {'form':form})


def problem_detail(request, pk):
    try:
        problem = Probleme.objects.get(pk = pk)
    except Probleme.DoesNotExist:
        raise Http404("Subject does not exist")
    return render(request, 'forumapp/detail.html', {'problem': problem})

def problem_edit(request, pk):
    post = get_object_or_404(Probleme, pk=pk)
    commentaires = Commentaire.objects.filter(probleme=post).order_by('-updated_at')
    form = ProblemeForm(instance=post)

    if request.method == "POST":
        form = ProblemeForm(request.POST, instance=post)
        comment_form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forumapp:detail_problem', pk=post.pk)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.probleme = post
            comment.save()
            return redirect('forumapp:edit_problem', pk=post.pk)
    else:
        comment_form = CommentaireForm()
    return render(request, 'forumapp/creation.html', {'post':post, 'form': form, 'comment_form':comment_form, 'commentaires': commentaires, })

def problem_with_a_solution(request,):
    problem_solved = Probleme.objects.filter(resolu_probleme=1)
    return HttpResponse(problem_solved)

def search(request):
    query = request.GET.get('query')
    if not query:
        problem = Probleme.objects.all()
    else:
        problem_count = Probleme.objects.count()
        problem = Probleme.objects.filter(Q(titre_probleme__icontains=query) | Q(desc_probleme__icontains=query)) #passer par Q pour faire des requêtes "OU" sur le champ de recherche

    ########## Gérer la pagination après recherche ##########

    page_number = request.GET.get('page', 1)
    paginator = Paginator(problem, 6)
    pagination = paginator.page(page_number)

    context = {
        'problems': problem,
        'count': problem_count,
        'problems': pagination
    }
    return render(request, 'forumapp/index.html', context)

def delete_problem(request, pk=None):
    pb_to_delete = get_object_or_404(Probleme, pk=pk)
    pb_to_delete.delete()
    return redirect('forumapp:index')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #on reprend les names des champs html
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes connecté !")
            return redirect('forumapp:index')

        else:
            messages.success(request, "Impossible de vous identifiez, merci de recommencer")
            return redirect('forumapp:login_function')
    else:
        return render(request, 'forumapp/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('forumapp:login_function')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Vous êtes connecté, merci !")
            return redirect('forumapp:index')

    else:
        form = SignUpForm()
    return render (request, 'forumapp/register.html', {'form':form})

def edit_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Vous êtes connecté, merci !")
            return redirect('forumapp:index')

    else:
        form = SignUpForm(instance=request.user)
    return render (request, 'forumapp/register.html', {'form':form})

