-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 1. feladat:
CREATE DATABASE `napsutes` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;

-- 3. feladat:
-- SET SQL_SAFE_UPDATES = 0;
UPDATE regiok
SET regioNev = 'Észak-Írország'
WHERE regioNev = 'Észak Írország';

-- 4. feladat:
SELECT COUNT(*) AS 'rekordszam', ROUND(AVG(perc), 2) AS 'atlag'
FROM meresek;

-- 5. feladat:
SELECT ev, ROUND(SUM(perc) / 60, 1) AS orak
FROM meresek, regiok
WHERE meresek.regioId = regiok.id
AND regiok.regioNev = 'Anglia'
AND ev BETWEEN 1990 AND 2000
GROUP BY meresek.ev
ORDER BY ev DESC;

SELECT ev, ROUND(SUM(perc) / 60, 1) AS orak
FROM meresek INNER JOIN regiok
ON meresek.regioId = regiok.id
WHERE regiok.regioNev = 'Anglia'
AND ev BETWEEN 1990 AND 2000
GROUP BY meresek.ev
ORDER BY ev DESC;

-- 6. feladat:
SELECT ev, perc, regiok.regioNev AS 'terulet'
FROM meresek INNER JOIN regiok
ON meresek.regioId = regiok.id
WHERE ho = 2
AND perc > 6000
ORDER BY perc DESC;
