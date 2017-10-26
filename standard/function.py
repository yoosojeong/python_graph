#2차 함수 함수식 찾는 프로그램
#x축,y축 대칭
class function:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def primary(p1,p2): # y = ax + b  -> 일차함수
    a = (p2.y - p1.y) / (p2.x - p1.x)
    b = p1.y - a*p1.x

    graph_one = "y = {}x + {}".format(a,b)
    return graph_one

def inclination(): #a 구하기 -> 이차함수
    a = (p4.y - p3.y) / (pow((p4.x - p3.x), 2))
    return a

def Quadratic(a,p3): # y = (x - p)² + q  - 표준형 ,  y=ax + bx + c - 일반형 -> 이차함수
    graph_two = "y = {}(x-{})²+ {}".format(a,p3.x,p3.y)
    return graph_two

def X_Symmetry(a,p3): # x축에 대칭이동 -> 이차함수
    graph_Xs_two = "y = -{}(x - {})²- {}".format(a, p3.x, p3.y)
    return graph_Xs_two

def Y_Symmetry(a,p3):
    graph_Ys_two = "y = {}(x + {})²+ {}".format(a, p3.x, p3.y)
    return graph_Ys_two


p1 = function(1,1) #한 점
p2 = function(2,2) #한 점

p3 = function(1,1) #꼭짓점
p4 = function(2,2) #한 점

a = inclination() #기울기 리턴받음

result_one = primary(p1,p2)
result_two = Quadratic(a,p3)
result_Xs_two = X_Symmetry(a,p3)
result_Ys_two = Y_Symmetry(a,p3)

print("일차함수 그래프 : {}".format(result_one))
print("이차함수 그래프 : {}".format(result_two))
print("이차함수 x축에 대칭 그래프 : {}".format(result_Xs_two))
print("이차함수 y축에 대칭 그래프 : {}".format(result_Ys_two))