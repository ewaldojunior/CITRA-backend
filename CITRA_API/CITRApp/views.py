from rest_framework import viewsets
from CITRApp.models import Candidacies, Vacancy, User
from CITRApp.serializers import VacancySerializer, CandidacySerializer, UserSerializer
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

class CandidacyViewSet(viewsets.ModelViewSet):
    queryset = Candidacies.objects.all()
    serializer_class = CandidacySerializer