
from rest_framework.serializers import ModelSerializer
from .models import Coin
from rest_framework.validators import UniqueTogetherValidator

class CoinSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id','name','currency']

