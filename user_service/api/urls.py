from django.urls import path, include
from .views import UserView

urlpatterns = [
    path('users', UserView.as_view({'get':'listUsers', 'post':'createUser'})),
    path('users/<str:pk>', UserView.as_view({'get':'retrieveUser', 'delete': 'deleteUser'})),
]