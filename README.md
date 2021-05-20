# ProjetData_Engineering

***Presentation***

Cette application permet d'avoir en temps réel les informations de base sur les 50 principales crypto-monnaies. On peut ainsi choisir celles qu'on souhaite voir. Ensuite on peut voir sur 24h son bénéfice et voir combien représente une somme de crypto-monnaie.

Cette application est faite en 3 parties:
- Une partie **Scraping** pour récupérer les informations en temps réel du site cryptonaute.fr
- Une partie **Mongodb** pour stocker les informations
- Une partie **Streamlit.io** qui permet d'afficher un site dynamique pour visualiser les informations

***#### User-guide ####***

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


***#### Dev Guide ####***


Les modules utilisées sont les suivant:
- scrapy==2.4.1
- streamlit
- pymongo==3.6.1
- pandas
- schedule
- plotly.express
- matplotlib

Pour le **Scraping**:

On utilise un crawler, pour récupérer les informations en css dans le spider (coinmarker_spider.py), on choisit les différents 
éléments sur le site scrapé et on les ajoute dans la classe items (items.py) et ensuite ces items sont envoyés dans la base de données mongodb
dans la pipelines (pipelines.py).
On peut donc rajouter des informations en complétant coinmarker_spider.py et items.py
Cette partie est lancé conteneur app qui lance à intervalle de temps régulier le crawler.

Pour le **Mongodb**:

On initialise son image sur les ports 27017 pour ensuite pouvoir s'y connecté dans les différents programme sur le localhost.

Pour l' **App**:

On utilise le conteneur streamlit pour lancer le programme python streamlitapp.io, cette application est composé de différentes
fonctions pour nettoyer les données de mongodb qui ne sont pas sous la forme de nombre (pour les graphiques).
On récupére tous les noms des 50 cryptos et on récupère leurs informations pour les mettre dans un dataframe et ensuite on peut
les afficher sous forme de tableau.
