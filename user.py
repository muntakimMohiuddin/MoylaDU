from firebase import firebase
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
from munch import munchify
class User:
    def __init__(self,user_obj):
        try:self.id=user_obj['id']
        except KeyError:pass
        try:self.department=user_obj['dept']
        except KeyError:pass
        try:self.hall=user_obj['hall']
        except KeyError:pass
        try:self.email=user_obj['email']
        except KeyError:pass
        try:self.photoUrl=user_obj['photoUrl']
        except KeyError:pass
        try:self.roll=user_obj['roll']
        except KeyError:pass
        try:self.username=user_obj['username']
        except KeyError:pass
        try:self.session=user_obj['session']
        except KeyError:pass
        try:self.likesCount=0
        except KeyError:pass

    def __str__(self):
        return str(self.__dict__)

class Profile():
    def __init__(self, user_obj):
        print("in profile",user_obj)
        try:
            self.id = user_obj['id']
        except KeyError:
            pass
        try:
            self.email = user_obj['email']
        except KeyError:
            pass
        try:
            self.photoUrl = user_obj['photoUrl']
        except KeyError:
            pass
        try:
            self.username = user_obj['username']
        except KeyError:
            pass
        try:
            self.likesCount = firebase.get("/profiles/"+self.id+"/likesCount",None)
        except KeyError:
            pass

    def __str__(self):
        return str(self.__dict__)