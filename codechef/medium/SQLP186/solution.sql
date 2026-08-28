SELECT
    U.user_name AS user_name,
    COUNT(F.singer_id) AS Total_count
FROM Follower F
JOIN User U ON U.user_id =F.user_id
GROUP BY F.user_id, U.user_name
ORDER BY F.user_id;