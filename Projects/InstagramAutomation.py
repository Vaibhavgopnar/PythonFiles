from instabot import Bot
bot = Bot()
bot.login(username="vaibhavpatil2169",password="8459056689")

# bot.follow('shadow.l0ve')   # follow

# upload
# bot.upload_photo("C:/Python Files/wishlist.jpg",caption="Wishlist")

# unfollow
# bot.unfollow("shadow.l0ve")

# message multiple people
# bot.send_message('I love python',["user1 username","user2 username"])

# Info about followers
followers = bot.get_user_followers("vaibhavpatil2169")
for follower in followers:
    print(bot.get_user_info(follower))

# Info about following
following = bot.get_user_following("vaibhavpatil2169")
for Following in following:
    print(bot.get_user_info(Following))
