SELECT
    utbildningsnamn,
    utbildningsområde,
    "yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet",
    kommun INTO it_educations
FROM
    myh_2024
WHERE
    utbildningsområde = 'Data/IT';

SELECT
    COUNT(*)
FROM
    it_educations;

SELECT
    *
FROM
    it_educations
WHERE
    LOWER(utbildningsnamn) LIKE '%data eng%';