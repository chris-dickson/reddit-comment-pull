import sys
import praw
import json

client_id = sys.argv[1]
client_secret = sys.argv[2]
user_agent = 'reddit-comment-pull'

# Create the reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,user_agent=user_agent)

# Get the submission
submission = reddit.submission(id='3g1jfi')
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    serializedComment = {}
    serializedComment['type'] = 'Comment'
    serializedComment['author'] = '[deleted]' if comment.author is None else comment.author.name
    serializedComment['body'] = comment.body
    serializedComment['created'] = comment.created_utc
    serializedComment['score'] = comment.score
    serializedComment['stickied'] = comment.stickied
    serializedComment['parent_id'] = comment.parent_id
    serializedComment['id'] = comment.id
    serializedComment['edited'] = comment.edited
    serializedComment['guilded'] = comment.gilded
    serializedComment['permalink'] = submission.permalink + comment.id
    commentJSON = json.dumps(serializedComment)
    print(commentJSON)