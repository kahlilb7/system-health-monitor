# ============================================================
# Kahlil Batieste
# 04/16/2026
# Project 3: System Health Monitor
#
# Defines custom exception classes used for handling service
# failures and threshold violations across the monitoring system.
# ============================================================

class ServiceUnavailableError(Exception):
    """
    Raised when a service cannot be reached.
    """
    pass


class DataCorruptionError(Exception):
    """
    Raised when returned service data is corrupted.
    """
    pass


class ConnectionTimeoutError(Exception):
    """
    Raised when a service connection times out.
    """
    pass


class ThresholdExceededError(Exception):
    """
    Raised when a metric exceeds its allowed threshold.
    """
    pass