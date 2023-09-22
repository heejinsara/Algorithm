SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS AS A
LEFT OUTER JOIN ANIMAL_INS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NOT NULL
AND B.ANIMAL_ID IS NULL