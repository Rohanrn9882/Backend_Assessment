from rest_framework.serializers  import ModelSerializer
# from django.contrib.auth import get_user_model
from .models import  Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie 
        fields = '__all__'