# Publication 1.0.0 — 2026-10-07

- Dépôt GitHub : `cyberbobjr/ArtelManufactoryFR`, visibilité privée vérifiée avec `gh repo view`.
- Workshop : https://steamcommunity.com/sharedfiles/filedetails/?id=3815128330
- Identifiant du mod : `batman_ArtelManufactoryFR`.
- Validation des onze JSON : 3 070 clés, syntaxe, couverture, ordre, paramètres et balises conformes à la copie source 0.2.0.
- Simulation d'envoi sans blocage ; publication principale et description française confirmées par l'API SteamUGC.
- Visibilité publique (`visibility=0`) et contenu de 1 955 875 octets confirmés par GetPublishedFileDetails.
- Page française relue : description et bloc Workshop ID / Mod ID présents.
- Dépendance Workshop ajoutée : `3794133594`, retour Steam `EResult 1` ; sa présence est confirmée dans la section `RequiredItems` de la page.
- Aperçus additionnels : 0 avant et après envoi.
- Aucun test interactif en jeu effectué, ni modification du dossier des mods abonnés.

Outil de publication : `../.claude/tools/steam_workshop_publish.py` depuis la racine du workspace, avec `ArtelManufactoryFR --create --submit` pour la première publication.
