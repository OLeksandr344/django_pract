from django.db import models
import math

class Character(models.Model):
    strength = models.IntegerField(default=10)
    vigor = models.IntegerField(default=10)
    health = models.IntegerField(default=75)
    agility = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    action_speed = models.IntegerField(default=0)
    move_speed = models.IntegerField(default=200)
    knowledge = models.IntegerField(default=10)
    spell_casting_speed = models.IntegerField(default=10)
    will = models.IntegerField(default=10)
    buff_duration = models.IntegerField(default=10)
    debuff_duration = models.IntegerField(default=math.ceil(-37.5))
    physical_power = models.IntegerField(default=0)
    magical_power = models.IntegerField(default=0)
    resourcefulness = models.IntegerField(default=10)
    power_grade = models.CharField(max_length=1, default="F")

    def increase_strength(self, n):
        self.strength += n
        self.update_health()
        self.update_physical_power()
        self.save()

    def increase_vigor(self, n):
        self.vigor += n
        self.update_health()
        self.save()

    def decrease_strength(self, n):
        self.strength = max(0, self.strength - n)
        self.update_health()
        self.save()

    def decrease_vigor(self, n):
        self.vigor = max(0, self.vigor - n)
        self.update_health()
        self.save()

    def increase_agility(self, n):
        self.agility += n
        self.update_actionspeed()
        self.update_move_speed()
        self.save()

    def decrease_agility(self, n):
        self.agility -= n
        self.update_actionspeed()
        self.update_move_speed()
        self.save()

    def increase_dexterity(self, n):
        self.dexterity += n
        self.update_actionspeed()
        self.save()

    def decrease_dexterity(self, n):
        self.dexterity -= n
        self.update_actionspeed()
        self.save()

    def increase_knowledge(self, n):
        self.knowledge += n
        self.update_spell_casting_speed()
        self.save()

    def decrease_knowledge(self, n):
        self.knowledge -= n
        self.update_spell_casting_speed()
        self.save()

    def increase_will(self, n):
        self.will += n
        self.update_buff_duration()
        self.update_debuff_duration()
        self.update_magical_power()
        self.save()

    def decrease_will(self, n):
        self.will -= n
        self.update_buff_duration()
        self.update_debuff_duration()
        self.update_magical_power()
        self.save()

    def increase_resourcefulness(self, n):
        self.resourcefulness += n
        self.save()

    def decrease_resourcefulness(self, n):
        self.resourcefulness -= n
        self.save()

    def update_health(self):
        sum_scaling = self.strength * 0.25 + self.vigor * 0.75
        if sum_scaling <= 0:
            self.health = int(75)
        elif sum_scaling <= 10:
            self.health = math.ceil(75 + 3 * sum_scaling)
        elif sum_scaling <= 50:
            self.health = math.ceil(105 + 2 * (sum_scaling - 10))
        elif sum_scaling <= 75:
            self.health = math.ceil(185 + (sum_scaling - 50))
        else:
            self.health = math.ceil(210 + 0.5 * (sum_scaling - 75))

    def update_actionspeed(self):
        self.action_speed = math.ceil(self.agility * 0.25 + self.dexterity * 0.75)

    def update_move_speed(self):
        if self.agility <= 0:
            self.move_speed = 290  
        elif 0 < self.agility <= 10:
            self.move_speed = math.ceil(290 + 0.5 * self.agility)  
        elif 10 < self.agility <= 15:
            self.move_speed = math.ceil(295 + 1 * (self.agility - 10)) 
        elif 15 < self.agility <= 75:
            self.move_speed = math.ceil(300 + 0.75 * (self.agility - 15))  
        elif 75 < self.agility <= 100:
            self.move_speed = math.ceil(345 + 0.5 * (self.agility - 75))  
        else:
            self.move_speed = 358 

    def update_spell_casting_speed(self):
        if self.knowledge <= 0:
            self.spell_casting_speed = -60 
        elif self.knowledge <= 5:
            self.spell_casting_speed = math.ceil(-60 + 5 * self.knowledge) 
        elif self.knowledge <= 10:
            self.spell_casting_speed = math.ceil(-35 + 4 * (self.knowledge - 5)) 
        elif self.knowledge <= 20:
            self.spell_casting_speed = math.ceil(-15 + 3 * (self.knowledge - 10))
        elif self.knowledge <= 50:
            self.spell_casting_speed = math.ceil(15 + 2.5 * (self.knowledge - 20))  
        elif self.knowledge <= 80:
            self.spell_casting_speed = math.ceil(90 + 2 * (self.knowledge - 50)) 
        elif self.knowledge <= 100:
            self.spell_casting_speed = math.ceil(150 + 1.5 * (self.knowledge - 80))  
        else:
            self.spell_casting_speed = 180  

    def update_buff_duration(self):
        if self.will <= 0:
            self.buff_duration = -80
        elif self.will <= 5:
            self.buff_duration = math.ceil(-80 + 10 * self.will)
        elif self.will <= 7:
            self.buff_duration = math.ceil(-30 + 5 * (self.will - 5))
        elif self.will <= 11:
            self.buff_duration = math.ceil(-20 + 3 * (self.will - 7))
        elif self.will <= 15:
            self.buff_duration = math.ceil(-8 + 2 * (self.will - 11))
        elif self.will <= 50:
            self.buff_duration = math.ceil(0 + 1 * (self.will - 15))
        else:
            self.buff_duration = math.ceil(35 + 0.5 * (self.will - 50))
        
        

    def update_debuff_duration(self):
        if self.will == 0:  
            self.debuff_duration = math.ceil(400)      
        elif self.will == 1:
                self.debuff_duration = math.ceil(233.3)
        elif self.will == 2:
                self.debuff_duration = math.ceil(150)
        elif self.will == 3:
                self.debuff_duration = math.ceil(100)
        elif self.will == 4:
                 self.debuff_duration = math.ceil(66.7)
        elif self.will == 5:
                self.debuff_duration = math.ceil(42.9)
        elif self.will == 6:
                self.debuff_duration = math.ceil(33.3)
        elif self.will == 7:
                self.debuff_duration = math.ceil(25)
        elif self.will == 8:
                self.debuff_duration = math.ceil(20.5)
        elif self.will == 9:
                self.debuff_duration = math.ceil(16.3)
        elif self.will == 10:
            self.debuff_duration = math.ceil(12.4)
        elif self.will == 11:
            self.debuff_duration = math.ceil(8.7)
        elif 12 <= self.will <= 13:
            self.debuff_duration = math.ceil(6.4 - 2.2 * (self.will - 12))
        elif 14 <= self.will <= 16:
            self.debuff_duration = math.ceil(2 - (self.will - 14))
        elif 17 <= self.will <= 18:
            self.debuff_duration = math.ceil(-2 - 0.9 * (self.will - 17))
        elif self.will == 19:
         self.debuff_duration = math.ceil(-4.8)
        elif self.will == 20:
            self.debuff_duration = math.ceil(-5.7)
        elif self.will == 21:
            self.debuff_duration = math.ceil(-6.5)
        elif self.will == 22:
            self.debuff_duration = math.ceil(-8.3)
        elif 23 <= self.will <= 28:
            self.debuff_duration = math.ceil(-8.3 - 0.8 * (self.will - 23))
        elif self.will == 29:
            self.debuff_duration = math.ceil(-12.3)
        elif self.will == 30:
            self.debuff_duration = math.ceil(-13)
        elif self.will == 31:
            self.debuff_duration = math.ceil(-13.8)
        elif self.will == 32:
            self.debuff_duration = math.ceil(-14.5)
        elif 33 <= self.will <= 35:
            self.debuff_duration = math.ceil(-15.3 - 0.7 * (self.will - 33))
        elif 36 <= self.will <= 38:
                   self.debuff_duration = math.ceil(-17.4 - 0.7 * (self.will - 36))
        elif self.will == 39:
                   self.debuff_duration = math.ceil(-20.6)
        elif 40 <= self.will <= 41:
                   self.debuff_duration = math.ceil(-21.3 - 0.7 * (self.will - 40))
        elif 42 <= self.will <= 45:
                   self.debuff_duration = math.ceil(-23.7 - 0.6 * (self.will - 42))
        elif self.will == 46:
                   self.debuff_duration = math.ceil(-24.2)
        elif 47 <= self.will <= 48:
                   self.debuff_duration = math.ceil(-25.4 - 0.6 * (self.will - 47))
        elif self.will == 49:
                   self.debuff_duration = math.ceil(-25.9)
        elif 50 <= self.will <= 51:
            self.debuff_duration = math.ceil(-26.5 - 0.3 * (self.will - 50))
        elif 52 <= self.will <= 54:
            self.debuff_duration = math.ceil(-26.7 - 0.3 * (self.will - 52))
        elif self.will == 55:
            self.debuff_duration = math.ceil(-27.5)
        elif self.will == 56:
            self.debuff_duration = math.ceil(-28.1)
        elif self.will == 57:
            self.debuff_duration = math.ceil(-28.3)
        elif self.will == 58:
            self.debuff_duration = math.ceil(-28.6)
        elif self.will == 59:
                       self.debuff_duration = math.ceil(-28.8)
        elif self.will == 60:
            self.debuff_duration = math.ceil(-29.1)
        elif 61 <= self.will <= 62:
            self.debuff_duration = math.ceil(-29.3 - 0.3 * (self.will - 61))
        elif 63 <= self.will <= 64:
            self.debuff_duration = math.ceil(-29.6 - 0.3 * (self.will - 63))
        elif self.will == 65:
            self.debuff_duration = math.ceil(-30.1)
        elif 66 <= self.will <= 67:
            self.debuff_duration = math.ceil(-30.3 - 0.3 * (self.will - 66))
        elif 68 <= self.will <= 69:
            self.debuff_duration = math.ceil(-31 - 0.3 * (self.will - 68))
        elif self.will == 70:
            self.debuff_duration = math.ceil(-31.3)
        elif 71 <= self.will <= 72:
            self.debuff_duration = math.ceil(-31.7 - 0.3 * (self.will - 71))
        elif 73 <= self.will <= 74:
            self.debuff_duration = math.ceil(-32 - 0.3 * (self.will - 73))
        elif 75 <= self.will <= 76:
            self.debuff_duration = math.ceil(-32.4 - 0.3 * (self.will - 75))
        elif self.will == 77:
            self.debuff_duration = math.ceil(-32.7)
        elif 78 <= self.will <= 79:
            self.debuff_duration = math.ceil(-33 - 0.3 * (self.will - 78))
        elif self.will == 80:
            self.debuff_duration = math.ceil(-33.3)
        elif 81 <= self.will <= 85:
            self.debuff_duration = math.ceil(-33.6 - 0.2 * (self.will - 81))
        elif self.will == 86:
            self.debuff_duration = math.ceil(-34.6)
        elif self.will == 87:
            self.debuff_duration = math.ceil(-34.9)
        elif 88 <= self.will <= 99:
            self.debuff_duration = math.ceil(-35.3 - 0.2 * (self.will - 88))
        elif self.will == 100:
            self.debuff_duration = math.ceil(-37.5)
        else:
            self.debuff_duration = math.ceil(-37.5)        

    def update_physical_power(self):
        self.physical_power += 1

    def update_magical_power(self):
        self.magical_power += 1

    def reset(self):
        self.strength = DEFAULT_VALUES['strength']
        character.strength = self.strength
        self.vigor   = DEFAULT_VALUES['vigor']
        character.vigor = self.vigor
        self.agility = DEFAULT_VALUES['agility']
        character.agility  = self.agility
        self.dexterity = DEFAULT_VALUES['dexterity']
        character.dexterity = self.dexterity
        self.knowledge = DEFAULT_VALUES['knowledge']
        character.knowledge = self.knowledge
        self.will = DEFAULT_VALUES['will']
        character.will = self.will
        self.resourcefulness = DEFAULT_VALUES['resourcefulness']
        character.resourcefulness = self.resourcefulness      
        self.save()
            
        
           
            
character = Character()


DEFAULT_VALUES = {
    'strength': 10,
    'vigor': 10,
    'health': 100,
    'agility': 10,
    'dexterity': 10,
    'knowledge': 10,
    'will': 10,
    'resourcefulness': 10,
}