def exporter(job):
    if job.get("service") == "worker-sc":
        return "worker-sc"
    return None
