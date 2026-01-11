from collections import defaultdict
from datetime import datetime, timedelta

# Track failed login timestamps per IP
failed_attempts = defaultdict(list)

# Detection parameters
THRESHOLD = 3
TIME_WINDOW = timedelta(minutes=5)

with open("auth.log", "r") as file:
    for line in file:
        if "STATUS=FAIL" in line:
            # Extract timestamp
            timestamp_str = " ".join(line.split()[:2])
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Extract IP address
            ip = line.split("IP=")[1].split()[0]

            # Store the failure time for this IP
            failed_attempts[ip].append(timestamp)

print("Suspicious IPs detected:")

for ip, timestamps in failed_attempts.items():
    timestamps.sort()

    for i in range(len(timestamps)):
        window_start = timestamps[i]
        window_end = window_start + TIME_WINDOW

        # Count failures within the time window
        count = sum(
            1 for t in timestamps
            if window_start <= t <= window_end
        )

        if count >= THRESHOLD:
            print(f"{ip}: {count} failures within 5 minutes")
            break