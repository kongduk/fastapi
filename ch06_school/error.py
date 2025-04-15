# get one 예외처리를 알아보자
class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

#
# def get_one(task:str):
#     if task !="todo":
#         raise Missing(msg="야 없잖아")
#     return "정상 동작"
#
#
# def web():
#     try:
#         result = get_one("todo")
#     except Missing as e:
#         print(f"web에서 예외를 잡음! {e.msg}")
#
# if __name__ == "__main__":
#     web()