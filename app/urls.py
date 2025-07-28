from django.urls import path
from .views import index_view, login_view, register_view, \
    reset_view, logout_view, user_detail_view, get_text_json, TemplView, MyTemplView, MyFormView, MyLoginView
from django.contrib.auth.views import LoginView

app_name = 'app'

urlpatterns = [
    path('', index_view, name='index'),
    path('template/', MyFormView.as_view(), name='template'),
    # path('template/', MyTemplView.as_view(), name='template'),
    # path('template/', TemplView.as_view(), name='template'),
    # path('template/', template_view, name='template'),
    path('login/', LoginView.as_view(template_name='app/login.html',
                                     redirect_authenticated_user=True), name='login'),
    path('login/', MyLoginView.as_view(), name='login'),
    # path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('reset/password', reset_view, name='reset'),
    path('logout', logout_view, name='logout'),
    path('profile/', user_detail_view, name='user_profile'),
    path('get/text/', get_text_json),
]