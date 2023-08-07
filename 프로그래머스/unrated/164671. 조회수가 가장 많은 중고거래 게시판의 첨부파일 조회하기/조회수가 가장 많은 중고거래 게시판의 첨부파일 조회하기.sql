SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', B.FILE_ID, B.FILE_name, B.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS A
RIGHT OUTER JOIN USED_GOODS_FILE AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE A.VIEWS = (SELECT MAX(A.VIEWS)
                FROM USED_GOODS_BOARD AS A)
ORDER BY B.FILE_ID DESC