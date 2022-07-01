from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserView, UserApiView

urlpatterns = [
    path('', UserView.as_view()),
    path('login/', UserApiView.as_view(), name='login'),
    path('logout/', UserApiView.as_view(), name='logout'),
    path('signup/', UserView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
