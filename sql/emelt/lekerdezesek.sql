A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!
***
14. feladat
CREATE DATABASE `csudijo` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci ;

***
16. feladat
SELECT COUNT(*) AS 'etelek-szama' FROM termekek
WHERE etel = 1;

***
17. feladat
SELECT termekek.nev, ar
FROM termekek, kategoriak
WHERE termekek.kategoriaId = kategoriak.id
AND kategoriak.nev = 'Desszertek'
ORDER BY termekek.nev;

***
18. feladat
INSERT INTO `termekek` (`nev`, `ar`, `etel`, `kategoriaId`) VALUES
('Málnahabos pohárkrém', '1090.00', 1, 6)

***
19. feladat
SELECT termekNev AS 'nev', ROUND(SUM(mennyiseg), 0) AS 'mennyiseg'
FROM rendelesek, termekek
WHERE rendelesek.termekId = termekek.id
AND MONTH(datum) = 2
AND etel = 1
GROUP BY termekNev
ORDER BY mennyiseg DESC
LIMIT 3;

***
20. feladat

