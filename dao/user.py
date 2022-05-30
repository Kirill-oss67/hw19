from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_name(self, name):
        return self.session.query(User).filter(User.username == name).first()

    def create(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, id):
        user = self.get_one(id)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_one(user_data.get('id'))
        user.username = user_data.get('username')
        user.password = user_data.get('password')
        user.role = user_data.get('role')

        self.session.add(user)
        self.session.commit()
