inf = open("/mnt/c/Users/yang/Desktop/30k-explained.txt",'r')

while(True):
    t_line = inf.readline()
    if(t_line):
        try:
            t_tt = t_line.split()
            t_word = t_tt[0]
            t_id = int(t_tt[1])
            t_ipa = inf.readline()
            t_e2c = inf.readline()
            t_e2e = inf.readline()
            ouf = open("/mnt/c/Users/yang/repo/eng-data/dict/main/%s.json"%t_id,"w")
            ouf.write('{"id":"%d","word":"%s","IPA":"%s","E2C":"%s","E2E":"%s"}'%(t_id,t_word,t_ipa[:-1],t_e2c[:-1],t_e2e[:-1]))
            print('{"id":"%d","word":"%s","IPA":"%s","E2C":"%s","E2E":"%s"}'%(t_id,t_word,t_ipa[:-1],t_e2c[:-1],t_e2e[:-1]))
        except:
            t_e2e = inf.readline()
            pass
    else:
        break
