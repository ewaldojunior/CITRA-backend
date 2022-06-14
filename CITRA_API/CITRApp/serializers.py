from rest_framework import serializers
from CITRApp import models
from CITRApp.validators import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'CPF':'O número é inválido'})
        
        if not celular_valido(data['fone']):
            raise serializers.ValidationError({'Celular':'O número precisa seguir este modelo: XX XXXXX-XXXX'})
        
        if not cep_valido(data['cep']):
            raise serializers.ValidationError({'CEP':'O formato do CEP é inválido (XXXXX-XXX)'})

        return data

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = '__all__'


    