import os

if __name__ == "__main__":
	# 指定目录路径
	path = "."

	# 使用os.listdir()方法获取目录下所有文件
	files = os.listdir(path)

	# 打印所有文件名
	for file in files:
	    print(f"{file}")