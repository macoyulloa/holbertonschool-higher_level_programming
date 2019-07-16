-- updates the score of Bob 
-- MySQL server
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY 1 DESC;
