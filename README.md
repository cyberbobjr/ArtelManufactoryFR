# Artel Manufactory — traduction française

Module de traduction indépendant pour Project Zomboid **42.21**, réalisé à partir de la copie installée d'Artel Manufactory **0.2.0** le 7 octobre 2026.

- Mod d'origine : https://steamcommunity.com/sharedfiles/filedetails/?id=3794133594
- Identifiant d'origine : `ArtelManufactory`.
- Identifiant de traduction : `batman_ArtelManufactoryFR`.

## Activation

Le jeu détecte directement ce projet dans `Zomboid/Workshop/ArtelManufactoryFR/Contents/mods` : aucune copie n'est nécessaire.

1. Redémarrer complètement le jeu.
2. Activer **batman_Artel Manufactory - Traduction française** et **Artel Manufactory [42.21]** dans la liste utilisée par la partie.
3. Charger la traduction après Artel Manufactory.
4. Choisir **Français** dans les options du jeu.

Pour une partie existante, activer aussi la traduction dans sa propre liste de mods. Aucune sauvegarde ni liste de mods n'a été modifiée automatiquement.

## Contenu et entretien

Le module fournit exclusivement les onze fichiers de textes français du mod : menus, entités, recettes évolutives, agriculture, fluides, interface et dialogues, noms d'objets, meubles, recettes, bac à sable et infobulles. Il ne copie aucun script de gameplay ni ressource du mod d'origine. Le fichier `language.json` n'est pas repris : le français est déjà déclaré par le jeu.

Après une mise à jour du mod d'origine, exécuter `python tools/validate_translation.py` pour repérer les clés ajoutées, retirées et les marqueurs modifiés. Les éventuels textes écrits directement dans le code, les images ou les sons du mod d'origine ne sont pas couverts par ces fichiers de langue.

## Validation

Le dernier journal local indique `version=42.21.0`. Les références moteur consultées sont celles des sources décompilées 42.21.0. Le contrôle fourni vérifie les JSON UTF-8, doublons, clés et ordre, paramètres, balises et retours à la ligne, ainsi que la dépendance et l'absence de Lua de gameplay.

**Aucun test en jeu n'a été effectué.** Après activation, contrôler un nom d'objet Artel, une recette, une infobulle, les options de bac à sable et le comptoir commercial. Vérifier l'absence de `JSON Error` dans `console.txt` et le rendu des textes dans les fenêtres.

Ce projet est créé localement et n'a pas été publié sur Steam. Les textes de traduction restent dérivés du contenu de l'auteur d'Artel Manufactory ; aucune autorisation de redistribution de son code ou de ses images n'est présumée.
