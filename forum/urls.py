"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from forumapp.forms import ChangeUserPassword
from forumapp import views
from forumapp.views import problem_index



urlpatterns = [
    path('forumapp/', include('forumapp.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
        # accounts/login/ [name='login']
        # accounts/logout/ [name='logout']
        # accounts/password_change/ [name='password_change']
        # accounts/password_change/done/ [name='password_change_done']
        # accounts/password_reset/ [name='password_reset']
        # accounts/password_reset/done/ [name='password_reset_done']
        # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
        # accounts/reset/done/ [name='password_reset_complete']
    #path('password_change/', auth_views.PasswordChangeView.as_view(template_name='forumapp/password_change.html', form_class=ChangeUserPassword, success_url=(path('forumapp/index', views.problem_index, name='index'))), name='password_change')
    path('password_change/', views.PasswordChangeConfView.as_view(), name='password_change'),
]
