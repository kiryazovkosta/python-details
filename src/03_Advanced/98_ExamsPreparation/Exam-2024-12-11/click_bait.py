from collections import deque

links = deque([int(n) for n in input().split()])
articles = [int(n) for n in input().split()]
target = int(input())

feeds = []

while links and articles:
    link = links.popleft()
    article = articles.pop()

    if article > link:
        remainder = article % link
        feeds.append(remainder)
        if remainder != 0:
            articles.append(remainder * 2)
    elif link > article:
        remainder = link %  article
        feeds.append(-remainder)
        if remainder != 0:
            links.append(remainder * 2)
    else:
        feeds.append(0)

print(f"Final Feed: {', '.join(map(str, feeds))}")
total_engagement_value = sum(feeds)
if total_engagement_value >= target:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target - total_engagement_value}")
