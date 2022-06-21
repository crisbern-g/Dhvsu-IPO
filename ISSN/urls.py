from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssnHome.as_view(), name='issn-home'),
    path('add/', views.AddIssnView.as_view(), name='add-issn'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks-issn'),
    path('<slug:slug>/', views.IssnDetailView.as_view(), name='issn-detail'),
    path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file-issn'),
    path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file-issn'),
    path('delete-issn/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole-issn'),
    path('search', views.SearchView.as_view(), name='search-issn')
]
