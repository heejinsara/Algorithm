WITH DATA1 AS(SELECT WRITER_ID, COUNT(WRITER_ID) AS CNT
              FROM USED_GOODS_BOARD
              GROUP BY WRITER_ID
              HAVING CNT>=3)

SELECT USER_ID, NICKNAME,
CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS 전체주소,
CONCAT(LEFT(TLNO,3),'-',SUBSTRING(TLNO,4,4),'-',RIGHT(TLNO,4)) AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT WRITER_ID
                  FROM DATA1)
ORDER BY USER_ID DESC