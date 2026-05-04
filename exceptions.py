"""
Custom Exception Definitions for System Health Monitor

This module defines exception classes used to handle service failures
and threshold violations across the monitoring system.

Author: Kahlil Batieste
"""

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