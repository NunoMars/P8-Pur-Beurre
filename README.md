(Project8) Openclassrooms

Project Python Django

Livrable projet 8  (PDF)
Projet codé en Python framework(Django)
   
en utf8 et tournant en environnement virtuel et avec la méthode de TDD (Test Driven Devlopement).
 
https://github.com/NunoMars/P8-Pur-Beurre
 
https://trello.com/b/8lZnyl3L/purbeurrep8 
Lien site en production (sur Heroku)
https://nunopurbeurre.herokuapp.com/

Vois-ci la page du site en production  sur Heroku (Frontend):
 

On doit 
	L’application est hébergé sur Heroku et utilise le serveur Gunicorn installé automatiquement et listé sur le fichier « requirements.txt ».
Avant la mise en production, on doit créer deux variables coté Heroku : Une variable qui a pour valeur « production » et une seconde SECRET_KEY : ayant pour valeur la clef secrète qui va être utilisé par l’application. La valeur de la secret Key varie selon on est en locale ou en production.
On doit aussi installer Postgresql add-on sur heroku afin de créer la base de données!
	Afin de « peupler » la base de données, j’ai créé une commande customisé, « insertdata ».
	Une fois l’application sur heroku on ouvre le terminal et on doit exécuter les commandes :
« python manage.py migrate »  
« python manage.py insertdata » 
On crée aussi un super-user :
« python manage.py createsuperuser » 
Et le programme est prêt à être utilisé.
