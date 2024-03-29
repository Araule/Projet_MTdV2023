#!/bin/python3
# -*- coding: utf-8 -*-

""" Gestionnaire de noms de variable pour programme MdtV+ au format de dictionnaire
    Le fichier contient la classe et ses méthodes
"""

import regex
import sys


class GestionnaireVariables:
    def __init__(self):
        """initialisation du gestionnaire de noms de variable"""
        self.variables = {}

    def addVariable(self, nom: str, adresse: int):
        """ajout de la variable dans le gestionnaire

        Args:
            nom (str): nom de la variable
        """
        # si le nom de la variable est autorisé
        if regex.match(r"([a-z]|[A-Z]|_)|([a-z][A-Z][0-9]_)*", nom):
            # on ajoute la variable au gestionnaire avec son adresse
            self.variables[nom] = adresse
        else:
            # sinon, fin du programme
            print("\033[91mLe nom de variable {} n'est pas autorisé.\033[0m".format(nom)) 
            sys.exit(1)

    def updateAdresse(self, nom: str, adresse: int):
        """mise à jour de l'adresse de la variable dans le gestionnaire
            peut-être appelé par les fonctions du groupe 3 s'il
            fait de la relocalisation de mémoire

        Args:
            nom (str): nom de la variable
        """
        # si la variable existe dans le gestionnaire
        if nom in self.variables:
            # on met à jour l'adresse de la variable
            self.variables[nom] = adresse
        else:
            # sinon, fin du programme
            print("\033[91mL'adresse de la variable '{}' n'a pas pu être mise à jour.".format(nom))
            print("La variable n'existe pas dans le gestionnaire.\033[0m")
            sys.exit(1)

    def deleteVariable(self, nom: str):
        """suppression de la variable dans le gestionnaire

        Args:
            nom (str): nom de la variable
        """
        # si la variable est bien dans le gestionnaire
        if nom in self.variables:
            # suppression de la variable
            del self.variables[nom]
        else:
            # sinon, fin du programme
            print("\033[91mLa variable '{}' n'a pas pu être supprimé.".format(nom))
            print("La variable n'existe pas dans le gestionnaire.\033[00m")
            sys.exit(1)

    def printVariables(self):
        """affichage de toutes les variables du gestionnaire"""
        if len(self.variables.keys()) > 0:
            for nom, adresse in self.variables.items():
                print(f"{nom}: {adresse}")
        else:
            print("\033[92mLe gestionnaire de noms de variable est vide.\033[00m")

    def getDict(self) -> dict:
        """retourne le dictionnaire de noms de variable

        Returns:
            dict: gestionnaire de noms de variable
        """
        return self.variables

    def getAdresse(self, nom: str) -> int:
        """retourne l'adresse de la variable

        Args:
            nom (str): nom de la variable

        Returns:
            int: adresse de la variable (pour l'instant de type int)
        """
        if nom in self.variables:
            # si la variable est bien dans le gestionnaire
            return self.variables[nom]
        else:
            # sinon, fin du programme
            print("\033[91mL'adresse de la variable '{}' n'a pas pu être obtenu.".format(nom))
            print("La variable n'existe pas dans le gestionnaire\033[0m")
            sys.exit(1)

    def doesVariableExist(self, nom: str) -> bool:
        """vérifie si une variable se trouve dans le gestionnaire

        Args:
            nom (str): nom de la variable

        Returns:
            bool: renvoie True ou False
                selon si la variable existe dans le gestionnaire
        """
        if nom in self.variables:
            # si la variable se trouve bien dans le gestionnaire
            return True
        else:
            # sinon
            return False

    def effacementGestionnaire(self):
        """efface le gestionnaire de noms de variables
        à appeler à la fin du programme
        """
        self.variables = {}
