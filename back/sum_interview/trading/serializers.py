from rest_framework import serializers
from trading.models import Blotter, User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['name', 'email']
        
class BlotterSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Blotter
        fields = ['id','ticker', 'volume', 'price', 'user', 'user_name', 'user_email'] 


        