"""Read-only Reddit MCP starter. Requires approved Reddit API access."""
import os
import praw
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("ChloeLux Reddit (read-only)")

def reddit_client():
    required = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError("Missing environment variables: " + ", ".join(missing))
    return praw.Reddit(client_id=os.environ["REDDIT_CLIENT_ID"],
                       client_secret=os.environ["REDDIT_CLIENT_SECRET"],
                       user_agent=os.environ["REDDIT_USER_AGENT"])

@mcp.tool()
def recent_public_posts(username: str = "MickoMrk", limit: int = 5) -> list[dict]:
    """List recent public submissions for a Reddit account. Does not post or modify data."""
    if not 1 <= limit <= 25:
        raise ValueError("limit must be between 1 and 25")
    reddit = reddit_client()
    return [{"title": post.title, "subreddit": str(post.subreddit),
             "url": "https://www.reddit.com" + post.permalink,
             "score": post.score, "comments": post.num_comments}
            for post in reddit.redditor(username).submissions.new(limit=limit)]

if __name__ == "__main__":
    mcp.run(transport="stdio")
