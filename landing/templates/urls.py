from django.urls import path
# from .views import MyFormView, TemplView
from .views import index_view

urlpatterns = [
    path('', index_view),
,
]
