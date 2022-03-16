
CREATE TABLE Livre(
	idLivre         INT NOT NULL ,
	titre           VARCHAR (50) NOT NULL ,
	format          VARCHAR (50) NOT NULL ,
	type            VARCHAR (25) NOT NULL ,
	auteur          VARCHAR (50) NOT NULL ,
	datePublication TIMESTAMP DEFAULT CURRENT_TIMESTAMP  NOT NULL ,
	description     VARCHAR (5000) NOT NULL ,
	idGenre         INT  NOT NULL ,
	idImage         INT  NOT NULL ,
	CONSTRAINT prk_constraint_Livre PRIMARY KEY (idLivre)
);



CREATE TABLE Utilisateur(
	idUtilisateur INT NOT NULL ,
	nom           VARCHAR (50) NOT NULL ,
	login         VARCHAR (50) NOT NULL UNIQUE,
	email         VARCHAR (250) NOT NULL ,
	mdp           VARCHAR (500) NOT NULL ,
	adresse       VARCHAR (500) NOT NULL ,
	numTel        INT  NOT NULL ,
	role          INT  NOT NULL ,
	CONSTRAINT prk_constraint_Utilisateur PRIMARY KEY (idUtilisateur)
);



CREATE TABLE Genre(
	idGenre INT NOT NULL ,
	nom     VARCHAR (50) NOT NULL ,
	idImage INT  NOT NULL ,
	CONSTRAINT prk_constraint_Genre PRIMARY KEY (idGenre)
);



CREATE TABLE Image(
	idImage     INT NOT NULL ,
	cheminImage VARCHAR (1000) NOT NULL ,
	CONSTRAINT prk_constraint_Image PRIMARY KEY (idImage)
);


CREATE TABLE Note(
	idNote INT NOT NULL ,
	note   INT  NOT NULL ,
	CONSTRAINT prk_constraint_Note PRIMARY KEY (idNote)
);


CREATE TABLE EstNotee(
	idLivre INT  NOT NULL ,
	idNote  INT  NOT NULL ,
	CONSTRAINT prk_constraint_EstNotee PRIMARY KEY (idLivre,idNote)
);

ALTER TABLE Livre CHANGE idLivre idLivre INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Utilisateur CHANGE idUtilisateur idUtilisateur INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Genre CHANGE idGenre idGenre INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Image CHANGE idImage idImage INT(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Note CHANGE idNote idNote INT(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE Livre ADD CONSTRAINT FK_Livre_idGenre FOREIGN KEY (idGenre) REFERENCES Genre(idGenre);
ALTER TABLE Livre ADD CONSTRAINT FK_Livre_idImage FOREIGN KEY (idImage) REFERENCES Image(idImage);
ALTER TABLE Genre ADD CONSTRAINT FK_Genre_idImage FOREIGN KEY (idImage) REFERENCES Image(idImage);
ALTER TABLE EstNotee ADD CONSTRAINT FK_EstNotee_idLivre FOREIGN KEY (idLivre) REFERENCES Livre(idLivre);
ALTER TABLE EstNotee ADD CONSTRAINT FK_EstNotee_idNote FOREIGN KEY (idNote) REFERENCES Note(idNote);