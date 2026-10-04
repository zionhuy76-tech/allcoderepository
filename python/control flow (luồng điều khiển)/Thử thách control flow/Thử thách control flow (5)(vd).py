Earth_weight = float(input("Hãy nhập trọng lượng của bạn trên Trái Đất: "))
Planet_number = int(input("Hãy chọn 1 hành tinh bằng số thứ tự (1-7): "))
if Planet_number == 1:
  Mercury = Earth_weight * 0.38
  print(Mercury)
elif Planet_number == 2:
  Venus = Earth_weight * 0.91
  print(Venus)
elif Planet_number == 3:
  Mars = Earth_weight * 0.38
  print(Mars)
elif Planet_number == 4:
  Jupiter = Earth_weight * 2.53
  print(Jupiter)
elif Planet_number == 5:
  Saturn = Earth_weight * 1.07
  print(Saturn)
elif Planet_number == 6:
  Uranus = Earth_weight * 0.89
  print(Uranus)
elif Planet_number == 7:
  Neptune = Earth_weight * 1.14
  print(Neptune)
else:
  print("Invalid number")