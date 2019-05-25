from rest_framework import serializers
from .models import User
from .models import Caso
from .forms import UploadFileForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'age', 'reg_date')
        

class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = ('id', 'title', 'document', 'upload_to', 'user')
        
