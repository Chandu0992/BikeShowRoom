from django.urls import path
from insurance import views
urlpatterns = [
    path('show_add_insurance/',views.showInsurance,name='show_add_insurance'),
    path('add_insurance/',views.addInsurance,name='add_insurance'),
    path('show_insurance/',views.showEditInsurance,name='show_insurance'),
    path('edit_insurance/',views.editInsurance,name='edit_insurance'),
    path('del_insurance/',views.deleteInsurance,name='del_insurance'),
    path('show_search_insurance/',views.show_searchInsurance,name='show_search_insurance'),
    path('search_insurance/',views.searchInsurance,name='search_insurance'),
]