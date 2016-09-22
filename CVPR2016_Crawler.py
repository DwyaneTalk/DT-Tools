import re
import os
import urllib.request


rootUrl = "http://www.cv-foundation.org/openaccess/CVPR2016.py"
indexUrl = "http://www.cv-foundation.org/openaccess/"
pdfPat =  r"(?<=href=\").+?pdf(?=\")|(?<=href=\').+?pdf(?=\')"
localDir = "D:\\CVPR2016\\"
def getPDFLinkList(rootUrl, pat):
    htmlReq = urllib.request.Request(rootUrl)
    htmlResponse = urllib.request.urlopen(htmlReq)
    htmlTextData = htmlResponse.read()
    htmlTextData = htmlTextData.decode()
    pdfLinkList = re.findall(pat, htmlTextData)
    return pdfLinkList

if __name__ == "__main__":
    if os.path.exists(localDir) == False:
        os.makedirs(localDir)
    count = 0
    downCount = 0
    for pdfUrl in getPDFLinkList(rootUrl, pdfPat):
        count = count + 1
        fileName = pdfUrl.split('/')[2]
        localPath =localDir + '%03d_' %count + fileName

        try:
            urllib.request.urlretrieve(indexUrl + pdfUrl, localPath)
        except Exception as err:
            print("[%03d] failed for %s, Error : %s" %(count, fileName, err))
            continue
        print("[%03d] succeed for %s" %(count, fileName))
        downCount = downCount + 1
    print("total %d papers download, ans stored in %s" %(downCount, localDir))



