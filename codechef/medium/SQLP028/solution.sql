-- your code goes here
SELECT DISTINCT
    p.player_id,
    p.player_name,
    p.level,
    p.experience_points
FROM
    players p
JOIN 
    characters c ON p.player_id = c.player_id
WHERE
    c.race = 'Elf';