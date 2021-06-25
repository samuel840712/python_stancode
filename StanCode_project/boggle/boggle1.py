FILE = 'dictionary.txt'
dictionary = [set() for i in range(26)]
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
count = 4
min =4
matrix = [list() for i in range(count)]
data=[]


def main():
	read_dictionary()
	create_boggle()
	find()
	print(f'There are {len(data)} words in total.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line=line.strip()
			dictionary[ALPHABET.find(line[0])].add(line)  #對字母找(line的開頭)

def create_boggle():
	for i in range(count):
		s = input(str(i + 1) + ' row of letters:').lower().split()
		if len(s) == count:
			for j in range(count):
				if len(s[j]) ==1 and s[j].isalpha():
					matrix[i].append([s[j],0]) #用0和1控制helper的判斷

		else:
			print('Illegal Format')
			break

def find():
	for i in range(count):
		for j in range(count):
			matrix[i][j][1]=1 #當等於1時進入helper判斷，已經有值為1，沒有值為0
			helper(i,j,matrix[i][j][0])
			matrix[i][j][1]=0


def helper(i,j,current):
	if len(current)>=min:
		check(current)
	for a in range(3): #a,b移動範圍為0~2     00 01 02
		if i+(a-1) in range(count):#       10 11 12
			for b in range(3): #           20 21 22
				if j+(b-1) in range(count):
					if matrix[i+a-1][j+b-1][1] == 0:
						if has_prefix(current + matrix[i+a-1][j+b-1][0]): #current為儲存字母，matrix[i+a][j+b][0]為16宮格的字母
							matrix[i+a-1][j+b-1][1]=1
							helper(i+a-1,j+b-1,current+matrix[i+a-1][j+b-1][0])
							matrix[i+a-1][j+b-1][1]=0


def check(current):
	if current not in data:
		if current in dictionary[ALPHABET.find(current[0])]:
			print('Found: '+current)
			data.append(current)


def has_prefix(sub_s):
	"""
	:param sub_s:
	:return:
	"""
	for keyword in dictionary[ALPHABET.find(sub_s[0])]:
		if keyword.startswith(sub_s):
			return True
		else:
			return False
if __name__=="__main__":
    main()



