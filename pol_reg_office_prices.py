import numpy as np
from sklearn import linear_model
features, input_rows =input().split()
input_data= []
for i in range(int(input_rows)):
    l = list(map(float,input().split()))
    input_data.append(l)
test_rows =input().split()[0]
test_data = []
for i in range(int(test_rows)):
    l = list(map(float,input().split()))
    test_data.append(l)
# print(len(data))
input_data = np.array(input_data)
# print(input/_data[0][2])
test_data = np.array(test_data)
# print(input_data.shape)


X = input_data[:,0:int(features)]
y = input_data[:,int(features)]
# print(X.shape)
model=linear_model.LinearRegression()
model.fit(X, y)
# print(test_data.shape)
solution =model.predict(test_data)

for p in range(len(solution)):
    print(solution[p])
