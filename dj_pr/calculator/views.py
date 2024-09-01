from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import character, Character

response = {'dexterity': character.dexterity,'action_speed': character.action_speed,'agility': character.agility,'move_speed': character.move_speed,'vigor': character.vigor,'strength': character.strength,'health': character.health,'dexterity': character.dexterity ,'spell_casting_speed': character.spell_casting_speed,'knowledge': character.knowledge,'will': character.will,'buff_duration': character.buff_duration,'debuff_duration': character.debuff_duration,'physical_power': character.physical_power,'magical_power': character.magical_power,'resourcefulness': character.resourcefulness}
            
def index(request):
    character, created = Character.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase_strength':
            character.increase_strength(1)      
            return JsonResponse({'strength': character.strength,'vigor': character.vigor, 'health': character.health, 'physical_power': character.physical_power })
        elif action == 'increase_vigor':
            character.increase_vigor(1)
            return JsonResponse({'vigor': character.vigor,'strength': character.strength,'health': character.health})
        elif action == 'decrease_strength':
            character.decrease_strength(1)
            return JsonResponse({'strength': character.strength,'vigor': character.vigor, 'health': character.health, 'physical_power': character.physical_power })
        elif action == 'decrease_vigor':
            character.decrease_vigor(1)
            return JsonResponse({'vigor': character.vigor,'strength': character.strength,'health': character.health })
        elif action == 'increase_agility':
            character.increase_agility(1)
            return JsonResponse({'agility': character.agility,'action_speed': character.action_speed,'move_speed': character.move_speed})
        elif action == 'decrease_agility':
            character.decrease_agility(1)
            return JsonResponse({'agility': character.agility,'action_speed': character.action_speed,'move_speed': character.move_speed})
        elif action == 'increase_dexterity':
            character.increase_dexterity(1)
            return JsonResponse({'dexterity': character.dexterity,'action_speed': character.action_speed})
        elif action == 'decrease_dexterity':
            character.decrease_dexterity(1)
            return JsonResponse({'dexterity': character.dexterity,'action_speed': character.action_speed})
        elif action == 'increase_knowledge':
            character.increase_knowledge(1)
            return JsonResponse({'knowledge': character.knowledge,'spell_casting_speed': character.spell_casting_speed})
        elif action == 'decrease_knowledge':
            character.decrease_knowledge(1)
            return JsonResponse({'knowledge': character.knowledge,'spell_casting_speed': character.spell_casting_speed})
        elif action == 'increase_will':
            character.increase_will(1)
            return JsonResponse({'will': character.will,'buff_duration': character.buff_duration,'debuff_duration': character.debuff_duration,'magical_power': character.magical_power})
        elif action == 'decrease_will':
            character.decrease_will(1)
            return JsonResponse({'will': character.will,'buff_duration': character.buff_duration,'debuff_duration': character.debuff_duration,'magical_power': character.magical_power })
        elif action == 'reset':
            character.reset()
            return JsonResponse(response) 
        elif action == 'increase_resourcefulness':
            character.increase_resourcefulness(1)
            return JsonResponse({'resourcefulness': character.resourcefulness})
        elif action == 'decrease_resourcefulness':
            character.decrease_resourcefulness(1)
            return JsonResponse({'resourcefulness': character.resourcefulness})                    
            
    return render(request, "calculator/index.html", {'character': character})
