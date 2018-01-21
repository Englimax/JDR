from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlayedCharacter#, Campaign, Attribute, SkillInventory, PlayedCharacter, VariousModificator, Dons, Spell, SpellUsage, SpellInventory, Item, Pouch, ItemInventory, Weapon, Armor

from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Armor
from .serializers.ArmorSerializer import ArmorSerializer
from django.http import Http404
from rest_framework.views import APIView


class armors_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        armors = Armor.objects.all()
        serializer = ArmorSerializer(armors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArmorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class armors_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Armor.objects.get(pk=pk)
        except Armor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        armor = self.get_object(pk)
        serializer = ArmorSerializer(armor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        armor = self.get_object(pk)
        serializer = ArmorSerializer(armor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        armor = self.get_object(pk)
        armor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def armors_list(request, format=None):
#     """
#     List all armors, or create a new armor.
#     """
#     if request.method == 'GET':
#         armors = Armor.objects.all()
#         serializer = ArmorSerializer(armors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArmorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def armors_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete an armor.
#     """
#     try:
#         armor = Armor.objects.get(pk=pk)
#     except Armor.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArmorSerializer(armor)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArmorSerializer(armor, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         armor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    player_list = User.objects.order_by('username')
    context = {'player_list': player_list}
    return render(request, 'DD35/index.html', context)

def index_list(request):
    armors = Armor.objects.all()
    context = {'armors': armors}
    return render(request, 'DD35/index.html', context)

def character_detail(request, charac_id):
    character = PlayedCharacter.objects.get(id=charac_id)
    attributes = character.attributes.jsonified()

    context = {'character': character, 'attributes': attributes}
    if character:
        return render(request, 'DD35/index.html', context)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)




def perso(request, perso_id):
    personnage = PlayedCharacter.objects.id[perso_id]
    context = {'perso':  personnage, 'perso_id': perso_id}
    return render(request, 'DD35/perso.html', context)


def itemInv(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def spellInv(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)