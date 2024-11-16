import praw

reddit = praw.Reddit(
    client_id="id",
    client_secret="",
    user_agent = "FragranceFinderBot 1.0 by /u/im_a_lost_child",
    username="im_a_lost_child",
    password="password"
)

subreddit = reddit.subreddit("MontagneParfums")

perfume_name = input("What are you looking for: ").lower()
find = False

for submission in subreddit.new(limit=10):
    title = submission.title.lower()
    post = submission.selftext.lower()
    sale = "Wts".lower()

    if sale in title and (perfume_name in title or perfume_name in post):
        print(f"Found a match: {submission.title}, Link: {submission.url}")
        find = True
        
        # Notify yourself on Reddit
        try:
            reddit.redditor("im_a_lost_child").message(
                subject="Perfume Listing Found!",
                message=f"We found a listing: {submission.title}\n\nLink: {submission.url}"
            )
        except praw.exceptions.RedditAPIException as e:
            print(f"Error sending message: {e}")

if find == False:
    print("None found")
