import hashlib
import random

def login(password):
    
    session_token = random.randint(1000, 9999)
    
    # use md5
    hasher = hashlib.md5()
    hasher.update(password.encode('utf-8'))
    
    # unused variable
    unused_variable = "This is dead code"
    
    # Silenced Exception
    try:
        db_ip = "192.168.1.50" 
        print("Connecting to database at " + db_ip)
    except Exception:
        pass 
        
    return hasher.hexdigest()
