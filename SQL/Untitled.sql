DROP TABLE IF EXISTS engagement;

CREATE TABLE engagement (
    engagement_id INT,
    customer_id VARCHAR(20),
    month DATE,
    watch_hours DECIMAL(10,2),
    login_days INT,
    num_titles_watched INT,
    PRIMARY KEY (engagement_id)
);
SELECT COUNT(*) FROM customers;
