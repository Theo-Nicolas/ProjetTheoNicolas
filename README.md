# ProjetData_Engineering

***Presentation***

Cette application permet d'avoir en temps réel les informations de base sur les 50 principales crypto-monnaies. On peut ainsi choisir celles qu'on souhaite voir. Ensuite on peut voir sur 24h son bénéfice et voir combien représente une somme de crypto-monnaie.

Cette application est faite en 3 parties:
- Une partie **Scraping** pour récupérer les informations en temps réel du site cryptonaute.fr
- Une partie **Mongodb** pour stocker les informations
- Une partie **Streamlit.io** qui permet d'afficher un site dynamique pour visualiser les informations

***Installation***

**Git**

Pour commencer, vous devez utiliser 
git clone https://github.com/Theo-Nicolas/ProjetTheoNicolas.git


**Docker**

Docker est nécessaire pour utiliser l'application,
vous pouvez l'installer via ce lien https://www.docker.com/get-started

Ensuite après avoir lancé **Docker**, il faut ouvrir la console/invite de commande:

Vous devez ensuite aller dans le dossier du projet puis,
lancez l'application avec la commande:

**docker-compose up -d --build**

**Website**

Enfin vous pouvez aller voir l'application sur une page web à cette adresse :

**http://localhost:8501/**



**Application Web**

<img src="/Image/Avant.JPG" alt="Avant"/>

On peut utiliser le bouton pour afficher la tendance actuelle du marché.

Ensuite on va pouvoir choisir les crypto-monnaies que l'on souhaite voir/utiliser avec un menu déroulant.
Cela permet ensuite d'afficher le tableau avec les informations des crypto choisies, ensuite on demande
à l'utilisateur le nombre qu'il possède pour celles choisies mais il n'est pas obligé de les remplir.

<img src="/Image/Calculateur.JPG" alt="calculateur"/>

Et on récupére le bénéfice et la valeur de crypto-monnaie possédée.

Enfin il y'a une option graphique pour comparé les crypto-monnaies entre-elles avec un graphe en bar pour comparé 
les informations une par une.

<img src="/Image/Graphique.JPG" alt="Graphique"/>
