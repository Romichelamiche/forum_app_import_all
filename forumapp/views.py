from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forumapp.models import Membre, Probleme, Solution, Commentaire
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from forumapp.forms import ProblemeForm, CommentaireForm, SignUpForm, ChangeUserForm, ChangeUserPassword
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



from django.urls import reverse
import datetime


def problem_index(request, ): #Vue qui gère la page d'index

    ## Pagination ##
    problems = Probleme.objects.all()
    paginator = Paginator(problems, 6)
    page = request.GET.get('page', 1) #Ramene 1 si page est vide

    try:
        problems_list = paginator.page(page) #on construit une page via paginator
    except PageNotAnInteger:
        problems_list = paginator.page(1)
    except EmptyPage:
        problems_list = paginator.page(paginator.num_pages)

    ## Bloc gauche ##
    # sujets totaux
    problems.count()
    # sujets ayant le plus de commentaire
    comments_per_problems = Commentaire.objects.values('probleme_id','probleme__titre_probleme').annotate(com_count=Count('commentaire')).exclude(probleme__titre_probleme=None).order_by('-com_count')
    # sujets récents (sortir les 5 derniers sujets grâce au slice [0:5]
    problems_recent = problems.order_by('-created_at')[:5]

    #template = loader.get_template('forumapp/index.html')
    context = {'problems': problems,
               'problems_list': problems_list,
               'paginator' : paginator,
               'page' : page,
               'comments_per_problems': comments_per_problems,
               'problems_recent' : problems_recent,
               }
    return render(request, 'forumapp/index.html', context)

def problem_creation(request): #Vue qui gère la création de sujet
    if request.method == 'POST':
        form = ProblemeForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect ('forumapp:edit_problem', pk=post.pk)
    else:
        form = ProblemeForm()
    return render(request, 'forumapp/creation.html', {'form':form})


def problem_detail(request, pk): #A supprimer ?
    try:
        problem = Probleme.objects.get(pk = pk)
    except Probleme.DoesNotExist:
        raise Http404("Subject does not exist")
    return render(request, 'forumapp/detail.html', {'problem': problem})

def problem_edit(request, pk): #Vue qui gère l'édition des sujets
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

def search(request): #Vue qui gère la recherche dans la navbar
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

def delete_problem(request, pk=None): #Vue qui gère la suppression de sujets
    pb_to_delete = get_object_or_404(Probleme, pk=pk)
    pb_to_delete.delete()
    return redirect('forumapp:index')

def login_user(request): #Vue qui gère la page de connexion/login
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


def logout_user(request): #Vue qui gère la deconnexion/logout
    logout(request)
    return redirect('forumapp:login_function')

def register_user(request): #s'inscrire
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

def edit_user(request): #editer profil
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a bien été modifié")
            return redirect('forumapp:edit_function')

    else:
        form = ChangeUserForm(instance=request.user)
    return render (request, 'forumapp/edit_user.html', {'form':form})

class PasswordChangeConfView(SuccessMessageMixin, auth_views.PasswordChangeView) :
    template_name = 'forumapp/password_change.html'
    form_class = ChangeUserPassword
    success_url = 'http://127.0.0.1:8000/forumapp/index'

    success_message = 'Votre mot de passe a été modifié avec succès !'




