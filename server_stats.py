# /// script
# dependencies = ["psutil"]
# ///

# To run this script, you will be needed `uv` and `python` to be installed in the server. Visit https://docs.astral.sh/uv/getting-started/installation/ for the installation guide for uv.
# After installation, run the command `uv run <filename>` 

import psutil
import platform
from datetime import datetime

def get_size(bytes):
    """Scale bytes to a readable format (e.g., MB, GB)"""
    factor = 1024
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}"
        bytes /= factor

print(f"--- Server Report: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

# 1. CPU Stats
print(f"\n[CPU]")
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Total cores:    {psutil.cpu_count(logical=True)}")
print(f"Total Usage:    {psutil.cpu_percent()}%")

# 2. Memory Stats
print(f"\n[Memory]")
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Used:  {get_size(svmem.used)} ({svmem.percent}%)")
print(f"Available: {get_size(svmem.available)}")

# 3. Disk Stats
print(f"\n[Disk Usage]")
partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Mount: {partition.mountpoint} | Total: {get_size(usage.total)} | Used: {usage.percent}%")
    except PermissionError:
        continue

# 4. Network Stats
print(f"\n[Network]")
net_io = psutil.net_io_counters()
print(f"Total Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Received: {get_size(net_io.bytes_recv)}")
