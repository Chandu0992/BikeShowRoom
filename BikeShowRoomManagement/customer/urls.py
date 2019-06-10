from django.urls import path
from customer import views
urlpatterns = [
    path('show_add_customer/',views.showCustomer,name='show_add_customer'),
    path('add_customer/',views.addCustomer,name='add_customer'),
    path('show_customer/',views.showEditCustomer,name='show_customer'),
    path('edit_customer/',views.editCustomer,name='edit_customer'),
    path('del_customer/',views.deleteCustomer,name='del_customer'),
    path('show_search_customer/',views.show_searchCustomer,name='show_search_customer'),
    path('search_customer/',views.searchCustomer,name='search_customer'),
]