inf = open("/mnt/c/Users/yang/repo/103976/EnWords.csv","r")
while True:
    tline = inf.readline()
    if(tline):
        ttttt = tline.split("@@")
        ouf = open("/mnt/c/Users/yang/repo/eng-data/dict/easy/%s.json"%(ttttt[0][1:-1]),"w")
        ouf.write('{"word":%s,"E2C":%s}'%(ttttt[0],ttttt[1][:-1]))
        # print('{"word":%s,"E2C":%s}'%(ttttt[0],ttttt[1][:-1]))
    else:
        break
