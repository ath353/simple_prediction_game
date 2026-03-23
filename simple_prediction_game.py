import random

number = random.randint(1,10)

guess = int(input("Tôi đang nghĩ đến một số trong khoảng từ 1 đến 10. Đó là số nào? "))

while guess != number:
    if guess < number:
        print("Số bạn chọn quá nhỏ...")
    else:
        print("Sô bạn chọn quá lớn...")
    guess = int(input("Xin hãy đoán lại... "))

print("Xin chúc mừng, bạn đã đoán đúng!")


