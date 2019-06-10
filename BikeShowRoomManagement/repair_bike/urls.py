from django.urls import path
from repair_bike import views
urlpatterns = [
    path('show_add_repair_bike/',views.showRepairBike,name='show_add_repair_bike'),
    path('add_repair_bike/',views.addRepairBike,name='add_repair_bike'),
    path('show_repair_bike/',views.showEditRepairBike,name='show_repair_bike'),
    path('edit_repair_bike/',views.editRepairBike,name='edit_repair_bike'),
    path('del_repair_bike/',views.deleteRepairBike,name='del_repair_bike'),
    path('show_search_repair_bike/',views.show_searchRepairBike,name='show_search_repair_bike'),
    path('search_repair_bike/',views.searchRepairBike,name='search_repair_bike'),
]