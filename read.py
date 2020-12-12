data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #每一千筆印一次
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(d), '筆留言長度小於100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))
print(good[0])


wc = {} # word_count
for d in data:
	words = d.split() #預設值空字串,連續空白也不會算
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) # 字典長度

while True:
	word = input('請問你想查甚麼字?')
	if word == 'q':
		break
	if word in wc:
		print('出現', wc[word], '次')
	else:
		print('這個字沒有出現過!')
print('感謝您使用本功能')














