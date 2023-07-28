-- Script to Count the number of shows per genre.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
