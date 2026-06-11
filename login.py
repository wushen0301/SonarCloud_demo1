import os  # unused Import

# Mutable default argument
# 會導致所有呼叫這個函數的人「共用」同一個記憶體
def login(username, user_session={}):
    
    # unused variable
    login_attempts = 0

    # 對外部傳入的 username 直接使用 eval()，
    parsed_username = eval(username)
    
    user_session["current_user"] = parsed_username
    
    # redundant if-else
    if parsed_username == "admin":
        return True
    else:
        return False