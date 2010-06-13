#!/usr/bin/python
# -*- coding: utf-8 -*-
# 今日の自分の1日の行動を取得します
import twitter3,jsonfile,traceback,toDate,datetime,mail
import os

#if True:
if False:
	homePath = "./"
else:
	homePath = os.path.abspath(os.path.dirname(__file__)))

def sendTmt(userName,toMail):
	# 引数 ユーザ名 メールアドレス
	getUser = userName
	print sendTmt, userName, toMail
	userdata = jsonfile.read(homePath+"user/twdata_hama")
	tw = twitter3.Twitter(userdata)
	latestTime = datetime.datetime.today()-datetime.timedelta(days=1)
	pageNum = 50
	
	header = u"  :: Today's my twitter ::\n"+unicode(getUser,"utf-8")+u"さんの一日の発言です。\n\n"
	header = header.encode("iso-2022-jp")
	outSentence = ""
	try:
		flag = True
		for i in range(pageNum):
			if flag != True : break
			for t in tw.getWithUserPage(getUser,i+1):
				td = toDate.toDate(t[2])
				if td - latestTime < datetime.timedelta(days =0) :
					flag = False
					break
				#if t[0].startswith("@") or t[0].startswith(".@"):
				#	continue
				s = unicode(t[1]).encode("iso-2022-jp","ignore")
				outSentence = s + " " + td.strftime('%Y/%m/%d %H:%M:%S') + "\n\n" + outSentence
	except:
		traceback.print_exc()
	
	outSentence = header + outSentence
	outSentence += "\n  Today's my twitter by showyou(twitter.com/showyou)\n"
	#print unicode(outSentence,"iso-2022-jp").encode("cp932")
	userdata2 = jsonfile.read(homePath + "user/twdata_tmt")
	user = userdata2["user"]
	passWord = userdata2["pass"]
	from_addr = user
	to_addr = toMail
	title = "today's my twitter:"+latestTime.strftime('%Y/%m/%d')
	title = title.encode("iso-2022-jp","ignore")
	msg = mail.create_message2(from_addr, to_addr, title, outSentence, 'ISO-2022-JP')
	mail.send_via_gmail(user,passWord,from_addr, to_addr, msg)
	
if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print "usage tmt.py user mail"
		print "use test mode"	
		sendTmt("ha_ma","showyou41@gmail.com")
		exit()
	sendTmt(sys.argv[1],sys.argv[2])
