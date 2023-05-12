
# # basic URL Configurations
# from django.urls import include, path
# # import routers
# from rest_framework import routers

# # import everything from views
# from .views import *

# # define the router
# router = routers.DefaultRouter()

# # define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)

# # specify URL Path for rest_framework
# urlpatterns = [
# 	path('', include(router.urls)),
# 	path('api-auth/', include('rest_framework.urls'))
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data/', views.data, name='data'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
