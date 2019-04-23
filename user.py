class User:
    def __init__(self,user_obj):
        self.id=user_obj['id']
        self.department=user_obj['dept']
        self.hall=user_obj['hall']
        self.email=user_obj['email']
        self.photoUrl=user_obj['photoUrl']
        self.roll=user_obj['roll']
        self.username=user_obj['username']
        self.session=user_obj['session']
    def __str__(self):
        return str(self.__dict__)