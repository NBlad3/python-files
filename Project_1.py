#input
scores = [9,1,6,4,8,2,10,3,6,7,3,4,5,6,2,3,4,1,6,10,8,9,8,7,5,7,8,9,7,7,9,9,10,10,2,8,8,4,3,8,9,9,10]

#process
# Giỏi 8.5 <= score
# Khá 7 <= score < 8.5
# Trung bình Phần còn lại

#output: Đếm số học sinh giỏi, khá, trung bình
# Có 5 học sinh giỏi
# Có 3 học sinh khá
# Có 8 học sinh trung bình

very_good = 0

good = 0

normal = 0

for score in scores:
    if score >= 8.5:
        very_good += 1
    elif score >= 7 and score < 8.5:
        good += 1
    else:
        normal += 1

print(f'''Co {very_good} hoc sinh gioi
Co {good} hoc sinh kha
Co {normal} hoc sinh trung binh''')
