from rest_framework import serializers

# Register your serializers here
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'