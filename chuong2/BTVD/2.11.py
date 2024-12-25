import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = response.json()

print(f"Tổng số bài post: {len(posts)}")

for post in posts:
    print(f"userID: {post['userId']}")
    print(f"id: {post['id']}")
    print(f"title: {post['title']}")
    print(f"body: {post['body']}")
    print("-" * 40)