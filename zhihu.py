# /usr/bin/env python3 coding:utf-8

from zhihu_oauth import ZhihuClient, Answer, Article, ts2str
from zhihu_oauth.exception import NeedCaptchaException
import json

# Use My Account
# Login
client = ZhihuClient()
email_or_phone='304350131@qq.com'
password=170579
client.login_in_terminal(email_or_phone,password)

# Choose a topic.
#E.g. Semantic Analysis
topic = client.topic(19626971)

class Question:
    def __init__(self, id, title, questionCreated_time, questionUpdated_time, answer_count, questionFollower_count, detail,
    # about the answers
    answerId, created_time, updated_time, voteup_count, thanks_count, content, comment_permission, comment_count,
    # about the authors
    authorId, authorName, gender, locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations):
        self.id = id
        self.title = title
        self.questionCreated_time=questionCreated_time
        self.questionUpdated_time=questionUpdated_time
        self.answer_count=answer_count
        self.questionFollower_count=questionFollower_count
        self.detail=detail
        self.answer = Answer(answerId, created_time, updated_time, voteup_count, thanks_count, content, comment_permission, comment_count, authorId, authorName, gender, locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations)
    def __repr__(self):
        return repr((self.id, self.title, self.questionCreated_time, self.questionUpdated_time, self.answer_count, self.questionFollower_count, self.detail, self.answer.answerId, self.answer.created_time, self.answer.updated_time, self.answer.voteup_count, self.answer.thanks_count, self.answer.content, self.answer.comment_permission, self.answer.comment_count, self.answer.author.id, self.answer.author.authorName, self.answer.author.gender, self.answer.author.locations, self.answer.author.authorAnswer_count, self.answer.author.authorArticle_count, self.answer.author.authorColumn_count, self.answer.author.follower_count, self.answer.author.business, self.answer.author.employments, self.answer.author.educations))

class Answer:
    def __init__(self, answerId, created_time, updated_time, voteup_count, thanks_count, content, comment_permission, comment_count, authorId, authorName, gender,locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations):
        self.answerId = answerId
        self.created_time = created_time
        self.updated_time = updated_time
        self.voteup_count = voteup_count
        self.thanks_count = thanks_count
        self.content=content
        self.comment_permission=comment_permission
        self.comment_count=comment_count

        self.author = Author(authorId, authorName, gender,locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations)
    def __repr__(self):
        return repr((self.id, self.title, self.questionCreated_time, self.questionUpdated_time, self.answer_count, self.questionFollower_count, self.detail))

# gender==1 male; gender==0 female; gender=-1 not setted
class Author:
    def __init__(self, authorId, authorName, gender,locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations):
        self.authorId=authorId
        self.authorName=authorName
        self.gender=gender
        self.locations=''
        if locations:
            for location in locations:
                self.locations += location.name
        else:
            self.locations="None"
        self.authorAnswer_count=authorAnswer_count
        self.authorArticle_count=authorArticle_count
        self.authorColumn_count=authorColumn_count
        self.follower_count=follower_count
        self.business=''
        if business:
            self.business = business.name
        else: self.business="None"
        self.employments=''
        if employments:
            for employment in employments:
                if 'company' in employment:
                    self.employments += employment.company.name
                if 'job' in employment:
                    self.employments += employment.job.name
        else:
            self.employments="None"
        self.educations=''
        if educations:
            for education in educations:
                if 'school' in education:
                    self.educations += education.school.name
                if 'major' in education:
                    self.educations += education.major.name
        else:
            self.educations="None"
    def __repr__(self):
        return repr((self.answerId, self.created_time, self.updated_time, self.voteup_count, self.thanks_count, self.content,         self.comment_permission, self.comment_count))


Questions=[]
for answer in topic.best_answers:
    id=answer.question.id
    title=answer.question.title

    questionCreated_time=ts2str(answer.question.created_time)
    questionUpdated_time=ts2str(answer.question.updated_time)
    answer_count=answer.question.answer_count
    questionFollower_count=answer.question.follower_count
    detail=answer.question.detail
    answerId=answer.id
    created_time=ts2str(answer.created_time)
    updated_time=ts2str(answer.updated_time)
    voteup_count=answer.voteup_count
    thanks_count=answer.thanks_count
    content=answer.content
    comment_permission=answer.comment_permission
    comment_count=answer.comment_count
    authorId=answer.author.id
    authorName=answer.author.name
    gender=answer.author.gender
    locations=answer.author.locations
    authorAnswer_count=answer.author.answer_count
    authorArticle_count=answer.author.article_count
    authorColumn_count=answer.author.column_count
    follower_count=answer.author.follower_count
    business=answer.author.business
    employments=answer.author.employments
    educations=answer.author.educations

    newQuestion=Question(id,title, questionCreated_time, questionUpdated_time, answer_count, questionFollower_count, detail, answerId, created_time, updated_time, voteup_count, thanks_count, content, comment_permission, comment_count, authorId, authorName, gender,locations, authorAnswer_count, authorArticle_count, authorColumn_count, follower_count, business, employments, educations)
    # To fiter the same questions.
    if not any(d.id==id for d in Questions):
        Questions.append(newQuestion)
    else: continue


# save the result in json
file_name = 'list.json'
with open(file_name,'w') as file_object:
    # format setting
    dataJSON=json.dump(Questions,file_object,default=lambda o: o.__dict__, indent=4, sort_keys=False,ensure_ascii=False)

print("Saved in "file_name+"!")


# decode
# with open(file_name,'r') as file_object2:
#     s=json.load(file_object2)
#     print(s)
