import hashlib
import secrets
import logging
import os

# log recorder
logging.basicConfig(level=logging.INFO)

def login(password):
    
    # use secrets.randbelow 
    session_token = secrets.randbelow(9000) + 1000
    
    # use sha-256
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    
	#delete unused variable1
	#unused_variable = "This is dead code"
    
	#read the ip from environment variable
    db_ip = os.getenv("DATABASE_IP", "127.0.0.1")
    
    
    try:
        logging.info("Connecting to database at %s", db_ip)
    except Exception as e:
        logging.exception("Failed to connect to the database: %s", e)
        
    return {
        "status": "success",
        "session_token": session_token,
        "password_hash": hasher.hexdigest()
    }
