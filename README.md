# 2015 MAST
Machine Assisted Scanning Toolkit

An application for splitting PDF files that I created for my previous employer to aide with document scanning, by using the power of the program called CPDF for very specific usage in the context of my previous job.

NB: This is not the latest version, but a previous one. It is to demonstrate my code, and is not intended to be useful to other people. It was adapted to the context in which I used it.

[Version Française en bas]

# Background
To simplify my task of scanning administration documents, I created a little application in a Front/Wrapper style which allows the user to enter specific data about the scanned documents which are in the supplied PDF document, and then to split the PDF (by calling on CPDF with specific parameters), implementing a specific naming system for internal database standards.

# More recent versions (changes)
My more recent versions included features such as moving the generated PDFs into their final destination folders (specific to the host system where it would be used!), a better history system to speed up data entry, as well as bug correction, etc.

# Usage/testing
You can launch the program under Windows (or even Linux, though it is not made for it!), try the menus, etc. But to split the PDFs, this program calls an external program (cpdf.exe) which needs to be in the same folder. The program is supplied here, https://github.com/coherentgraphics/cpdf-binaries, now with a community licence, so to show this program's usage, I included the binary. But it does not belong to me!.

Although it is possible to launch this code in Python under Linux, it only works correctly under Windows.

# License
This Git repository contains a program CPDF which does not belong to me. For details about its license, you can go here: https://community.coherentpdf.com

As for my code, it is my property. Please ask me if you want to use it for anything other than testing and learning.

###############################################################################################

# Version Française

# 2015 MAST
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
