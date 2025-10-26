import pytest


@pytest.fixture
def user_factory(db, faker):
    from apps.users.models.user_model import User
    
    def make_user(
        *,
        email=None,
        password='Pass@123',
        username=None,
        count=1,
        **extra
    ):
        users=[]
        for i in range(count):
            _email = email or faker.unique.email()
            _username = username or faker.name()
            
            user = User.objects.create_user(
                email=_email,
                password=password,
                username=_username,
                **extra
            )
            users.append(user)
        
        return users if count>1 else users[0]
    
    return make_user