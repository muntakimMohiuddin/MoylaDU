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