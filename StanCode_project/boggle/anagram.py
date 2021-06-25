"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop



def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        anagrams = input("Find anagrams for : ")
        if anagrams == EXIT:
            print("Thank you")
            break
        print("Searching...")
        n = find_anagrams(anagrams)
        print(f'{len(n)} anagrams : {n}')


def read_dictionary():
    data=[]
    with open(FILE,'r') as f:
        for line in f:
            lines=line.split()
            data.append(lines)


def find_anagrams(s):
    """
    :param s:

    :return:
    """
    y=[]
    lst=[]
    data=[]
    for i in range(len(s)):
        data.append([])
    helper(s,y,lst,data)
    return lst


def helper(s,current,lst,data):
    if len(current) == len(s):
        if int_to_str(s,current,'') not in lst:
            for i in range(len(data[len(s)-1])):
                if len(data[len(s)-1][i]) == len(s):
                    lst.append(int_to_str(s,current,''))
                    print(f'Found:{int_to_str(s,current,"")}')
                    print('Searching...')
    else:
        for i in range(len(s)):
            if i not in current:
                current.append(i)
                if has_prefix(int_to_str(s,current,''),data):
                    helper(s,current,lst,data)
                    current.pop()
                    data[len(current)]=[]
                else:
                    current.pop()


def int_to_str(x,y,z):
    if len(z)==len(y):
        return z
    else:
        z+=x[y[len(z)]]
        return int_to_str(x,y,z)


def has_prefix(sub_s, data):
    """
    :param sub_s:
    :return:
    """
    if len(sub_s)==1:
        with open(FILE) as f:
            for line in f:
                if line.strip().startswith(sub_s):
                    data[len(sub_s)-1].append(line.strip())
        if len(data[len(sub_s)-1])!=0:
            return True
        else:
            return False
    else:
        for i in range(len(data[len(sub_s)-2])):
            if data[len(sub_s)-2][i].startswith(sub_s):
                data[len(sub_s)-1].append(data[len(sub_s)-2][i])
        if len(data[len(sub_s)-1])!=0:
            return True
        else:
            return False

if __name__ == '__main__':
    main()
