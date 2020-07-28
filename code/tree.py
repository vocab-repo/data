import os

inf = open("/mnt/c/Users/yang/repo/eng-data/dict/list.txt","r")

while(True):
    ln = inf.readline()
    if ln:
        wd = ln[:-1]
        lwd = list(ln[:-1])
        # print(ln[:-1])
        t_path = "/mnt/c/Users/yang/repo/eng-data/word/"
        for i in range(len(lwd)):
            t_path+=lwd[i]
            t_path+="/"

            if(False==os.path.exists(t_path)):
                os.makedirs(t_path)
            w_path = t_path+"index.txt"
            # print(w_path)

            ouf = open(w_path,"a")
            ouf.write(wd+"\n")
    else:
        break
