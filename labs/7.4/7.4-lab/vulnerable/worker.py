def exporter(job):
    return job.get('user_session') or job.get('service')
