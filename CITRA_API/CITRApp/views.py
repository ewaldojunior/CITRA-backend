from rest_framework import viewsets
from CITRApp.models import Vacancy
from CITRApp.serializers import VacancySerializer
from CITRApp.serializers import UserSerializer
from CITRApp.models import User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nameVacancy']
    search_fields = ['nameVacancy', 'nameCompany', 'salary', 'cep', 'typeRemuneration']
    filterset_fields = ['shifts']