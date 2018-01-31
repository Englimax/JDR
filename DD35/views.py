from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlayedCharacter, ChatRoom, Message#, Campaign, Attribute, SkillInventory, PlayedCharacter, VariousModificator, Dons, Spell, SpellUsage, SpellInventory, Item, Pouch, ItemInventory, Weapon, Armor
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Armor
from .serializers.ArmorSerializer import ArmorSerializer
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from pusher import Pusher
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

pusher = Pusher(app_id=u'462482', key=u'e35aa2ec9d8ab3ac21ce', secret=u'7286fe37c3e2761f6b3e', cluster='eu')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'DD35/signup.html', {'form': form})

@csrf_exempt
def broadcast(request):
    user = User.objects.get_by_natural_key(request.POST['user'])
    message = request.POST['message']
    chatroom = ChatRoom.objects.get(id=1)
    message_save = Message.objects.create(room = chatroom, sender=user, message=message)
    message_save.save()
    pusher.trigger(str(request.POST['channel']), u'my-event', {u'name': request.user.username, u'message': message})
    return HttpResponse("done");


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




@login_required(login_url='/login')
def index(request):
    player_list = User.objects.order_by('username')
    chatrooms = filter(lambda x: ChatRoom.is_present(x, request.user), ChatRoom.objects.all())
    print(chatroom for chatroom in chatrooms)
    context = {'player_list': player_list, 'chatrooms': chatrooms}
    return render(request, 'DD35/index.html', context)


def index_list(request):
    armors = Armor.objects.all()
    context = {'armors': armors}
    return render(request, 'DD35/index.html', context)

@login_required(login_url='/login')
def character_detail(request, charac_id):
    character = PlayedCharacter.objects.get(id=charac_id)
    attributes = character.attributes.jsonified()
    user = User.objects.get(id = request.user.pk)
    # chatrooms = user.chatrooms
    chatrooms = ChatRoom.objects.filter(list_of_users__in=[request.user])
    context = {'character': character, 'attributes': attributes, 'chatrooms': chatrooms}
    if character:
        return render(request, 'DD35/index.html', context)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


def chat_list(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:5]
    context = {
        'chat_list': chat_rooms,
    }
    return render(request, 'DD35/chat_list.html', context)


def chat_detail(request, chat_room_id):
  chat = get_object_or_404(ChatRoom, pk=chat_room_id)
  return render(request, 'DD35/chat_room.html', {'chat': chat})


def perso(request, perso_id):
    personnage = PlayedCharacter.objects.id[perso_id]
    context = {'perso':  personnage, 'perso_id': perso_id}
    return render(request, 'DD35/perso.html', context)


def itemInv(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def spellInv(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)