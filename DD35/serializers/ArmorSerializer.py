from rest_framework import serializers
from ..models import Armor
from ..models.model_choices import size

class ArmorSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    is_master = serializers.BooleanField(default=False)
    size = serializers.ChoiceField(choices=size)
    armor_bonus = serializers.IntegerField(default=1)
    dext_max = serializers.IntegerField(default=1)
    armor_malus = serializers.IntegerField(default=1)
    spell_fail = serializers.FloatField(default=0.1)
    speed = serializers.IntegerField(default=1)

    def create(self, validated_data):
        """
        Create and return a new `Armor` instance, given the validated data.
        """
        return Armor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Armor` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.is_master = validated_data.get('is_master', instance.is_master)
        instance.size = validated_data.get('size', instance.size)
        instance.armor_bonus = validated_data.get('armor_bonus', instance.armor_bonus)
        instance.dext_max = validated_data.get('dext_max', instance.dext_max)
        instance.armor_malus = validated_data.get('armor_malus', instance.armor_malus)
        instance.spell_fail = validated_data.get('spell_fail', instance.spell_fail)
        instance.speed = validated_data.get('speed', instance.speed)
        instance.save()
        return instance
