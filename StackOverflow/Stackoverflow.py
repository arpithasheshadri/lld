from enum import Enum
from datetime import datetime
from typing import List,Dict

class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1


class User:
    def __init__(self, username: str):
        self.username = username
        self.reputation = 0
        self.questions = []
        self.answers = []

    def __str__(self):
        return f"Username: {self.username} - Reputation: {self.reputation}"
    
    def post_question(self, title: str, description: str, tags: List[str]):
        question = Question(self,title,description,tags)
        self.questions.append(question)
        return question
    
    def post_answer(self, question, content: str):
        answer =  Answer(self,question, content)
        self.answers.append(answer)
        return answer
    
    def upvote(self, post):
        post.add_vote(VoteType.UPVOTE,self)

    def downvote(self, post):
        post.add_vote(VoteType.DOWNVOTE,self)

class Tag:
    def __init__(self, name:str):
        self.name = name

class Comment:
    def __init__(self, user:User, content: str):
        self.user = user
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.user.username}: {self.content}"

class Post:
    def __init__(self, user:User, content: str):
        self.user = user
        self.content = content
        self.votes = 0
        self.created_at = datetime.now()
        self.comments = []

    def add_comments(self, comment: Comment):
        self.comments.append(comment)

    def add_vote(self, votetype: VoteType, voter: User):
        print("here")
        self.votes += votetype.value
        print(self.votes)
        if votetype == VoteType.UPVOTE:
            voter.reputation += 10

        elif votetype == VoteType.DOWNVOTE:
            voter.reputation -= 2

    def __str__(self):
        return f"{self.content} | Votes: {self.votes} | Posted by {self.user.username}"


class Question(Post):
    def __init__(self, user: User, title: str, description: str, tags: List[str]):
        super().__init__(user,description)
        self.title = title
        self.tags = [Tag(tag) for tag in tags]
        self.answers = []
        self.accepted_ans = None

    def add_answer(self, answer):
        self.answers.append(answer)

    def accept_answer(self, answer):
        if answer in self.answers:
            self.accept_answer = answer
            answer.user.reputation += 20

    def __str__(self):
        return f"Question: {self.title} | Tags: {[tag.name for tag in self.tags]} | Votes: {self.votes}"


class Answer(Post):
    def __init__(self, user,question, content):
        super().__init__(user, content)
        self.question = question

class StackOverflow:
    def __init__(self):
        self.users = []
        self.questions = []

    def register_user(self, username):
        user  = User(username)
        self.users.append(user)
        return user
    
    def post_question(self, user: User, title: str, description: str, tags: List[str]):
        question = Question(user,title,description,tags)
        self.questions.append(question)
        return question
    
    def search_questions(self, keyword: str):
        return [q for q in self.questions if keyword.lower() in q.title.lower() or keyword.lower() in q.content.lower()]
    
    def show_top_questions(self):
        sorted_questions = sorted(self.questions, key=lambda q: q.votes, reverse=True)
        for q in sorted_questions:
            print(q)

def main():
    stackoverflow = StackOverflow()

    user1 = stackoverflow.register_user("Alice")
    user2 = stackoverflow.register_user("Brian")
    
    question1 = stackoverflow.post_question(user1,"How to implement a binary search in Python?","I need help with a binary search function.", ["python", "algorithm"])

    answer1 = user2.post_answer(question1,"Here is an implementation of binary search in Python:\n\n```python\ndef binary_search(arr, x): pass```")

    user1.upvote(answer1)

    question1.accept_answer(answer1)

    stackoverflow.show_top_questions()

if __name__ == "__main__":
    main()