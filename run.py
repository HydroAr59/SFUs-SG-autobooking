try:
    from userDefined import *
    import browserDriver
    import threading
except:
    print("Something went wrong")

def room_book(browsers):

    print("Booking rooms on desired times...")
    browsers[0].book_room()

if __name__ == '__main__':

    browsers = []
    print("Initializing. Please wait.")

    for x in range(num_accounts):
        browsers.append(browserDriver.browser())
        browsers[x].cas_login(accounts[x]["username"], accounts[x]["password"])

    print("Complete.")

    room_book(browsers)


