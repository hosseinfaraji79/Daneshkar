import uuid
import hashlib
import os

class User:
    def hash_password(password: str, salt: str) -> str:
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)


    users = []
    usernames = []
    ids = []
    hashes = []
    salts = []
    user_info = {}

    def __init__(self, username: str, password: str, phone_number: str = None):
        self.username, self.password = username, password
        self.user_id = User.uuid_generator(username)
        self.salt = os.urandom(64)
        self.phone_number = phone_number
        self.password = User.hash_password(password, self.salt)
        User.users.append(self)
        User.usernames.append(username)
        User.ids.append(self.user_id)
        User.hashes.append(self.password)

    def __str__(self):
        return f"Username: {self.username}\n\tPhone Number: {self.phone_number}\n\tUser ID: {self.user_id}"

    def password_login_check(self, passwd):
        new_key = User.hashing(passwd, self.salt)
        if not new_key == self.password:
            raise Exception("Wrong Password! ")

    def sign_in_validation(cls, user_name: str, password: str) -> bool:
        if user_name not in cls.usernames:
            raise Exception("Username not found! ")
        for user in cls.usernames:
            if user_name == user:
                class_object = User.get_obj(user_name)
        class_object.password_login_check(password)
        return class_object

    def signup(cls, user_name: str, passwd: str, ph_numb: str = None):
        obj = cls(user_name, passwd, ph_numb)
        User.user_info[obj] = user_name

    def get_obj(user_name: str):
        for obj in User.users:
            if obj.username == user_name:
                return obj

    def show(self):
        print(self)

    def username_check(user_name: str) -> bool:
        if user_name in User.usernames:
            return False
        return True

    def update_user(self, user_name: str = None, phone_num: str = None):
        if user_name in User.usernames:
            raise Exception("Username already Taken! ")
        if user_name != "":
            User.usernames.remove(self.username)
            self.username = user_name
            User.usernames.append(self.username)
            User.user_info[self] = user_name
        if phone_num != "":
            self.phone_number = phone_num

    def passwd_change(self, old_pass: str, new_pass: str, again_new_key: str):
        old_key = User.hash_password(old_pass, self.salt)
        new_key = User.hash_password(new_pass, self.salt)
        again_new_key = User.hash_password(again_new_key, self.salt)
        if old_key != self.password:
            raise Exception("Wrong original Password! ")
        if new_key != again_new_key:
            raise Exception("Unmatched new passwords")
        User.hashes.remove(self.password)
        self.password = new_key
        User.hashes.append(self.password)

    def username(self):
        return self._username

    @username.setter
    def username(self, user_value):
        if not User.username_check(user_value):
            raise Exception("Username is already taken! ")
        self._username = user_value

    def password_check(passwd: str) -> bool:
        if len(passwd) < 4:
            return False
        return True

    def password(self):
        return self.__password

    @password.setter
    def password(self, passwd_value):
        if not User.password_check(passwd_value):
            raise Exception("Too short Password! ")
        self.__password = passwd_value

    @staticmethod
    def uuid_generator(name: str) -> str:
        hash_str = uuid.uuid1()
        return uuid.uuid5(hash_str, name)