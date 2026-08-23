def exporter(job):
    return job.get('service') if job.get('service')=='worker-sc' else None
