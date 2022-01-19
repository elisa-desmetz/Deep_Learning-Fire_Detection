# Deep_Learning-Fire_Detection
Mise en oeuvre des cours de deep learning. 

L'objectif de ce projet est de mettre en place un modèle permettant de reconnaître des images présentant du feu.

Les données initiales sont composées de 2 dossiers :
- 755 images d'incendies en extérieur
- 244 photos de nature "normales" (forêt, arbre, herbe, rivière, etc.)

Les données initiales sont biaisées, puisque les deux classes n'ont pas le même nombre d'échantillons. Il faut prendre en compte cette information afin de construire un set de validation approprié : avec un nombre égal d'images pour les deux classes.
