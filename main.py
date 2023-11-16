import instaloader

def ProfilePic(username):
    # if 
    loader = instaloader.Instaloader()
    loader.download_profile(username, profile_pic_only=True)

username = input("Enter Instagram Username: ")
ProfilePic(username)