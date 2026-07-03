-- View all records
SELECT * FROM news_data;

-- Count total news articles
SELECT COUNT(*) AS total_news
FROM news_data;

-- Count news by sentiment
SELECT sentiment, COUNT(*) AS total
FROM news_data
GROUP BY sentiment;

-- Show only positive news
SELECT *
FROM news_data
WHERE sentiment = 'Positive';

-- Show only negative news
SELECT *
FROM news_data
WHERE sentiment = 'Negative';

-- Show only neutral news
SELECT *
FROM news_data
WHERE sentiment = 'Neutral';