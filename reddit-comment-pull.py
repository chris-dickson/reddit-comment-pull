import sys
import praw

client_id = sys.argv[1]
client_secret = sys.argv[2]
user_agent = 'reddit-comment-pull'

# Create the reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,user_agent=user_agent)

# Get the submission
submission = reddit.submission(id='3g1jfi')
for top_level_comment in submission.comments:
    print(top_level_comment.body)