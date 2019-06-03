product = []
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	p = [name, price]
	product.append(p)
for p in product:
	print(p[0], '的价格是：', p[1])

with open('product.csv', 'w' , encoding='utf-8') as f:
	f.write('商品,价格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')