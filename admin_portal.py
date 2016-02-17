from portal_db_reader import PortalDBReader
from user import User

db_reader = PortalDBReader()
logged_in = False

while not logged_in:
    print("Please log in with your username and password.")
    user = User()
    if user.login(db_reader):
        print("Successfully logged in as {}".format(user.username))
        logged_in = True

    while logged_in:
        choice = input("You may\n(1) logout\n(2) create new user\n>> ")
        if choice == "1":
            logged_in = user.logout()
            db_reader = PortalDBReader()
        elif choice == "2":
            new_user = user.create_new_user()
            db_reader.append_to_file(new_user)
