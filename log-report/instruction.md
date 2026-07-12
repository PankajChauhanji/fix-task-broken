There is an access log (`access.log`) in the working directory. Analyze the traffic and summarize what you find. 
Save your findings to exactly `/app/report.json` as a valid JSON object satisfying these numbered success criteria:

1. The JSON object contains a `total_requests` key with the total number of requests in the log file.
2. The JSON object contains a `unique_ips` key with the total number of unique client IP addresses involved.
3. The JSON object contains a `top_path` key with the single most frequently requested path.
