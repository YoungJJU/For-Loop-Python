for x in range(3):
    print(100)
    print(200)
print(300)

import turtle as t

#삼각형 그리기
for x in range(3):
    t.fd(100)
    t.lt(120)

#사각형 그리기
for x in range(4):
    t.fd(100)
    t.lt(90)

#원 그리기
t.circle(50)

print("[0-4]")
for x in range(5):
    print(x)


print("[1-10]")
for x in range(1,11):
    print(x)

b = 0
for a in range(1,11):
    b = b + a
print(b)

b = 0
for a in range(1,11):
    b = b +a
    print("x: ", x,"총합: ",b)
