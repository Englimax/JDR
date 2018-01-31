from rest_framework import serializers
from ..models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'force', 'dex', 'con', 'intell', 'sag', 'cha', 'pv', 'pv_temp', 'dmg_reduction', 'ca',
                  'deplacement', 'initiative', 'base_atk_bonus', 'reflexes', 'vigueur', 'volonte', 'poids_transp'
                  )





# class AttributeSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField(read_only=True)
#     force = serializers.IntegerField(default=10)
#     dex = serializers.IntegerField(default=10)
#     con = serializers.IntegerField(default=10)
#     intell = serializers.IntegerField(default=10)
#     sag = serializers.IntegerField(default=10)
#     cha = serializers.IntegerField(default=10)
#     pv = serializers.IntegerField(default=9)
#     pv_temp = serializers.IntegerField(default=0)
#     dmg_reduction = serializers.IntegerField(default=0)
#     ca = serializers.IntegerField(default=10)
#     deplacement = serializers.IntegerField(default=9)
#     initiative = serializers.IntegerField(default=0)
#     base_atk_bonus = serializers.IntegerField(default=0)
#     reflexes = serializers.IntegerField(default=0)
#     vigueur = serializers.IntegerField(default=0)
#     volonte = serializers.IntegerField(default=0)
#     poids_transp = serializers.FloatField(default=17.5)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Armor` instance, given the validated data.
#         """
#         return Attribute.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Armor` instance, given the validated data.
#         """
#         instance.id = validated_data.get('id', instance.id)
#
#         instance.force = validated_data.get('force', instance.force)
#         instance.dex = validated_data.get('dex', instance.dex)
#         instance.con = validated_data.get('con', instance.con)
#         instance.intell = validated_data.get('intell', instance.intell)
#         instance.sag = validated_data.get('sag', instance.sag)
#         instance.cha = validated_data.get('cha', instance.cha)
#         instance.pv = validated_data.get('pv', instance.pv)
#         instance.pv_temp = validated_data.get('pv_temp', instance.pv_temp)
#         instance.dmg_reduction = validated_data.get('dmg_reduction', instance.dmg_reduction)
#         instance.ca = validated_data.get('ca', instance.ca)
#         instance.deplacement = validated_data.get('deplacement', instance.deplacement)
#         instance.initiative = validated_data.get('initiative', instance.initiative)
#         instance.base_atk_bonus = validated_data.get('base_atk_bonus', instance.base_atk_bonus)
#         instance.reflexes = validated_data.get('reflexes', instance.reflexes)
#         instance.vigueur = validated_data.get('vigueur', instance.vigueur)
#         instance.volonte = validated_data.get('volonte', instance.volonte)
#         instance.poids_transp = validated_data.get('poids_transp', instance.poids_transp)
#         instance.save()
#         return instance