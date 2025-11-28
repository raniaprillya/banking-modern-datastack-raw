

SELECT
    t.transaction_id,
    t.account_id,
    a.customer_id,
    t.amount,
    t.related_account_id,
    t.status,
    t.transaction_type,
    t.transaction_time,
    CURRENT_TIMESTAMP AS load_timestamp
FROM banking.analytics.stg_transactions t
LEFT JOIN banking.analytics.stg_accounts a
    ON t.account_id = a.account_id