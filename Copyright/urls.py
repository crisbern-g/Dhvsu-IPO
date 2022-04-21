from django.urls import path
from . import views

urlpatterns = [
    path('', views.CopyrightHome.as_view(), name='copyright-home'),
    path('add/', views.AddCopyrightView.as_view(), name='add-copyright'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks'),
    path('<slug:slug>/', views.CopyrightDetailView.as_view(), name='copyright-detail'),
    path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file'),
    path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file'),
    path('delete-copyright/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole'),
    path('search', views.SearchView.as_view(), name='search-copyright')
]