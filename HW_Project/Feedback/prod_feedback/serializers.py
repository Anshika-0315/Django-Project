from rest_framework import serializers
from .models import Feed_back

class Feed_backSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_back
        fields = ['name', 'email', 'mobile', 'rating', 'message']
