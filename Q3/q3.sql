SELECT o.owner_id as owner_id,
    o.owner_name as owner_name,
    COUNT(DISTINCT cam.category_id) as different_category_count
FROM owner o
    LEFT JOIN article a ON o.owner_id = a.owner_id
    LEFT JOIN category_article_mapping cam ON a.article_id = cam.article_id
GROUP BY o.owner_id
ORDER BY different_category_count DESC;