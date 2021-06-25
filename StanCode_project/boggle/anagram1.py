FILE= 'dictionary.txt'

def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        x=input("Find anagrams for : ")
        if x=="-1":
            print("Thank you")
            break
        print("Searching")
        ans=[]
        with open(FILE) as f:
            for line in f:
                if strindict(x)==strindict(line.strip()):
                    ans.append(line.strip())
                    print(f"Found : {line.strip()}")
                    print("Searching")
        print(f"{len(ans)} anagrams : {ans}")

def strindict(x):
    str_in_dict={}
    for i in range(len(x)):
        if x[i] not in str_in_dict:
            str_in_dict[x[i]]=x.count(x[i])   #將字母加入
    return str_in_dict

if __name__=="__main__":
    main()