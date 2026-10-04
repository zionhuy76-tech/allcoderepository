#=================
#Area Calculator📐
#=================

print("HÃY CHỌN HÌNH CẦN TÍNH DƯỚI ĐÂY!")
print("1. Hình vuông")
print("2. Hình chữ nhật")
print("3. Hình tam giác")
print("4. Hình tròn")

shape = int(input("Bạn chọn hình số: "))

if shape == 1:
    side = float(input("nhập độ dài cạnh của hình vuông: "))
    area = side ** 2
    print("Diện tích hình vuông là:", area)
elif shape == 2:
    lenght = float(input("Nhập chiều dài của hình chữ nhật:"))
    width = float(input("Nhập chiều rộng hình chữ nhật:"))
    area = lenght * width
    print("Diện tích hình chữ nhật là:", area)
elif shape == 3:
    base = float(input("Nhập độ dài đáy của hình tam giác: "))
    height = float(input("Nhập chiều cao của hình tam giác: "))
    area = 0.5 * base * height
    print("Diện tích hình tam giác là:", area)
elif shape == 4:
    radius = float(input("Nhập bán kính của hình tròn: "))
    area = 3.14 * radius ** 2
    print("Diện tích hình tròn là:", area)
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")