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

# thresholds for each system
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0


# ============================================================
# Step 1: CPU Check Function 
# ============================================================

def check_cpu():
    """
    Gets CPU metrics, checks if usage is too high,
    and returns the result.

    Parameters:
        None

    Returns:
        dict: includes status and cpu data or error message
    """
    try:
        # get cpu data from cpu_monitor
        data = cpu_monitor.get_cpu_metrics()

        # check if usage goes exceeds threshold
        if data["usage_percent"] > CPU_THRESHOLD:
            raise ThresholdExceededError("CPU usage exceeded the allowed threshold.")

        # return success result
        return {"status": "ok", "data": data}

    except ServiceUnavailableError as error:
        # handle case where cpu service is down
        return {"status": "error", "data": str(error)}


# ============================================================
# Step 2: Memory Check Function
# ============================================================

def check_memory():
    """
    Gets memory metrics, checks if usage is too high,
    and returns the result.

    Parameters:
        None

    Returns:
        dict: includes status and memory data or error message
    """
    try:
        # get memory data from memory_monitor
        data = memory_monitor.get_memory_metrics()

        # check if memory is full
        if data["usage_percent"] > MEMORY_THRESHOLD:
            raise ThresholdExceededError("Memory usage exceeded the allowed threshold.")

        # return success result
        return {"status": "ok", "data": data}

    except DataCorruptionError as error:
        # handle corrupted data case
        return {"status": "error", "data": str(error)}


# ============================================================
# Step 3: Network Check Function 
# ============================================================

def check_network():
    """
    Gets network metrics, checks if usage is too high,
    and returns the result.

    Parameters:
        None

    Returns:
        dict: includes status and network data or error message
    """
    try:
        # get network data from network_monitor
        data = network_monitor.get_network_metrics()

        # check if network usage is exceeded
        if data["usage_percent"] > NETWORK_THRESHOLD:
            raise ThresholdExceededError("Network usage exceeded the allowed threshold.")

        # return success result
        return {"status": "ok", "data": data}

    except ConnectionTimeoutError as error:
        # handle timeout case
        return {"status": "error", "data": str(error)}


# ============================================================
# Step 4: Run All Checks (Aggregate Results)
# ============================================================

def run_checks():
    """
    Runs all three service checks and returns the results together.

    Parameters:
        None

    Returns:
        dict: includes cpu, memory, and network results
    """
    # run each check and store results together
    results = {
        "cpu": check_cpu(),
        "memory": check_memory(),
        "network": check_network()
    }

    return results


# ============================================================
# Step 5: Log Results to File 
# ============================================================

def log_results(results, filepath):
    """
    Writes monitoring results to a log file.

    Parameters:
        results (dict): the results from run_checks()
        filepath (str): path to the log file

    Returns:
        None
    """
    try:
        # open file in append mode so we don't overwrite previous runs
        with open(filepath, "a") as file:
            file.write("Monitoring Results:\n")

            # loop through results and write each one
            for key in results:
                file.write(f"{key}: {results[key]}\n")

    finally:
        # always write completion message even if something goes wrong
        with open(filepath, "a") as file:
            file.write("Log complete\n\n")


# ============================================================
# Step 6: Generate Report (Formatted Output Summary)
# ============================================================

def generate_report(results):
    """
    Builds a simple report string from the results.

    Parameters:
        results (dict): results from run_checks()

    Returns:
        str: formatted report of system status
    """
    report = "System Health Report\n"
    report += "---------------------\n"

    # go through each service and add its info
    for key in results:
        report += f"{key.upper()}:\n"
        report += f"  Status: {results[key]['status']}\n"

        # only show data if it exists
        if "data" in results[key]:
            report += f"  Data: {results[key]['data']}\n"

        report += "\n"

    return report


# ============================================================
# Step 7: Main Function (Run Monitor and Display Results)
# ============================================================

def main():
    """
    Runs the monitor, prints the report,
    and logs the results to a file.

    Parameters:
        None

    Returns:
        None
    """
    results = run_checks()
    report = generate_report(results)

    print(report)
    log_results(results, "monitor.log")


if __name__ == "__main__":
    main()
    