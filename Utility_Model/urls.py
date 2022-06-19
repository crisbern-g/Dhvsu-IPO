from django.urls import path
from . import views

urlpatterns = [
    path('', views.UtilityModelHome.as_view(), name='utility-model-home'),
    path('add/', views.AddUtilityModelView.as_view(), name='add-utility-model'),
    path('edit-remarks/<slug:slug>/', views.EditRemarks.as_view(), name='edit-remarks-utility-model'),
    path('<slug:slug>/', views.UtilityModelDetailView.as_view(), name='utility-model-detail'),
    path('<slug:slug>/add-new-file/<str:file_type>/', views.AddSingleFile.as_view(), name='new-file-utility-model'),
    path('<slug:slug>/edit-file/<str:file_type>/', views.EditFile.as_view(), name='edit-file-utility-model'),
    path('delete-utility-model/<slug:slug>/', views.DeleteWhole.as_view(), name='delete-whole-utility-model'),
    path('search', views.SearchView.as_view(), name='search-utility-model')
]
