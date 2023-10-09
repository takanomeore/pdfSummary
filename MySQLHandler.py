import mysql.connector
import settings
import sys
from datetime import datetime,timedelta
import os

baseIP = settings.DBIP
uName = settings.USN
Passw = settings.PWD

'''
print(settings.DBIP)
print(settings.USN)
print(settings.PWD)
'''

def main():
    db = mysql.connector.connect(
        host=baseIP,
        port='3306',
        user=uName,
        db='pdfManage_DB',
        password=Passw,
        charset='utf8'
    )

    cursor = db.cursor()
    db.commit()

    if(sys.argv[1] == "1"):
        dateSign(db,cursor)
    elif(sys.argv[1] == "2"):
        deleteFlagCheck(db,cursor)
    elif(sys.argv[1] == "3"):
        deletePDF(db,cursor)
    else:
        print('gomi')

    cursor.close()
    db.close()

def dateSign(mydb, myCursor):
    nowDatestr = getDate(0)
    deleteDatestr = getDate(1)

    fName = sys.argv[2]
    myCursor.execute(f"INSERT INTO pdfManager_TB(fileName,uploadDate,deleteDate,deleteFlag) VALUES ('{fName}','{nowDatestr}','{deleteDatestr}',0);")
    mydb.commit()

def deleteFlagCheck(mydb,myCursor):
    nowDatestr = getDate(0)
    myCursor.execute(f"UPDATE pdfManager_TB SET deleteFlag=1 WHERE deleteDate='{nowDatestr}';")
    mydb.commit()

def deletePDF(mydb,myCursor):
    myCursor.execute(f"SELECT fileName,deleteDate FROM pdfManager_TB WHERE deleteFlag = 1;")
    deleteFiles = myCursor.fetchall()
    rowCount = myCursor.rowcount
    linuxPath = "/var/www/unj-labo/pdfs/"

    for index in range(rowCount):
        try:
            os.remove(linuxPath + deleteFiles[index][0] + ".pdf")
            myCursor.execute(f"INSERT INTO deletedFiles(fileName,deletedDate) VALUES('{deleteFiles[index][0]}','{deleteFiles[index][1]}');")
            mydb.commit()
        except Exception as e:
            print(e)
            continue

        myCursor.execute("DELETE FROM pdfManager_TB WHERE deleteFlag = 1;")
        mydb.commit()

def getDate(plusValue):
    nowDate = datetime.now() + timedelta(days=plusValue)

    nowYear = nowDate.year
    nowMonth = nowDate.month
    nowDay = nowDate.day

    dayStr = str(nowYear) + "-" + str(nowMonth) + "-" + str(nowDay)

    return dayStr

if __name__ == '__main__':
    sys.exit(main())