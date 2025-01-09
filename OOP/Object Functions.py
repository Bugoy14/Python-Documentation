
class User:
    def __init__(self, first_name, last_name, likes_count, *friends_names):
        self.first_name = first_name
        self.last_name = last_name
        self.likes_count = likes_count
        self.friends_names = friends_names

    def introduce(self):
        print(f"Hi! My name is {self.first_name} {self.last_name}")

    def full_profile(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Likes    : {self.likes_count}")
        print("Friends: ")
        for friend in self.friends_names:
            print(f"      -{friend}")


user_one = User("Carl", "Azarcon", 100, "Lalay", "Bugoy", "Alyssa", "Alieya")
user_one.introduce()
user_one.full_profile()


