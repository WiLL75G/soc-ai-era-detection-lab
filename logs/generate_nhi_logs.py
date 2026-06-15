import json
import random
from datetime import datetime, timedelta

service_accounts = ["svc_billing_api", "svc_hr_sync", "svc_ai_agent_01", "svc_crm_connector"]
normal_ips = ["10.0.1.45", "10.0.1.46", "10.0.1.47"]
malicious_ip = "185.220.101.34"
endpoints = ["/api/v1/users", "/api/v1/billing", "/api/v1/reports", "/api/v1/admin/export"]

logs = []

for i in range(80):
    logs.append({
        "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 72))).strftime("%Y-%m-%dT%H:%M:%S"),
        "account": random.choice(service_accounts[:3]),
        "source_ip": random.choice(normal_ips),
        "endpoint": random.choice(endpoints[:2]),
        "records_accessed": random.randint(1, 50),
        "status": "SUCCESS",
        "alert": False
    })

for i in range(20):
    logs.append({
        "timestamp": datetime.now().replace(hour=random.randint(1, 4), minute=random.randint(0, 59)).strftime("%Y-%m-%dT%H:%M:%S"),
        "account": "svc_ai_agent_01",
        "source_ip": malicious_ip,
        "endpoint": "/api/v1/admin/export",
        "records_accessed": random.randint(800, 2000),
        "status": "SUCCESS",
        "alert": True
    })

random.shuffle(logs)

with open("logs/nhi_logs.json", "w") as f:
    json.dump(logs, f, indent=2)

print(f"Successfully generated {len(logs)} log entries")
print(f"Normal entries: 80")
print(f"Malicious entries: 20")
print(f"Saved to: logs/nhi_logs.json")