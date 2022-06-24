from attr import fields
from rest_framework import viewsets
from CITRApp.models import Candidacies, Vacancy, User
from CITRApp.serializers import VacancySerializer, CandidacySerializer, UserSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilterInput(FilterSet):
    min_salary = NumberFilter(field_name="salary", lookup_expr='gte')
    max_salary = NumberFilter(field_name="salary", lookup_expr='lte')

    class Meta:
        model = Vacancy
        fields = ['shifts']

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nameVacancy']
    search_fields = ['nameVacancy', 'nameCompany', 'cep', 'typeHires']
    filterset_class = FilterInput
    

class CandidacyViewSet(viewsets.ModelViewSet):
    queryset = Candidacies.objects.all()
    serializer_class = CandidacySerializer
