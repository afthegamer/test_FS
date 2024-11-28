---

### **Test Développeur Full Stack (Énergie & Données)**

#### **Durée estimée :** 1 à 2 heures

#### **Objectifs :**

* Évaluer les compétences en **algorithmie** avec des données énergétiques.
* Tester la maîtrise de **Python** dans le traitement de données réelles.
* Vérifier l’expérience avec **Django** en créant une application simple d’analyse énergétique.
---

### **Partie 1 : Algorithmie et Python**

> **Objectif :** Évaluer la capacité à résoudre des problèmes avec des données énergétiques.

#### Exercice 1 : Calcul des pics de consommation électrique

**Énoncé :**  
Vous disposez d’un fichier CSV contenant les données annuelles de consommation électrique en France (<https://analysesetdonnees.rte-france.com/sites/default/files/graphDownloads/R%25C3%25A9partition_de_la_consommation_d%2527%25C3%25A9lectricit%25C3%25A9_fran%25C3%25A7aise_par_r%25C3%25A9gion_2024-08-14_10-21.csv>) avec les colonnes suivantes :

* `date` : Date (format ISO 8601).
* `region` : Nom de la région.
* `consumption_twh` : Consommation électrique en mégawattheures (TWh).

**Consignes :**

1. Écrire une fonction `find_peak_consumption(file_path: str) -> Dict[str, Any]` qui :
   * Identifie la région avec la consommation maximale à un moment donné.
   * Retourne la date et l’heure de ce pic, ainsi que la valeur correspondante.

---

#### Exercice 2 : Tri personnalisé

**Énoncé :** Dans le fichier <https://www.data.gouv.fr/fr/datasets/r/4c176588-a444-4dc7-b6bf-60390ae7e5be>, on souhaite trier une liste de *Typologie des données impactées* (colonne D). Les typologies doivent être triées par longueur, puis par ordre alphabétique pour celles de même longueur.

**Consignes :**

* Implémenter une fonction `custom_sort(strings: List[str]) -> List[str]`.

**Exemple attendu :**

```
pythonCopier le code>>> custom_sort(["apple", "bat", "zebra", "a", "antelope"])
['a', 'bat', 'apple', 'zebra', 'antelope']
```

---

### 

---

### **Partie 3 : Projet Django** 

> **Objectif :** Évaluer la capacité à construire une application Django fonctionnelle pour l’analyse énergétique.

#### Sujet : Tableau de bord énergétique

**Énoncé :**  
Créer une application Django permettant d’afficher et de visualiser des données énergétiques.

**Fonctionnalités demandées :**

1. **Modèle Django** :
   * Créer un modèle `EnergyData` avec les champs suivants : 
     * `date` : Date.
     * `region` : Nom de la région.
     * `consumption_twh` : Quantité consommée (float).
2. **Interface utilisateur :**
   * Une page permettant : 
     * D’importer des données à partir d’un fichier CSV (celui présenté plus haut par exemple)
     * D’afficher un tableau listant les données importées (avec pagination).
     * De visualiser des graphiques interactifs montrant : 
       * La consommation par région.
       * La consommation en France par année.
3. **API REST (bonus) :**
   * Créer une API REST pour récupérer les données sous forme JSON.

**Livrables :**

* Code source dans un dépôt Git.
* Instructions pour lancer l’application (fichier `README.md`).

**Critères d’évaluation :**

* Fonctionnalité de l’application.
* Clarté et lisibilité du code.
* Utilisation des bonnes pratiques Django.
* Implémentation correcte des fonctionnalités demandées.

---

### Pas de stress, nous n'attendons pas une copie parfaite mais de mieux comprendre dans quelle mesure vous pourrez vous adaptez à nos sujets.

---