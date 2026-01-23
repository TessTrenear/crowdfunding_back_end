from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer) : #Inherit FundraiserSerializer, do not need to repeat code. Only add the difference.
    pledges = PledgeSerializer(many=True, read_only=True)