import random


def partie():
    #les variables
    consecutive = 0
    victoire = 0
    defaite = 0
    combat = 1
    adverse = 0
    niv_vie = 20

    print("Vous êtes un aventurier dans une forêt.")
    # if niveau de vie = 0 fin partie
    while niv_vie >= 0:
        # force adversaire
        force_random = random.randint(1, 5)

        print(f"Vous atterisser sur un monstre de niveau {force_random}")
        # donner les choix que tu peux faire
        choix = int(input('Que voulez-vous faire?\n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller '
                          'ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie\n\n'))
        # si choix = 1
        if choix == 1:
            # ajouter le nbr de combat
            combat += 1
            adverse += 1
            # affiche information bataille
            print(
                f'\nAdversaire: {adverse}\nForce de adversaire: {force_random}\n'
                f'Votre niveau de vie: {niv_vie}\nCombat {combat} : {victoire} vs {defaite}')
            # lancé dé aléatoire
            score_de = random.randint(1, 6)
            print(f'Lancer de dé:{score_de}')
            # victoire
            if score_de >= force_random:
                niv_vie += force_random
                victoire += 1
                consecutive += 1

                print(f'Dernier combat: Victoire')
                print(f'Niveau de vie: {niv_vie}')
                print(f'Nombres de victoires consécutives: {consecutive}')

                print('\n')
            # défaite
            elif score_de <= force_random:
                niv_vie -= force_random
                defaite += 1
                consecutive = 0

                print(f'Dernier combat: Défaite')
                print(f'Niveau de vie: {niv_vie}')

                if niv_vie <= 0:
                    print(f'La partie est terminée. Vous Avex vaincu {victoire} monstres.')
        # si choix = 2
        if choix == 2:
            # -1 niveau de vie
            niv_vie -= 1
            print(f'Vous avez éviter le combat. Votre niveau de vie est maintenant à {niv_vie}')
        # si chois = 3
        if choix == 3:
            print(
                'Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de '
                'l’adversaire.\n '
                'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n'
                'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de '
                'l’adversaire.\n '
                'Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n'
                'La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n'
                'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité '
                'de 1 '
                'point de vie.')
        # si choix =4
        if choix == 4:
            print('Merci et au revoir...')
            quit()


partie()
