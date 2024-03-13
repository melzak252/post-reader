import praw

from dataclasses import dataclass
from pathlib import Path

from config import Config

from typing import Iterable

config = Config.from_toml(Path("config.toml"))

@dataclass(frozen=True, slots=True)
class RedditPost:
    author: str
    title: str
    content: str
    no_comments: int   
    
reddit = praw.Reddit(
    client_id=config.praw.client_id,
    client_secret=config.praw.client_secret,
    user_agent=config.praw.user_agent,
    username=config.praw.username,
    password=config.praw.password
)

subred: praw.reddit.Subreddit = reddit.subreddit("Genshin_Impact")
submissions: Iterable[praw.reddit.Submission] = subred.new(limit=20)

posts = []
for submission in submissions:
    reddit_post = RedditPost(
        author=submission.author.name,
        title=submission.title.strip(),
        content=submission.selftext.strip(),
        no_comments=submission.num_comments
    )
    posts.append(reddit_post)
    
print(posts)