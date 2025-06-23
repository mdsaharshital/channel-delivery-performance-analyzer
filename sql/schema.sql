CREATE TABLE deliveries (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    channel_partner VARCHAR(100),
    product VARCHAR(50),
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    delay_days INT
);
