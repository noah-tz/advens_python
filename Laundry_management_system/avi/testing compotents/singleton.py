class testing_singleton:
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.name = "avi"

    def track(self):
        print(f"track the name {self.name}")

    def change_name(self, new_name):
        self.name = new_name


first_insta = testing_singleton()
print(first_insta.name)
print()
first_insta.change_name("yanki")
print()
second_insta = testing_singleton()
print(second_insta.name)
print()
print(first_insta.name)
