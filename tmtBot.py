#!/usr/bin/python
# -*- coding: utf-8 -*-
# twitter/tmtの監視を行う

# twitter側の処理
# followされてたらfollowしかえす
# removeされたらremoveする

# D来てたらD処理
# コマンド
# D todays start mail でmailに送ります
# D todays stop で 停止(削除)
# D todays settime time でtimeに送ります。(15分単位の予定)
# D todays get mail で今すぐ送ります
import twitter3,jsonfile,datetime,toDate,picklefile


if True:
#if False:
	homePath = "./"
else:
	homePath = "/home/yuki/tmt/"

def tmtBot(userData):

	try:
		latestTime = picklefile.read(homePath+"user/latesttime")
	except:
		latestTime = datetime.datetime.today()-datetime.timedelta(days=1)

	authData = jsonfile.read(homePath+"user/twdata_todays")
	tw = twitter3.Twitter(authData)

	analyzeDM(userData,tw,latestTime)
	latestTime = datetime.datetime.today()
	
	picklefile.write(homePath+"user/latesttime",latestTime)


def analyzeDM(userData,tw,latest):
	# DM 取得解析
	a = tw.getDM("todays")
	a.reverse()
	for x in a:
		print x[0],
		print ":",
		print x[1].encode("cp932")
		
		# 最終更新時刻以前のログはカット
		if toDate.toDate(x[2]) - latest < datetime.timedelta(days =0) :
			print "pass"
			continue;
		xs = x[1].encode("utf-8")
		cmd = xs.split()#xsをスペースで分割

		#xs の解析で命令処理
		flag = False
		id = -1
		for u in range(len(userData)):
			if userData[u]["user"] == x[0]:
				flag = True
				id = u
				break

		if cmd[0] == "start":
			print cmd
			print len(cmd)
			if len(cmd) < 2:
				print "error:start needs 1 arg"
				continue
			if flag :
				# keyが存在:更新
				userData[id]["mail"] = cmd[1]
			else:
				d = {}
				d["user"] = x[0]
				d["mail"] = cmd[1]
				d["now"] = False
				d["time"] = latest
				userData.append(d)
		elif cmd[0] == "get":
			if len(cmd) < 2:
				if flag:
					toMail = userData[i]["mail"]
				else:
					print "error: not registered user and none mail address"
					continue
			else:
				toMail = cmd[1]
				
			if flag :
				# keyが存在:更新
				userData[id]["mail"] = toMail
				userData[id]["now"] = True
			else:
				d = {}
				d["user"] = x[0]
				d["mail"] = toMail
				d["now"] = True
				userData.append(d)
		elif cmd[0] == "stop":
			if flag == False:
				print "error:stop - no key"
				continue
			print "delete user",
			print userData[id]["user"]
			del userData[id]

		else:
			print "error:no cmd"+xs

if __name__ == '__main__':
	try:
		userData = picklefile.read(homePath+"user/twdata_tmtMail")
	except:
		userData = []
		

	tmtBot(userData)
	picklefile.write(homePath+"user/twdata_tmtMail",userData)
