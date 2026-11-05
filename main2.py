# 클래스 정의(선언): 뿡어빵 틀
class User:
    def __init__ (self, name): # 생성자: 클래스가 처음 생성될 때 자동으로 호출
        self.name = name # 변수를 초기화

    def show(self): # 메서드(Method)
        return f"회원 이름: {self.name}"

# 인스터스 생성 : 붕어빵
user_a = User("손흥민")
user_b = User("이강인")

# user 클래스로 생성한 인스턴스 (메모리에 생성)

# 클래스의 인스턴스 변수
print(user_a.name)
print(user_b.name)

# 클래스의 메서드 접근
print(user_a.show())
print(user_b.show())

print(type(user_a))
print(user_a is user_b)
print(id(user_a))
print(id(user_b))

# ============================

class Monitor:
    def display_info(self):
        # 인스턴스 변수
        self.resolution = "1920X1080"
        self.size = "27인치"
        print(f"모니터 정보\n해상도: {self.resolution}\n크기: {self.size}\n객체 ID: {id(self)}")

monitor = Monitor () # 인스턴스 생성(모니터 객체 생성)
print(id(monitor)) # 모니터 인스턴스의 ID 출력

monitor.display_info()

# ==================================

class SmartPhone:
    def __init__(self, model):
        self.model = model # 속성(Attridute)
        self.battery = 50 # 속성

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
            print(f"배터리 충전 완료 : {self.battery}%")
        else:
            print(f"배터리 충전 중 ... : {self.battery}%")

phone_a = SmartPhone("아이폰")
print(phone_a.model)
phone_a.charge(30)
phone_a.charge(30)

phone_b = SmartPhone("갤럭시")
print(phone_b.model)
phone_b.charge(30)
phone_b.charge(30)


    