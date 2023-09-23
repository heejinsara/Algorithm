SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER,
COUNT(DISTINCT B.USER_ID) AS USERS
FROM USER_INFO AS A
INNER JOIN ONLINE_SALE AS B
ON A.USER_ID=B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER