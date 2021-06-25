"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
MIN_LENGTH = 4
count = 4
ALPHABET='abcdefghijklmnopqrstuvwxyz'
dictionary = [set() for i in range(26)]
matrix = [list() for i in range(count)]


class tree:
	def __init__(self,name):
		self.name=name
		self.point=[]
		for i in range(3):   #i,j範圍為0~2  00 01 02 (j往右走,i往下走)
			self.point.append([])#         10 11 12
			for j in range(3):#            20 21 22
				self.point[i].append(None)



def main():
	"""
	TODO:
	"""
	read_dictionary()
	create_boggle()
	find(matrix[0][0],matrix,1,matrix[0][0])



def read_dictionary():
	with open(FILE,'r') as f:
		for line in f:
			lines=line.lower().strip()
			dictionary[ALPHABET.find(line[0])].add(lines)


def create_boggle():
	for i in range(count):
		matrix.append([])
		s=input(f'{i+1} row of letters: ').lower().split()
		if len(s) ==count and len(list(filter(lambda x:len(x)==1 and x.isalpha(),s)))==count:
			for j in s: #將a(j)放入第一格(i),
				matrix[i].append(tree(j))
		else:
			print('Illegal Format')
			break

	for i in range(count):
	 	for j in range(count):
	 		print(list(map(lambda x:x.name,matrix[i])))
	 		make_tree(matrix[i][j],i,j,matrix) #ij為xy的座標

	control(matrix,i,j)


def make_tree(address,x,y,matrix):
	for a in range(3):
		for b in range(3):
			if x+(a-1) in range(count) and y+(b-1) in range(count): #座標為xy 九宮格為ab(ab範圍為-1~1之間)
				address.point[a][b]=matrix[x+a-1][y+b-1]

def control(matrix,x,y):
	print('往(左上)輸入1')
	print('往(  上)輸入2')
	print('往(右上)輸入3')
	print('往(  左)輸入4')
	print('往(  右)輸入5')
	print('往(左下)輸入6')
	print('往(  下)輸入7')
	print('往(右下)輸入8')
	for i in range(count):
		for j in range(count):
			print(str(matrix[i][j].name),end= '')
		print('\n')
		print(f'在{matrix[x][y].name}')
		s=input('Input: ')
		p=['0 0','0 1', '0 2', '1 0', '1 2', '2 1','2 2']
		o=p[int(s)-1].split('')
		if matrix[x][y].point[int(o[0])][int(o[1])]==None:
			control(matrix,x,y)
			print('----------------')
		else:
			print(matrix[x][y].point[int(o[0])].name)
			control(matrix,x+int(o[0])-1,y+int(o[1])-1)


def find(address,matrix,n,letter):
	#address為目前位置,n目前有幾個letter,把所有letter寫入list
	able_walk=[]
	for a in range(3):
		for b in range(3):
			address.point[a][b]==None




def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	pass


if __name__ == '__main__':
	main()
