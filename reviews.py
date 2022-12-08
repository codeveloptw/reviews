data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 50000 == 0:
			print(len(data))
print(f'檔案讀取完了，總共有 {len(data)} 筆資料')

# 文字記數
wc = {}  # word_count
count = 0
for d in data:
    words = d.strip().split()  # split default = '' 空字串 and 連續空會忽略
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
        	wc[word] = 1
    # print(words)
    # break

for word in wc:
    if wc[word] > 100000:
        print(f'{word} {wc[word]}')

print(len(wc))

while True:
    word = input('要查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(f'{word} 出現次數 {wc[word]}')
    else:
        print(f'{word} 沒有在裡面')

print('離開查詢')


# 計算平均長度
total_len = 0
for d in data:
	total_len += len(d)
print(f'總長度 {total_len} ,平均長度 {total_len/len(data)}')


# 篩選有 'good' 
#-------------------------
#good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
#-化簡為下面這一行------------------------
good = [d for d in data if 'good' in d]
print(len(good))
print(f'含有 good 字串的第一筆資料 :\n {good[0]}')

# []中第一個是變數是要放進 list 的東西
good = [d[0] for d in data if 'good' in d]
print(good)

# for i in range(100):
# 	print('hi')