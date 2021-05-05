CREATE TABLE User (firstName VARCHAR(64),
lastName VARCHAR(64),
email VARCHAR(64),
password_hash REAL,
ID INTEGER PRIMARY KEY
);

CREATE TABLE Sores (Mod_1 INTEGER
Mod_2 INTEGER
Mod_3 INTEGER
finalScore INTEGER
totalScore INTEGER
Score_ID INTEGER 
FOREIGN KEY(ID) REFERENCES User (ID)

)

CREATE TRIGGER average AFTER UPDATE
ON Sores
BEGIN
UPDATE totalScore SET
           totalScore = ((new.Mod_1 + new.Mod_2 + new.Mod_3 + new.finalScore) / 4) * 100;
END ;