from django.urls import path
from . views import *

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('link/create', LinkCreateView.as_view(), name='link-create'),
    path('link/<int:pk>/update', LinkUpdateView.as_view(), name='link-update'),
    path('link/<int:pk>/delete', LinkDeleteView.as_view(), name='link-delete'), 
    path('<slug:profile_slug>/', ProfileView, name='profile'),
]
