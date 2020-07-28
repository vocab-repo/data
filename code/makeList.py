inf1 = open("/mnt/c/Users/yang/Desktop/30k-explained.txt",'r')
inf2 = open("/mnt/c/Users/yang/repo/103976/EnWords.csv","r")
ll = set()
while(True):
    t_line = inf1.readline()
    if(t_line):
        try:
            t_tt = t_line.split()
            t_word = t_tt[0]
            t_id = int(t_tt[1])
            t_ipa = inf1.readline()
            t_e2c = inf1.readline()
            t_e2e = inf1.readline()
            ll.add(t_word)
            # print('{"id":"%d","word":"%s","IPA":"%s","E2C":"%s","E2E":"%s"}'%(t_id,t_word,t_ipa[:-1],t_e2c[:-1],t_e2e[:-1]))
        except:
            t_e2e = inf1.readline()
            pass
    else:
        break
while True:
    tline = inf2.readline()
    if(tline):
        ttttt = tline.split("@@")
        ll.add(ttttt[0][1:-1])
    else:
        break

ll = list(ll)
ll.sort()
ml = 0
wd = ""
for i in ll:
    if(len(i)>ml):
        ml = len(i)
        wd = i
print(ml)
print(wd)
