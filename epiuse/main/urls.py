from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path('<int:emp_num>',views.employee,name="employee"),
    path('<int:emp_num>/supervisor',views.supervisor,name='supervisor'),
    path("search_query/",views.search_query,name="search_query"),
    path("search_name/",views.search_name,name="search_name")
]


