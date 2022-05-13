from rest_framework import serializers
from CITRApp import models

class UserSerializer(serializers.ModelSerializer):
    # senha = serializers.CharField(
    #     style={'input_type': 'password'},
    #     write_only=True,
    # label="Senha"
    # )

    # senha_confirm = serializers.CharField(
    #     style={'input_type': 'password'},
    #     write_only=True,
    #     label="Confirme a senha"
    # )

    class Meta:
        model = models.Usuario
        fields = '__all__'
    
    # def save(self):
    #     conta = models.Usuario(
    #         Email = self.validated_data['Email'], 
    #     )
    #     senha = self.validated_data['senha']
    #     senha_confirm = self.validated_data['senha_confirm']

    #     if senha != senha_confirm:
    #         raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
    #     conta.set_password(senha)
    #     conta.save()

    #     return conta