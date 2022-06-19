from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndustrialDesignHome.as_view(), name='industrial-design-home'),
    path('add/', views.AddIndustrialDesignView.as_view(), name='add-industrial-design'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks-industrial-design'),
    path('<slug:slug>/', views.UtilityModelDetailView.as_view(), name='industrial-design-detail'),
    path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file-industrial-design'),
    path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file-industrial-design'),
    path('delete-industrial-design/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole-industrial-design'),
    path('search', views.SearchView.as_view(), name='search-industrial-design')
]