class UserAuthentication:
    def login(self, username, password):
        
        # Hardcoded password
        db_password = "superSecretPassword123"

        # unused variable
        login_attempts = 0

        # redundant if-else
        if username == "admin":
            if password == db_password:
                return True
            else:
                return False
                
        return False