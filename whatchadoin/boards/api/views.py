from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from boards.models import Board

# Generic class views
from .permissions import IsOwnerOrReadOnly
from .searializers import UserSerializer, BoardSerializer
from rest_framework import generics, permissions


class BoardViewSet(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class UserViewSet(viewsets.ModelViewSet):
    print("HI")
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
