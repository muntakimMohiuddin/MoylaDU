from firebase import firebase
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
from munch import munchify
from copy import deepcopy
class Posts:
    def __init__(self,postId,post_object):
        self.id=postId
        self.authorId=post_object['authorId']
        self.commentsCount=post_object['commentsCount']
        self.createdDate=post_object['createdDate']
        self.createdDateText=post_object['createdDateText']
        self.description=post_object['description'].split("\n")
        self.imagePath=post_object['imagePath']
        self.imageTitle=post_object['imageTitle']
        self.likesCount=post_object['likesCount']
        self.title=post_object['title']

    def __str__(self):
        return str(self.__dict__)

    def getShowable(self):
        temp=deepcopy(self.__dict__)
        temp['authorName']=firebase.get('users/'+self.authorId,None)['username']
        temp['comments']=list()
        result=firebase.get('post-comments/'+self.id,None)
        if result is not None:
            for comments in result.items():
                for i in range(len(comments)):
                    if i%2==1:
                        comments[i]['authorName']=firebase.get('users/'+comments[i]['authorId'],None)['username']
                        comments[i]['profilePic']=firebase.get('users/'+comments[i]['authorId'],None)['photoUrl']
                temp['comments'].append(comments)

        return munchify(temp)
