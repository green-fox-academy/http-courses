A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!
***
14. feladat
CREATE DATABASE `csudijo` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;

***
16. feladat
SELECT COUNT(etel) AS "etelek-szama"
FROM termekek
WHERE etel = 1;

***
17. feladat
SELECT termekek.nev, ar
FROM termekek JOIN kategoriak ON kategoriaId = kategoriak.id
WHERE kategoriak.nev = "Desszertek"
ORDER BY termekek.nev;

***
18. feladat

***
19. feladat

***
20. feladat

