-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 1. feladat:
CREATE DATABASE `napsutes` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;

-- 3. feladat:
UPDATE regiok
SET regioNev = "Észak-Írország"
WHERE regioNev = "Észak Írország";

-- 4. feladat:
SELECT COUNT(*) AS "rekordszam", ROUND(AVG(perc), 2) AS "atlag"
FROM meresek;

-- 5. feladat:
SELECT ev, ROUND(SUM(perc) / 60, 1) AS "orak"
FROM regiok JOIN meresek ON regiok.id = meresek.regioId
WHERE regioNev = "Anglia"
AND ev BETWEEN 1990 AND 2000
GROUP BY ev
ORDER BY ev DESC;

-- 6. feladat:
SELECT ev, perc, regioNev AS "terulet"
FROM regiok, meresek
WHERE regiok.id = meresek.regioId
AND ho = 2
AND PERC > 6000
ORDER BY PERC DESC;
