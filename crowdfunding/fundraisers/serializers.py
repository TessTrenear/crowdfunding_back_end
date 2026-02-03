from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id') # happy to show who owner is, not allowed to create one or write it. Read a fundraiser > read only
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer) : #Inherit FundraiserSerializer, do not need to repeat code. Only add the difference.
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data) : #We are telling our serializer how to perform an update on an existing instance of a Fundraiser.
        instance.title = validated_data.get ('title', instance.title) #When it performs that update, it will get some validated_data.
        instance.description = validated_data.get ('description', instance.description) #It should go through each field on the instance, and try to get the new value for that field from the validated_data
        instance.goal = validated_data.get ('goal', instance.goal) #In this step, we tell it what field in the JSON will contain the data it needs. We also note that if it can't find a value in the validated_data, it can use the value that is already on the instance! That's why we have things like .get('title', instance.title).
        instance.image = validated_data.get ('image', instance.image)
        instance.is_open = validated_data.get ('is_open', instance.is_open)
        instance.date_created = validated_data.get ('date_created', instance.date_created)
        instance.owner = validated_data.get ('owner', instance.owner)
        instance.save() #Then we save the instance to the database, and return it to the process that initiated the update.
        return instance #Provide your own update logica when serializing e.g. Instance of that fundraiser
            #can customise in the future.

class PledgeDetailSerializer(PledgeSerializer):
    fundraiser = FundraiserSerializer(many=True, read_only=True)

    def update(self, instance, validated_data) :
        instance.title = validated_data.get ('title', instance.title) #When it performs that update, it will get some validated_data.
        instance.description = validated_data.get ('description', instance.description) #It should go through each field on the instance, and try to get the new value for that field from the validated_data
        instance.goal = validated_data.get ('goal', instance.goal) #In this step, we tell it what field in the JSON will contain the data it needs. We also note that if it can't find a value in the validated_data, it can use the value that is already on the instance! That's why we have things like .get('title', instance.title).
        instance.image = validated_data.get ('image', instance.image)
        instance.is_open = validated_data.get ('is_open', instance.is_open)
        instance.date_created = validated_data.get ('date_created', instance.date_created)
        instance.supporter = validated_data.get ('supporter', instance.owner)
        instance.save() #Then we save the instance to the database, and return it to the process that initiated the update.
        return instance #Provide your own update logica when serializing e.g. Instance of that fundraiser
            #can customise in the future.