from django.urls import path
from booking import views
urlpatterns = [
    path('show_add_booking/',views.showBooking,name='show_add_booking'),
    path('add_booking/',views.addBooking,name='add_booking'),
    path('show_booking/',views.showEditBooking,name='show_booking'),
    path('edit_booking/',views.editBooking,name='edit_booking'),
    path('del_booking/',views.deleteBooking,name='del_booking'),
    path('show_search_booking/',views.show_searchBooking,name='show_search_booking'),
    path('search_booking/',views.searchBooking,name='search_booking'),
]