# Projet Odoo Docker - Demande Interne

## Description
Ce projet est une implémentation d'un module Odoo personnalisé pour gérer les demandes internes. Il utilise Docker pour faciliter le déploiement et l'exécution.

## Technologies utilisées
- **Odoo 17.0** : Framework ERP open-source basé sur Python pour la gestion d'entreprise.
- **PostgreSQL 15** : Base de données relationnelle utilisée par Odoo.
- **Docker** : Plateforme de conteneurisation pour exécuter les services.
- **Docker Compose** : Outil pour définir et exécuter des applications multi-conteneurs.

## Étapes pour lancer le projet

### Prérequis
- Docker installé sur votre machine (voir [documentation Docker](https://docs.docker.com/get-docker/)).
- Docker Compose installé (généralement inclus avec Docker Desktop).

### Lancement
1. Ouvrez un terminal dans le répertoire racine du projet (`odoo-docker-DmD`).
2. Exécutez la commande suivante pour démarrer les services :
   ```
   docker-compose up
   ```
3. Attendez que les conteneurs se lancent. Odoo sera accessible sur `http://localhost:8069`.
4. Lors du premier lancement, configurez Odoo avec les informations suivantes :
   - Base de données : `postgres`
   - Utilisateur : `odoo`
   - Mot de passe : `odoo`

### Arrêt du projet
Pour arrêter les services :
```
docker-compose down
```

### Développement
- Les addons personnalisés sont dans le dossier `addons/`.
- La configuration Odoo est dans `config/odoo.conf`.
- Les logs sont disponibles dans `logs.txt`.

## Dépannage
- Si le port 8069 est occupé, modifiez le mapping dans `docker-compose.yml`.
- Vérifiez les logs avec `docker-compose logs` en cas de problème.