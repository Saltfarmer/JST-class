import numpy as np

#Memasukkan data train
train_x = [[1,1,1,1,1], [0,1,0,0,1], [0,0,0,1,0], [1,1,0,0,0], [0,0,1,0,1]]
train_y = [[1,1,1], [1,0,0], [0,1,1], [1,0,0], [0,0,0]]

#Inisialisasi weight = 0
w = np.zeros((len(train_x[0]), len(train_y[0])))

#Update nilai weighy
if len(train_x) == len(train_y):		
	for i in range(len(train_x)):
		for j in range(len(train_x[0])):
			for k in range(len(train_y[0])):
				w[j][k] += train_x[i][j] * train_y[i][k]
else:
	print("Jumlah x dan Jumlah y tidak sama")

# Test data pada weight yang sudah ditentukan		
test_x = [[0,0,0,1,1]]
test_y = np.dot(test_x, w)

#Fungsi aktivasi
for i in range(len(test_y)):
	for j in range(len(test_y[0])):
		if test_y[i][j] > 0:
			test_y[i][j] = 1
		else:
			test_y[i][j] = 0

#Output hasil test
print(test_y)