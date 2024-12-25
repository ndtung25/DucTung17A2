import requests

url = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = requests.get(url)
comments = response.json()

print(f"Danh sách các bài post nổi bật (postId = 1):")

for i, comment in enumerate(comments[:3]):
    print(f"\nBài post {i+1}:")
    print(f"Post ID: {comment['postId']}")
    print(f"ID: {comment['id']}")
    print(f"Name: {comment['name']}")
    print(f"Email: {comment['email']}")
    print(f"Body: {comment['body']}")
    print("-" * 40)