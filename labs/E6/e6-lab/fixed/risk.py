def accept_exception(exc):
    return bool(exc.get('owner') and exc.get('review_by') and exc.get('wcag_checked'))
