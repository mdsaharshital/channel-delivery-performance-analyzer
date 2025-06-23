-- Query 1: Average delay by channel partner
SELECT 
    channel_partner,
    ROUND(AVG(delay_days), 2) AS avg_delay,
    COUNT(*) AS total_deliveries
FROM deliveries
GROUP BY channel_partner
ORDER BY avg_delay DESC;

-- Query 2: Average delay by city
SELECT 
    city,
    ROUND(AVG(delay_days), 2) AS avg_delay,
    COUNT(*) AS total_deliveries
FROM deliveries
GROUP BY city
ORDER BY avg_delay DESC;

-- Query 3: Products with deliveries delayed by more than 2 days
SELECT 
    product,
    COUNT(*) AS late_deliveries
FROM deliveries
WHERE delay_days > 2
GROUP BY product
ORDER BY late_deliveries DESC;
