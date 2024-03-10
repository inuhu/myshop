from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include

from users.views import *

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path(
        'password-change/',
        PasswordChangeView.as_view(
            template_name='password_change_form.html',
            success_url=reverse_lazy('users:password_change_done')
        ),
        name='password_change'
    ),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]
