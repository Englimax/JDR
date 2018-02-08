from django.contrib import admin
from .models import Player, Campaign, BaseItem, Attribute, SkillInventory, PlayedCharacter, VariousModificator, Dons, \
                    Spell, SpellUsage, SpellInventory, Item, Pouch, ItemInventory, Weapon, Armor, ChatRoom, Message, \
                    Skill

admin.site.register(Player)
admin.site.register(Campaign)
admin.site.register(Attribute)
admin.site.register(BaseItem)
admin.site.register(SkillInventory)
admin.site.register(PlayedCharacter)
admin.site.register(VariousModificator)
admin.site.register(Dons)
admin.site.register(Spell)
admin.site.register(SpellUsage)
admin.site.register(SpellInventory)
admin.site.register(Item)
admin.site.register(Pouch)
admin.site.register(ItemInventory)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(Skill)
