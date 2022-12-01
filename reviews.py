data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(f'檔案讀取完了，總共有 {len(data)} 筆資料')

# 計算平均長度
total_len = 0
for d in data:
	total_len += len(d)
print(f'總長度 {total_len} ,平均長度 {total_len/len(data)}')