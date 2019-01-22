# 2015_MAST
Machine Assisted Scanning Toolkit
Logiciel pour scinder des PDF que j'ai crée pour mon ancien employeur pour aider avec la numérisation des documents, en appuyant sur la puissance du logiciel CPDF pour un usage très spécifique lors de mon ancienne activité.

!!! Ceci ne comprends pas la derniere version mais une version précédente pour démontrer mon code !!!

# Contexte
Pour rendre plus facile ma tâche de numérisation de documents dans un ancien poste, j'ai crée une petite programme du style Wrapper/Front qui permet l'utilisateur de saisir des données à propos des documents scannés qui se trouvent dans le PDF fourni pour ensuite le scinder avec un système de nomenclature précis. 

# Versions plus récentes
Des versions faites plus tard incluaient des fonctionalités tel que transferer les PDFs sortis dans leur dossiers finals, un système de historique plus puissant, ainsi que moins de bugs, etc.

# Pour le tester
Vous pouvez lancer le logiciel et essayer les menus etc. Mais pour scinder les PDFs, cette programme fait appel à une programme externe (cpdf.exe) qui doit obligatoirement se trouver dans le même dossier. Cette programme est fourni ici, https://github.com/coherentgraphics/cpdf-binaries, désormais avec une licence "Community", donc pour le but de démontrer, j'ai inclu la binaire dans ce projet, mais ça ne m'appartient pas. 

Bien que c'est possible de lancer le code avec Python sous Linux, ça ne marche correctement que sous Windows.

# Licence
Ce repétoire Git contient une programme CPDF.exe qui ne m'appartient pas. Pour détails de la licence pour ce dernier, vous les trouverez ici : https://community.coherentpdf.com

Quant à ma code, ça reste ma propriété. Merci de me demander si vous voulez l'utiliser pour quelque chose outre que tester et apprendre. 
