from werkzeug.security import generate_password_hash, check_password_hash
from database import UpdateDatabase


def password_encryption(password):
    hash_password = generate_password_hash(
        password,
        method='pbkdf2:sha256',
        salt_length=8
    )
    return hash_password


def check_password(data_password, password_to_check):
    # user_password = password_encryption(user_password)
    if check_password_hash(data_password, password_to_check):
        return True
    else:
        return False

# password = password_encryption('Admin123!@#')
# admin = UpdateDatabase('instance/data.sql', 'admin@gmail.com', 'Admin123!@#')
# admin.update_password(password)
# # result = check_password(password, 'Wampir123!')
# print(password)