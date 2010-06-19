#!/usr/bin/python
# -*- coding: utf-8 -*-
# 今日の自分の1日の行動を取得します
import auth_api,jsonfile,traceback,toDate3,datetime,mail
import os

homePath = os.path.abspath(os.path.dirname(__file__))

def sendTmt(userName,toMail):
    # 引数 ユーザ名 メールアドレス
    getUser = userName
    print sendTmt, userName, toMail
    conf = auth_api.loadJSON(homePath+"/config.json")
    tw = auth_api.connect(conf["consumer_token"], conf["consumer_secret"], homePath)

    a = datetime.datetime.today()
    timeMax = a - datetime.timedelta(hours = a.hour - 6, minutes = a.minute, seconds = a.second)
    timeMin = timeMax - datetime.timedelta(days=1)
	#latestTime = datetime.datetime.today()-datetime.timedelta(days=1)
    pageNum = 50
    
    header = u"  :: Today's my tweets ::\n"+unicode(getUser,"utf-8")+u"さんの一日の発言です。\n\n"
    header = header.encode("iso-2022-jp")
    outSentence = ""
    try:
        flag = True
        for i in range(pageNum):
            if flag != True : break
            print getUser, pageNum
            for t in tw.user_timeline(getUser,page = i):
                td = toDate3.toDate3(t.created_at)
                if td - timeMin < datetime.timedelta(days =0):
                    flag = False
                    break
                if td - timeMax > datetime.timedelta(days = 0):
                    continue
                #if t[0].startswith("@") or t[0].startswith(".@"):
                #	continue
                s = unicode(t.text).encode("iso-2022-jp","ignore")
                outSentence = s + " " + td.strftime('%Y/%m/%d %H:%M:%S') + "\n\n" + outSentence
    except:
        traceback.print_exc()
    
    outSentence = header + outSentence
    outSentence += "\n  Today's my tweets by showyou(twitter.com/showyou)\n"
    #print unicode(outSentence,"iso-2022-jp").encode("cp932")
    
    userdata2 = jsonfile.read(homePath + "/user/twdata_tmt")
    user = userdata2["user"]
    passWord = userdata2["pass"]
    from_addr = user
    to_addr = toMail
    title = "today's my tweets:"+timeMin.strftime('%Y/%m/%d')
    title = title.encode("iso-2022-jp","ignore")
    msg = mail.create_message2(from_addr, to_addr, title, outSentence, 'ISO-2022-JP')
    mail.send_via_gmail(user,passWord,from_addr, to_addr, msg)


if __name__ == "__main__":
    import sys
    sendTmt(sys.argv[1], sys.argv[2])
