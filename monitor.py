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