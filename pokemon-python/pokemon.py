# Pokemon Master

fire = "fire"
water = "water"
grass = "grass"

min_level = 5
max_health_multiplier = 6
default_potion = 20

def damage_multiply(base_damage, attack_type, defense_type):
    if attack_type == fire:
        return fire_attack(base_damage, defense_type)
    elif attack_type == water:
        return water_attack(base_damage, defense_type)
    elif attack_type == grass:
        return grass_attack(base_damage, defense_type)
    else:
        return base_damage

def fire_attack(base_damage, defense_type):
    if defense_type == water:
        return round(base_damage / 2)
    elif defense_type == grass:
        return base_damage * 2
    else:
        return base_damage
    
def water_attack(base_damage, defense_type):
    if defense_type == grass:
        return round(base_damage / 2)
    elif defense_type == fire:
        return base_damage * 2
    else:
        return base_damage
    
def grass_attack(base_damage, defense_type):
    if defense_type == fire:
        return round(base_damage / 2)
    elif defense_type == water:
        return base_damage * 2
    else:
        return base_damage

class Pokemon:
    def __init__(self, name, type, level=min_level):
        self.name = name
        self.level = min_level if (level < min_level) else level
        self.type = type
        self.max_health = level * max_health_multiplier
        self.current_health = self.max_health
        self.knocked_out = False
        self.exp = 0
        self.creation_announce()
        
    def creation_announce(self):
        print(self.name + " created.")
        print("Type: " + self.type)
        print("Level: " + str(self.level))
        print("Health: " + self.health_string())
        print("Unconcious: " + str(self.knocked_out) + "\n")
        
    def lose_health(self, damage=0):
        if damage < 0:
            damage = 0
        self.current_health -= damage
        if self.current_health <= 0:
            self.knock_out()
        else:
            print(self.name + " now has " + self.health_string() + " health.\n")
            
    def knock_out(self):
        self.knocked_out = True
        self.current_health = 0
        print(self.name + " fell unconscious!\n")
        
    def gain_health(self, gain=0):
        if gain < 0:
            gain = 0
        self.current_health += gain
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(self.name + " has " + str(self.current_health) + "/" + str(self.max_health) + " health.\n")
        
    def attack(self, opponent):
        print(self.name + " attacks " + opponent.name + ".")
        damage = damage_multiply(self.level, self.type, opponent.type)
        print("It does " + str(damage) + " damage.")
        self.exp_up(damage)
        opponent.lose_health(damage)
        
    def health_string(self):
        return str(self.current_health) + "/" + str(self.max_health)
    
    def exp_up(self, damage):
        self.exp = self.exp + damage
        if self.level > 99:
            return
        level_up_threshold = self.level * self.level * 5
        if self.exp > level_up_threshold:
            self.level = self.level + 1
            self.exp = self.exp - level_up_threshold
            print(self.name + " has leveled up!")
        
        
        
        
class Trainer:
    def __init__(self, name, pokemon_list=[], potions=0, current_pokemon=0):
        self.name = name
        pokemon_list_length = len(pokemon_list)
        if pokemon_list_length > 6:
            shortened_pokemon_list = list(pokemon_list[:6])
            self.pokemon_list = shortened_pokemon_list
        else:
            self.pokemon_list = pokemon_list
        self.potions = potions
        pokemon_count = len(pokemon_list)
        self.current_pokemon = current_pokemon if (current_pokemon < pokemon_count) else pokemon_count-1
        
    def use_potion(self):
        if (self.potions < 1):
            print("You are out of potions!\n")
            return
        current_pokemon = self.pokemon_list[self.current_pokemon]
        if current_pokemon.knocked_out == True:
            print(current_pokemon.name + " cannot be revived with a potion.\n")
            return
        last = "their last" if self.potions == 1 else "a"
        print(self.name + " uses " + last + " potion on " + self.pokemon_list[self.current_pokemon].name)
        self.pokemon_list[self.current_pokemon].gain_health(default_potion)
        self.potions = self.potions - 1
        
    def switch_pokemon(self, index):
        if index < 0:
            return
        pokemon_count = len(self.pokemon_list)
        if index < pokemon_count:
            target_pokemon = self.pokemon_list[index]
            if target_pokemon.knocked_out == True:
                print(target_pokemon.name + " is unconscious and cannot be brought into battle!\n")
                return
            self.current_pokemon = index
            print(self.name + " is switching to " + target_pokemon.name + ".\n")
                  
    def attack(self, opponent):
        my_pokemon = self.pokemon_list[self.current_pokemon]
        if my_pokemon.knocked_out == True:
            print(my_pokemon.name + " is unconscious and cannot attack!\n")
            return
        opponent_pokemon = opponent.pokemon_list[opponent.current_pokemon]
        if opponent_pokemon.knocked_out == True:
            print(opponent_pokemon.name + " is already unconscious!\n")
            return
        my_pokemon.attack(opponent_pokemon)
        
        
charmander = Pokemon("Charmander", fire)
squirtle = Pokemon("Squirtle", water)
bulbasaur = Pokemon("Bulbasaur", grass)

charmeleon = Pokemon("Charmeleon", fire, 16)
wartortle = Pokemon("Wartortle", water, 17)
ivysaur = Pokemon("Ivysaur", grass, 18)

ash_pokemons = [charmander, squirtle, bulbasaur]
ash = Trainer("Ash", ash_pokemons, 11, 0)

brock_pokemons = [charmeleon, wartortle, ivysaur]
brock = Trainer("Brock", brock_pokemons, 33, 1)

ash.attack(brock)
brock.use_potion()
ash.switch_pokemon(1)
brock.attack(ash)
ash.use_potion()
brock.switch_pokemon(0)
ash.attack(brock)
ash.attack(brock)

ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
brock.use_potion()
ash.attack(brock)
brock.use_potion()
ash.attack(brock)
brock.use_potion()

