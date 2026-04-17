# ============================================================
# Kahlil Batieste
# 04/16/2026
# Project 3: System Health Monitor
#
# Implements system health checks, handles exceptions from
# service modules, logs results, and generates status reports.
# ============================================================

import cpu_monitor
import memory_monitor
import network_monitor

from exceptions import (
    ServiceUnavailableError,
    DataCorruptionError,
    ConnectionTimeoutError,
    ThresholdExceededError,
)

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0

# ============================================================
# Step 1: CPU Check Function (Service Call and Threshold Check)
# ============================================================

def check_cpu():
    """
    Checks CPU health metrics and returns the result.

    Parameters:
        None

    Returns:
        dict: A dictionary with the check status and CPU data.
    """
    try:
        data = cpu_monitor.get_cpu_metrics()

        if data["usage_percent"] > CPU_THRESHOLD:
            raise ThresholdExceededError("CPU usage exceeded the allowed threshold.")

        return {"status": "ok", "data": data}

    except ServiceUnavailableError as error:
        return {"status": "error", "data": str(error)}