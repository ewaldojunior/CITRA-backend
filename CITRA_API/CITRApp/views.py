from rest_framework import viewsets, generics
from CITRApp.serializers import UserSerializer
from CITRApp.models import Usuario

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

# class ListaUsuarios(generics.ListAPIView):
    
#     def get_queryset(self):
#         queryset = Usuario.objects.all()
#         return queryset
#     serializer_class = UserSerializer
