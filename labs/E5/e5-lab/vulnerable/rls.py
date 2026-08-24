def tenant_for(session, body):
    return body.get('tenant', session['tenant'])
