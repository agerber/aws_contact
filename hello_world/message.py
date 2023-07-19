class Message:
    def __init__(self, subject, body, email):
        self.subject = subject
        self.body = body
        self.email = email


    def __str__(self):
        return f"Message{{subject='{self.subject}', body='{self.body}', email='{self.email}'}}"
