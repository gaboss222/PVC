		Python PVC
   Gabriel Griesser et Guillaume Noguera


Instructions :
	python NogueraGriesser.py guiOrNot maxTime path
Ex :
	python NogueraGriesser.py True 5 None
	python NogueraGriesser.py False 4.3 data/pb005.txt


Les opérations suivantes ont été réalisées :

Calcul fitness (fonction score) : renvoie la plus courte distance entre 2 villes

La selection : On croise la meilleure moitié du tableau et l'autre motié, on la refait en random. Pas la meilleure méthode

Mutation (fonction mutate) : Inversion au hasard de 2 villes dans un parcours. Choix du taux de mutation variable
Choix d'un random.uniform entre 0 et 0.06 pour minimiser l'aléatoire (plus de chance de mutation qu'avec un random.random() simple)

Croisement (fonction crossover) : Echange de 2 parties du tableau --> Création d'enfants --> crossover OX avec la fonction compress permettant le tassement


Beaucoup de galère sur le croisement, merci Guillaume qui a bien compris comment faire !

