import random
ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:
    # Jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour")
        SKIP_TURN = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez vous attaquer (1) ou utiliser une potion (2)")

        if user_choice == "1": #Attaque
            your_attack = random.randint(5, 10)
            ENEMY_HEALTH -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégâts à l'ennemi")
        elif user_choice == "2":
            if NUMBER_OF_POTIONS > 0:
                potion_health = random.randint(15, 50)
                PLAYER_HEALTH += potion_health
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous avez récupéré {potion_health} points de vie et vous avez {NUMBER_OF_POTIONS} de potions restantes")
            else:
                print("Vous n'avez plus de potions")
                continue
    
    if ENEMY_HEALTH <= 0:
        print("Vous avez gagné !")
        break

    # Attaque ennemie
    enemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats")

    if PLAYER_HEALTH <= 0:
        print("Vous avez perdu")
        break

    #Stats
    print(f"Il vous reste {PLAYER_HEALTH} points de vie")
    print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi")
    print("-"*50)

print("Fin deu jeu")
