from django.urls import path
from .views import IndexView, DetailsView

app_name = 'polls'

urlpatterns = [
    
    path('',IndexView.as_view(),name='index'),
    path('<int:pk>/',DetailsView.as_view(),name='detail'),


]