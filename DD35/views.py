from django.http import HttpResponse
from django.shortcuts import render
from DD35.models import Player, Campaign, Attribute, SkillInventory, PlayedCharacter, VariousModificator, Dons, Spell, SpellUsage, SpellInventory, Item, Pouch, ItemInventory, Weapon, Armor


def index(request):
    player_list = Player.objects.order_by('username')
    context = {'player_list': player_list}
    return render(request, 'DD35/index.html', context)


def perso(request, perso_id):
    personnage = Player.objects.id[perso_id]
    context = {'perso':  personnage, 'perso_id': perso_id}
    return render(request, 'DD35/perso.html', context)


def itemInv(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def spellInv(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)