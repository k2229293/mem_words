import time
import datetime
import os
def xuexi():
    studyed = []
    with open("words.txt") as file_:
        words = file_.readlines()
        with open("words_backup.txt","w") as file_backup:
            for i in words:
                file_backup.write(i)
        words = [i.strip() for i in words]
        words_new = [i for i in words if len(i.split("\t"))==2]
        words_old = [i for i in words if len(i.split("\t"))==4]
        words_new_old = words_new + words_old
        words_strange = [i for i in words if i not in words_new_old]
        words_old = [i for i in words_old if i.split("\t")[-1]!="0"]
        words_dead = [i for i in words_old if i.split("\t")[-1]=="0"]
    words_new_num = len(words_new)
    print("all words:"+str(len(words)))
    if words_strange:
        n = 0
        for i in words_strange:
            n+=1
            print("strange_word:"+str(i)+",line:" + str(words.index(i)))
    print("not study:"+ str(words_new_num))
    pre_new_num = 200 if (words_new_num > 200) else words_new_num
    pre_old_num = daoqi(words_old)
    pre_num = pre_new_num*2 + pre_old_num
    pre_min = pre_num*5/60
    print("old worlds:"+str(pre_old_num))
    print("prepare study words:" + str(pre_num))
    print("prepate study time:" + str(pre_min)+"mins")
    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')
    studyed += xuexi_new(words_new,pre_new_num)
    studyed += xuexi_old(words_old)
    studyed += words_dead
    if (len(studyed) != len(words)):
        print("wrong: words="+str(len(words))+" studyed="+str(len(studyed)))
    with open("words.txt","w") as file_:
        for i in studyed:
            file_.write(i+"\n")
    print("updated!")
    print("today task complete!")
def xuexi_new(words_new,pre_new_num):
    nw_words_new = []
    pre_words = words_new[:pre_new_num]
    for i in pre_words:
        show(i,"forward")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    for i in pre_words:
        show(i,"reward")
        date_string = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
        nw_words_new.append(i+"\t"+date_string+"\t"+"1")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    if len(words_new) > 200:
        return nw_words_new + words_new[200:]
    else:
        return nw_words_new

def time_interval(time_str):
    date_lst = time_str.split("-")
    y = int(date_lst[0])
    m = int(date_lst[1])
    d = int(date_lst[2])
    dt = datetime.date(y,m,d)
    delta_days = (datetime.date.today()-dt).days
    return delta_days

def daoqi(words_old):
    n=0
    for i in words_old:
        time_str = i.split("\t")[2]
        delta_days = time_interval(time_str)
        dl_days = int(i.split("\t")[3])
        if delta_days >= dl_days:
            n+=1
    return n

def xuexi_old(words_old):
    nw_words_old = []
    for i in words_old:
        dt = i.split("\t")[2]
        dl_days = int(i.split("\t")[3])
        delta_days = time_interval(dt)
        if delta_days > dl_days:
            print("\t".join(i.split("\t")[:2])+"sup")
            date_string = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
            nw_words_old.append("\t".join(i.split("\t")[:3])+"\t" + date_string + "\t" + "1")
        if delta_days == dl_days:
            show(i,"forward")
            x = "\t".join(i.split("\t")[:-1]) + "\t" + str(interval_change(dl_days))
            nw_words_old.append(x)
        if delta_days < dl_days:
            nw_words_old.append(i)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    return nw_words_old

def show(word_min,ward):
    word_min = word_min.split("\t")
    word = word_min[0]
    mining = word_min[1]
    if ward == "forward":
        print(word)
        time.sleep(2)
        print(mining)
    elif ward == "reward":
        print(mining)
        time.sleep(2)
        print(word)

def interval_change(n):
    if n==1:
        return 2
    if n == 2:
        return 5
    if n == 5:
        return 8
    if n == 8:
        return 14
    if n == 14:
        return 0
if __name__=="__main__":
    xuexi()
