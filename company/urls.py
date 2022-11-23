from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('list/', views.company_list),
    # path('detail/<str:slug>', views.aow_detail),
    path('create/', views.create),
    # path('update/<str:slugkey>', views.update),
    # path('delete/<str:slug>', views.delete),

]