import csv

def sangatSedikitFollower(x):
    if (x <= 1500):
        tmpSangatSedikitFollower = 1
    elif (x >= 1500 and x <=5000):
        tmpSangatSedikitFollower = (5000-x)/(5000-1500)
    else:
        tmpSangatSedikitFollower = 0
    return tmpSangatSedikitFollower

def sedikitFollower(x):
    if (x <= 1500 or x >= 25000):
        tmpSedikitFollower = 0
    elif (x > 1500 and x < 5000):
        tmpSedikitFollower = (x-1500)/(5000-1500)
    elif (x >= 5000 and x <= 10000):
        tmpSedikitFollower = 1
    else:
        tmpSedikitFollower = -(x-25000)/(25000-10000)
    return tmpSedikitFollower

def sedangFollower(x):
    if (x <= 10000 or x >= 75000):
        tmpSedangFollower = 0
    elif (x > 10000 and x < 25000):
        tmpSedangFollower = (x-10000)/(25000-10000)
    elif (x >= 25000 and x <= 50000):
        tmpSedangFollower = 1
    else:
        tmpSedangFollower = -(x-75000)/(75000-50000)
    return tmpSedangFollower

def banyakFollower(x):
    if (x <= 50000 or x >= 95000):
        tmpBanyakFollower = 0
    elif (x > 50000 and x < 75000):
        tmpBanyakFollower = (x-50000)/(75000-50000)
    elif (x >= 75000 and x <= 80000):
        tmpBanyakFollower = 1
    else:
        tmpBanyakFollower = -(x-95000)/(95000-80000)
    return tmpBanyakFollower

def sangatBanyakFollower(x):
    if (x <= 80000):
        tmpSangatBanyakFollower = 0
    elif (x > 85000 and x < 95000):
        tmpSangatBanyakFollower = (x-80000)/(95000-80000)
    else:
        tmpSangatBanyakFollower = 1
    return tmpSangatBanyakFollower

def sangatSedikitEngagement(y):
    if (y <= 0.1):
        tmpSangatSedikitEngagement = 1
    elif (y >= 0.1 and y <= 2):
        tmpSangatSedikitEngagement = (2-y)/(2-0.1)
    else:
        tmpSangatSedikitEngagement = 0
    return tmpSangatSedikitEngagement

def sedikitEngagement(y):
    if (y <= 0.1 or y >= 5.5):
        tmpSedikitEngagement = 0
    elif (y > 0.1 and y < 2):
        tmpSedikitEngagement = (y-0.1)/(2-0.1)
    elif (y >= 2 and y <= 3.5):
        tmpSedikitEngagement = 1
    else:
        tmpSedikitEngagement = -(y-5.5)/(5.5-3.5)
    return tmpSedikitEngagement

def sedangEngagement(y):
    if (y <= 3.5 or y >= 8):
        tmpSedangEngagement = 0
    elif (y > 3.5 and y < 5.5):
        tmpSedangEngagement = (y-3.5)/(5.5-3.5)
    elif (y >= 5.5 and y <= 7):
        tmpSedangEngagement = 1
    else:
        tmpSedangEngagement = -(y-8)/(8-7)
    return tmpSedangEngagement

def banyakEngagement(y):
    if (y <= 7 or y >= 94):
        tmpBanyakEngagement = 0
    elif (y > 7 and y < 8):
        tmpBanyakEngagement = (y-7)/(8-7)
    elif (y >= 8 and y <= 8.5):
        tmpBanyakEngagement = 1
    else:
        tmpBanyakEngagement = -(y-9.4)/(9.4-8.5)
    return tmpBanyakEngagement

def sangatBanyakEngagement(y):
    if (y <= 8.5):
        tmpSangatBanyakEngagement = 0
    elif (y > 8.5 and y < 9.4):
        tmpSangatBanyakEngagement = (y-8.5)/(9.4-8.5)
    else:
        tmpSangatBanyakEngagement = 1
    return tmpSangatBanyakEngagement

def veryBadValue(follower,engagement):
    a1 = min(follower[3],engagement[4])
    a2 = min(follower[4],engagement[4])
    a3 = min(follower[4],engagement[3])
    a4 = min(follower[4],engagement[2])

    tmpVeryBad = max(a1,a2,a3,a4)

    return tmpVeryBad

