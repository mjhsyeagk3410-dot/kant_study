# 클래스 정의(선언): 뿡어빵 틀
class User:
    def __init__ (self, name): # 생성자: 클래스가 처음 생성될 때 자동으로 호출
        self.name = name # 변수를 초기화

    def show(self): # 메서드(Method)
        return f"회원 이름: {self.name}"

# 인스터스 생성 : 붕어빵
user_a = User("손흥민")

# user 클래스로 생성한 인스턴스 (메모리에 생성)

# 클래스의 인스턴스 변수
print(user_a.name)

# 클래스의 메서드 접근
print(user_a.show())