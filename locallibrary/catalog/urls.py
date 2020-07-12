# Use include() to add paths from the catalog application
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]