def badValue(follower,engagement):
    b1 = min(follower[3],engagement[4])
    b2 = min(follower[2],engagement[3])
    b3 = min(follower[3],engagement[3])
    b4 = min(follower[3],engagement[2])
    b5 = min(follower[3],engagement[1])
    b6 = min(follower[4],engagement[1])
    b7 = min(follower[4],engagement[0])
    b8 = min(follower[3],engagement[0])

    tmpBad = max(b1,b2,b3,b4,b5,b6,b7,b8)

    return tmpBad

def consideredValue(follower,engagement):
    c1 = min(follower[2],engagement[2])
    c2 = min(follower[2],engagement[3])
    c3 = min(follower[2],engagement[4])
    c4 = min(follower[1],engagement[4])
    

    tmpConsidered = max(c1,c2,c3,c4)

    return tmpConsidered    

def goodValue(follower,engagement):
    d1 = min(follower[1],engagement[1])
    d2 = min(follower[1],engagement[2])
    d3 = min(follower[1],engagement[3])
    

    tmpGood = max(d1,d2,d3)

    return tmpGood 

def veryGoodValue(follower,engagement):
    e1 = min(follower[0],engagement[0])
    e2 = min(follower[0],engagement[1])
    e3 = min(follower[0],engagement[2])
    e4 = min(follower[0],engagement[3])
    e5 = min(follower[0],engagement[4])
    e6 = min(follower[1],engagement[0])

    tmpVeryGood = max(e1,e2,e3,e4,e5,e6)

    return tmpVeryGood


def deFuzzifikasi(ssedikit,sedikit,sedang,banyak,sbanyak):
    down = ssedikit+sedikit+sedang+banyak+sbanyak
    up = (ssedikit*10)+(sedikit*20)+(sedang*30)+(banyak*40)+(sbanyak*50)

    hasilAkhir = up/(down+0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    return hasilAkhir


def bacaFileCSV():
    arraybaru = []
    data = []
    with open('influencers.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            arraybaru.append(row)
    
    del arraybaru[0]
    
    for i in arraybaru:
        data.append([int(i[0]),int(i[1]),float(i[2])])
    # print(data)

    return data

# MAIN

i=0
arrNew = []
baca = bacaFileCSV()
arrHasil = []
arrFoll = []
arrEngage = []

while i < 100:
    # print(baca1[i][1])
    follSSedikit = sangatSedikitFollower(baca[i][1])
    
    follSedikit = sedikitFollower(baca[i][1])
    follSedang = sedangFollower(baca[i][1])
    follBanyak = banyakFollower(baca[i][1])
    follSBanyak = sangatBanyakFollower(baca[i][1])

    engageSSedikit = sangatSedikitEngagement(baca[i][2])
    engageSedikit = sedikitEngagement(baca[i][2])
    engageSedang = sedangEngagement(baca[i][2])
    engageBanyak = banyakEngagement(baca[i][2])
    engageSBanyak = sangatBanyakEngagement(baca[i][2])

    arrFoll = [follSSedikit,follSedikit,follSedang,follBanyak,follSBanyak]
    arrEngage = [engageSSedikit,engageSedikit,engageSedang,engageBanyak,engageSBanyak]

    hasilVeryBadValue = veryBadValue(arrFoll,arrEngage)
    hasilBadValue = badValue(arrFoll,arrEngage)
    hasilConsideredValue = consideredValue(arrFoll,arrEngage)
    hasilGoodValue = goodValue(arrFoll,arrEngage)
    hasilVeryGoodValue = veryGoodValue(arrFoll,arrEngage)
        
    arrNew = deFuzzifikasi(hasilVeryBadValue,hasilBadValue,hasilConsideredValue,hasilGoodValue,hasilVeryGoodValue)

    arrHasil.append([arrNew,i+1])
    i += 1

arrHasil.sort(reverse= True)
hasilTerbaik=arrHasil[:20] 
print (hasilTerbaik)

f = open("choosen.csv","w+")
for x in range(len(hasilTerbaik)):
    f.write(str(hasilTerbaik[x][1])+"\n")
f.close()

# with open ('choosen.csv', mode='w') as terpilih:
#     terpilih_writer = csv.writer(terpilih, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for x in range(len(hasilTerbaik)):
#         terpilih_writer.writerow([hasilTerbaik[x][1]])
