def create():
    with open("data.txt","w")as f:
        data=f.write("i am shubham\n i am ai enginer \n my fav language is python")
        print(data)


def find_word():
    word="language"
    data=True
    while data:
        with open("data.txt","r") as f:
            data=f.read()
            if (word in data):
                print("word found")
                break
            else:
                print("not found")

def find_line():
    word="language"
    data=True
    line_no=1
    while data:
        with open("data.txt","r") as f:
            data=f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
        return -1

create()
find_word()
find_line()

count=0
with open("data.txt","r") as f:
    data=f.read()
    num=data.split(",")
    for val in num:
        if ((val) % 2==0):
            count +=1

print(count)
         