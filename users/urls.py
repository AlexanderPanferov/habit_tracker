from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateView, UserRetrieveView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-get'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
