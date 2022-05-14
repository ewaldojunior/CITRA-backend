from dataclasses import fields
from rest_framework import serializers
from CITRApp import models
from CITRApp.validators import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['CPF']):
            raise serializers.ValidationError({'CPF':'O número é inválido'})
        
        if not nome_valido(data['NomeCompleto']):
            raise serializers.ValidationError({'NomeCompleto':'Não inclua números neste campo'})

        if not celular_valido(data['Celular']):
            raise serializers.ValidationError({'Celular':'O número precisa seguir este modelo: XX XXXXX-XXXX'})
        return data





    