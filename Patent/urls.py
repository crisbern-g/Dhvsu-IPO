from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatentHome.as_view(), name='patent-home'),
    path('add/', views.AddPatentView.as_view(), name='add-patent'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks-patent'),
    path('<slug:slug>/', views.PatentDetailView.as_view(), name='patent-detail'),
    path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file-patent'),
    path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file-patent'),
    path('delete-patent/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole-patent'),
    path('search', views.SearchView.as_view(), name='search-patent')
]