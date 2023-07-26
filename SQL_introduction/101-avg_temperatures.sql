-- Advanced task
-- Display the average temperature by city ordered by temperature (descending).

SELECT city, AVG(value) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
