import time
__author__ = "Steven Lee"

user, pw = "stevenlee", "abc123"


def auth(auth_type):
    print("auth func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                print("wrapper func args:", *args, **kwargs)
                username = input("Username:").strip()
                password = input("Password:").strip()

                if username == user and password == pw:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    func(*args, **kwargs)
                else:
                    print("\033[31;1mInvalid username or password\033[0m")
                    exit()
            elif auth_type == "ldap":
                func()
                print("ldap,exit")

        return wrapper
    return outer_wrapper


def index():
    print("welcome to index page")


@auth(auth_type = "local")
def home():
    print("welcome to home page")


@auth(auth_type = "ldap")
def bbs():
    print("welcome to bbs page")

index()
home()  # wrapper
bbs()
