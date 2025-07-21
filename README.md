# unzip_and_merge.py

Script Python de décompression automatique, fusion intelligente et copie de fichiers issus de fichiers `.zip`, notamment ceux générés par Google Takeout.

## Objectif

Lors d’un export Google Takeout, les données sont souvent fragmentées dans plusieurs fichiers `.zip` avec des structures similaires. Ce script permet de :

- Décompresser automatiquement tous les `.zip` présents dans un dossier.
- Fusionner les arborescences extraites (création ou regroupement de dossiers).
- Écraser les fichiers en doublon en conservant la version la plus récente.
- Copier le contenu vers un dossier de destination unique.
- Supprimer le `.zip` et les fichiers extraits une fois le traitement terminé.
- Surveiller en continu l’arrivée de nouveaux `.zip` et les traiter automatiquement.

## Structure recommandée

```
takeout-unzip/
├── unzip_and_merge.py # Le script
├── source/ # Dossier contenant les fichiers .zip
└── target/ # Dossier final fusionné
```

Le script doit être placé dans le dossier `source/`.

## Installation

Pré-requis : Python 3.6 ou supérieur.

```bash
git clone https://github.com/votre-compte/takeout-unzip.git
cd takeout-unzip/source
```

Aucune dépendance externe.

## Utilisation

Lancer le script depuis le dossier contenant les `.zip`, en indiquant le dossier de destination :

```
python3 unzip_and_merge.py ../target

```

Le script fonctionne en boucle et traite chaque nouveau `.zip` automatiquement.

## Nettoyage

Chaque zip est supprimé après traitement, ainsi que son contenu temporairement extrait.
