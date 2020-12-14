from instapy import InstaPy

username = "username" 
password = "password"

session = InstaPy(username=username, password=password)
session.login()

#my_following = session.grab_following(username=username, amount="full", live_match=True, store_locally=True)
#my_followers = session.grab_followers(username=username, amount="full", live_match=False, store_locally=True)
#all_unfollowers, active_unfollowers = session.pick_unfollowers(username=username, compare_by="day", compare_track="first", live_match=True, store_locally=True, print_out=True)

hashtags = session.target_list("/Users/alessandrotola/InstaPy/logs/al_tola_/relationship_data/al_tola_/hashtag/hashtag.txt")
session.like_by_tags(hashtags, amount=10)