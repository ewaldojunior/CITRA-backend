from rest_framework import viewsets, generics
from CITRApp.serializers import UserSerializer
from CITRApp.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

