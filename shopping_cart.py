# shopping cart 클래스 선언
class ShoopingCart: # 쇼핑카트 틀을 만든다. 
    def __init__(self): # 먼저 초기화를 한다. 
        self.bucket = [] # self.bucket에 데이터를 담을 수 있도록 빈 리스트 상태로 초기화
    def add_product(self, product): # 쇼핑카트에 상품을 담을 수 있는 메서드생성
        self.bucket.append(product) # 담은 상품이 빈리스트 마지막에 담긴다
    def remove_product(self, product): # 쇼핑카트에 담긴 상품을 지우는 메서드생성
        self.bucket.remove(product) # 담은 상품이 삭제가 됨. 
    def show_products(self): #쇼핑카트에 담긴 상품목록을 볼 수 있는 메서드생성
        return self.bucket #쇼핑카트에 현재까지 뭘 담았는지 볼 수 있음. 

class Product: # 상품 틀을 만든다. 
    def __init__(self, name, price): #먼저 초기화를 한다.  
        selame = name #상품이름을 저장하는 속성 
        self.price = price #상품가격을 저장하는 속성

cart = ShoopingCart() #만든 쇼핑카트 틀로 찍어낼 인스턴스로 cart 생성. 
product_a = Product("dexter guitar", 300_000) #상품 틀로 찍어낼 인스턴스로 product_a를 생성. 상품 이름과 가격을 이 인스턴스에 담음
product_b = Product("ESP guitar", 1_000_000)
product_c = Product("Gipson guitar", 2_000_000)

cart.add_product(product_a) #product_a 인스터스의 담긴 상품을 카트에 추가를 한다 
cart.add_product(product_b)
cart.add_product(product_c)
cart.remove_product(product_b)
for product in cart.show_products(): 
    print(product.name, product.price)