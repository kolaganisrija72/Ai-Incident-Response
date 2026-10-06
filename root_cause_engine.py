def find_root_cause(data):

    text = (
        data["incident"] + " " +
        data["service"]
    ).lower()

    if any(x in text for x in ["database", "sql", "mysql"]):
        return "Possible database availability or performance failure."

    if any(x in text for x in ["payment", "transaction", "gateway"]):
        return "Possible payment gateway or transaction processing failure."

    if any(x in text for x in ["network", "connection", "timeout"]):
        return "Possible network connectivity or service communication failure."

    if any(x in text for x in ["server", "cpu", "memory"]):
        return "Possible server resource or infrastructure failure."

    if any(x in text for x in ["security", "attack", "malware"]):
        return "Possible security event requiring immediate investigation."

    return "Root cause requires further log and system investigation."