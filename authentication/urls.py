from django.contrib.auth.views import LoginView
from django.urls import path

import authentication.views

urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ),
         name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
]
