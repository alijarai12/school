from rest_framework import serializers
from api.models import SchoolProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolProfile
        fields = ['id', 'schoolname', 'schooladdress', 'contact', 'pimage']
