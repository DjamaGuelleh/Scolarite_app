
use projet_devops;

CREATE TABLE filiere (
  id_filiere int PRIMARY KEY,
  intitule varchar(100) NOT NULL
) ;

CREATE TABLE users (
  id int PRIMARY KEY,
  mdp varchar(100) NOT NULL
) ;


CREATE TABLE etudiant (
  id int  PRIMARY KEY,
  nom varchar(100) NOT NULL,
  prenom varchar(100) NOT NULL,
  id_filiere int , 
   FOREIGN KEY (id) REFERENCES users(id),
   FOREIGN KEY (id_filiere) REFERENCES filiere(id_filiere)
);
CREATE TABLE `matiere` (
  `id_matiere` int NOT NULL PRIMARY KEY,
  `id_filiere` int NOT NULL,
  `nom` varchar(100) NOT NULL,
  FOREIGN KEY (id_filiere) REFERENCES filiere(id_filiere)
);

CREATE TABLE `professeur` (
  `id_professeur` int NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
   FOREIGN KEY (id_professeur) REFERENCES users(id)
);


CREATE TABLE `note` (
  id_matiere int ,
  id_filiere int ,
  cne int ,
  note float ,
  FOREIGN KEY (cne) REFERENCES users(id),
  FOREIGN KEY (id_filiere) REFERENCES filiere(id_filiere)
);
