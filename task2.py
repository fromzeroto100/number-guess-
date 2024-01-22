game_level = 3 
# Here enemies is Global scope
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)    

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"] # Here enemies is local scope

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)  
        

