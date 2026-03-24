import random
import time
from datetime import datetime

JOBS = ["extract_transactions", "validate_accounts", "load_summary", "reconcile_balances"]

def run_job(job_name):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting job: {job_name}")
    time.sleep(random.uniform(0.5, 2.0)) # Simulate job processing time
    status = random.choices(["SUCCESS", "FAILED"], weights=[80, 20])[0]
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {job_name} -> {status}")
    return status

def run_pipeline():
    print("\n===== PIPELINE RUN STARTED =====")
    results = {}
    for job in JOBS:
        results[job] = run_job(job)
    print("\n===== PIPELINE RUN SUMMARY =====")
    for job, status in results.items():
        icon = "✅" if status == "SUCCESS" else "❌"
        print(f"{icon} {job}: {status}")
    print ("==================================\n")
    
if __name__ == "__main__":
    run_pipeline()
    
