from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.permissions import IsOwner
from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
