# Cleans expired sessions from DB
def sessionCleaner():
    tmp = get_expired_sessions()
