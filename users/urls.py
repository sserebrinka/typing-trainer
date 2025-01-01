from django.urls import path
from .views import profile_view, login_view, registration_view, update_test_results
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('update_test_results/', update_test_results, name='update_test_results'),
]