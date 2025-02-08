Ce projet est un module Odoo pour la gestion des stocks et des inventaires. Il comprend plusieurs modèles, vues, et fonctionnalités pour organiser les produits, les catégories, les fournisseurs, les emplacements de stockage, et les mouvements de stock. Voici une documentation détaillée de chaque composant.

1. Modèles (Models)
Categorie (categorie.produit)
Description : Ce modèle permet d'organiser les produits en catégories.

Champs :

name (Char) : Nom de la catégorie (obligatoire).

description (Text) : Description de la catégorie.

Emplacement (stock.emplacement)
Description : Ce modèle gère les emplacements de stockage.

Champs :

name (Char) : Nom de l'emplacement (obligatoire).

type (Selection) : Type d'emplacement (Interne ou Externe).

capacity (Float) : Capacité de l'emplacement (obligatoire).

product_ids (One2many) : Liste des produits stockés dans cet emplacement.

Contraintes :

La capacité doit être supérieure à 0.

Fournisseur (fournisseur.model)
Description : Ce modèle gère les fournisseurs.

Champs :

name (Char) : Nom du fournisseur (obligatoire).

phone (Char) : Téléphone du fournisseur (obligatoire).

address (Char) : Adresse du fournisseur (obligatoire).

email (Char) : Email du fournisseur.

StockMouvement (stock.mouvement)
Description : Ce modèle gère les mouvements de stock (entrées, sorties, ajustements).

Champs :

product_id (Many2one) : Produit concerné (obligatoire).

quantity (Float) : Quantité déplacée (obligatoire).

type (Selection) : Type de mouvement (Entrée, Sortie, Ajustement).

emplacement_source_id (Many2one) : Emplacement source.

emplacement_destination_id (Many2one) : Emplacement de destination.

reason (Text) : Raison du mouvement.

date (Datetime) : Date du mouvement (par défaut, la date actuelle).

Contraintes :

La quantité doit être supérieure à 0.

Vérification de la disponibilité du stock pour les sorties.

Méthodes :

_update_stock_quantity : Met à jour les quantités de stock après un mouvement.

Produit (stock.produits)
Description : Ce modèle représente les produits en stock.

Champs :

name (Char) : Nom du produit (obligatoire).

reference (Char) : Référence du produit (générée automatiquement).

barcode (Char) : Code-barres du produit.

categorie_id (Many2one) : Catégorie du produit (obligatoire).

emplacement_id (Many2one) : Emplacement du produit (obligatoire).

fournisseur_id (Many2one) : Fournisseur du produit (obligatoire).

mouvement_ids (One2many) : Liste des mouvements de stock pour ce produit.

quantity_ids (One2many) : Quantités de stock par emplacement.

quantity (Float) : Quantité totale du produit (calculée).

Méthodes :

_compute_quantity : Calcule la quantité totale du produit.

_inverse_quantity : Ajuste la quantité manuellement.

StockQuantity (stock.quantity)
Description : Ce modèle gère les quantités de stock par emplacement.

Champs :

product_id (Many2one) : Produit concerné (obligatoire).

emplacement_id (Many2one) : Emplacement concerné (obligatoire).

quantity (Float) : Quantité en stock (par défaut 0.0).

Contraintes :

Un produit ne peut avoir qu'une seule quantité par emplacement.

Méthodes :

update_stock : Met à jour la quantité de stock.

get_stock_quantity : Récupère la quantité de stock pour un produit et un emplacement.

2. Vues (Views)
Categorie
Form View : Formulaire pour créer/modifier une catégorie.

List View : Liste des catégories.

Emplacement
Form View : Formulaire pour créer/modifier un emplacement.

List View : Liste des emplacements.

Fournisseur
Form View : Formulaire pour créer/modifier un fournisseur.

List View : Liste des fournisseurs.

StockMouvement
Form View : Formulaire pour créer/modifier un mouvement de stock.

List View : Liste des mouvements de stock.

Produit
Form View : Formulaire détaillé pour créer/modifier un produit.

List View : Liste des produits.

StockQuantity
Tree View : Liste des quantités de stock par emplacement.

Form View : Formulaire pour créer/modifier une quantité de stock.

Search View : Recherche des quantités de stock.

3. Rapports (Reports)
Rapport Produit
Description : Génère un rapport PDF pour un produit.

Champs inclus : Nom, Référence, Catégorie, Fournisseur, Emplacement, Quantité.

4. Menus
Menu Principal : "Stock et Inventaire ERP".

Sous-menus :

Produits

Catégories

Mouvements

Fournisseurs

Emplacements

Quantités

5. Sécurité
Accès : Des règles d'accès sont définies pour chaque modèle, permettant aux utilisateurs de lire, écrire, créer et supprimer des enregistrements.

6. Fichier Manifeste
Description : Définit les métadonnées du module, les dépendances, et les fichiers de données à charger.

Fichiers inclus :

data/sequences.xml

security/ir.model.access.csv

views/*.xml

reports/stock_report.xml

views/menus.xml

Utilisation
Installation : Installer le module dans Odoo.

Navigation : Utiliser les menus pour accéder aux différentes fonctionnalités.

Gestion des Stocks : Ajouter des produits, des catégories, des fournisseurs, et des emplacements. Gérer les mouvements de stock et consulter les rapports.

Exemples d'Utilisation
Ajouter une Catégorie : Aller dans "Catégories" et cliquer sur "Créer".

Ajouter un Produit : Aller dans "Produits" et cliquer sur "Créer".

Effectuer un Mouvement de Stock : Aller dans "Mouvements" et cliquer sur "Créer".

Générer un Rapport : Dans la fiche d'un produit, cliquer sur "Imprimer le Rapport".
