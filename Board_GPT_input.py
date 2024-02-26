import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        # 비밀번호를 해시화하여 저장
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"Name: {self.name}")
        print(f"Username: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
posts = []

# 회원 생성 함수
def create_member():
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    members.append(Member(name, username, password))

# 게시글 생성 함수
def create_post():
    if not members:
        print("Please create a member first.")
        return
    author_username = input("Enter your username to create a post: ")
    for member in members:
        if member.username == author_username:
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            posts.append(Post(title, content, author_username))
            print("Post created successfully.")
            return
    print("User not found. Please create a member first.")

# 사용자 입력을 받아 Member 인스턴스 생성
while True:
    create_member_option = input("Would you like to create a member? (yes/no): ")
    if create_member_option.lower() == 'yes':
        create_member()
    else:
        break

# 사용자 입력을 받아 Post 인스턴스 생성
while True:
    create_post_option = input("Would you like to create a post? (yes/no): ")
    if create_post_option.lower() == 'yes':
        create_post()
    else:
        break

# 회원 이름 출력
print("\nMembers:")
for member in members:
    print(member.name)

# 특정 유저가 작성한 게시글 제목 출력
print("\nPosts by specific users:")
for post in posts:
    if post.author == "john_doe":  # 예시로 john_doe가 작성한 게시글 출력
        print(post.title)

# 특정 단어가 content에 포함된 게시글 제목 출력
print("\nPosts containing 'number' in content:")
for post in posts:
    if 'number' in post.content:
        print(post.title)
