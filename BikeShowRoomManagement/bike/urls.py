from django.urls import path
from bike import views
urlpatterns = [
    path('show_add_bike/',views.showBike,name='show_add_bike'),
    path('add_bike/',views.addBike,name='add_bike'),
    path('show_bike/',views.showEditBike,name='show_bike'),
    path('edit_bike/',views.editBike,name='edit_bike'),
    path('del_bike/',views.deleteBike,name='del_bike'),
    path('show_search_bike/',views.show_searchBike,name='show_search_bike'),
    path('search_bike/',views.searchBike,name='search_bike'),
]