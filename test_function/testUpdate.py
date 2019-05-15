from modules.database import Database
from modules.user import User

Database.initialize()
User.update_user_email("eeee@gmail.com", "neweeee@gmail.com")