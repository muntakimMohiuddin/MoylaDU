from firebase import firebase
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
class Posts:
    def __init__(self,postId,post_object):
        self.id=postId
        self.authorId=post_object['authorId']
        self.authorName=firebase.get('profiles/'+self.authorId,None)['username']
        self.commentsCount=post_object['commentsCount']
        self.createdDate=post_object['createdDate']
        self.createdDateText=post_object['createdDateText']
        self.description=post_object['description'].split("\n")
        self.hasComplain=post_object['hasComplain']
        self.imagePath=post_object['imagePath']
        self.imageTitle=post_object['imageTitle']
        self.likesCount=post_object['likesCount']
        self.title=post_object['title']
        self.watcherCount=post_object['watchersCount']

    def __str__(self):
        return str(self.__dict__)