# -*- coding: utf-8 -*-
import urllib2,urllib,json

class Twitter:
	def __init__(self, userdata):
		self.user = userdata
		self.url  = "twitter.com"
		self.serviceName = "Twitter API"
		self.serviceURL = "twitter.com"
	
	def setUser(self,userdata):
		self.user = userdata
	def setAuthService(self,service):
		if service == "twitter":
			self.serviceName = "Twitter API"
			self.serviceURL = "twitter.com"
			self.url = "twitter.com"

		if service == "wassr":
			self.serviceName = "API Authentication"
			self.serviceURL = "api.wassr.jp:80"
			self.url = "api.wassr.jp"
		
	def setAuthHandler(self):
		#ユーザ名等設定する
		#初回時のみで充分かなぁ
		auth_handler = urllib2.HTTPBasicAuthHandler()
		auth_handler.add_password(self.serviceName,self.serviceURL,self.user['user'],self.user['pass'])
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
		return opener
	
	def get(self,username): 
		self.setAuthHandler()
		data = urllib2.urlopen("http://twitter.com/statuses/friends_timeline.json")
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)
		
	def getPublicTimeline(self):
		data = urllib2.urlopen("http://"+self.url+"/statuses/public_timeline.json")
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)
		
	def getReplies(self,username):
		self.setAuthHandler()
		data = urllib2.urlopen("http://"+self.url+"/statuses/replies.json")
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)
	
	def getDM(self,username):
		self.setAuthHandler()
		s = "http://"+self.url+"/direct_messages.json"
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		a = json.read(urlstring)
		print a
		return self.parseTwitJSONDM(a)
		
	def getWithPage(self,username,num): 
		# page番号つきget
		self.setAuthHandler()
		s = "http://"+self.url+"/statuses/friends_timeline.json?page="+str(num)
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)

	def getWithUser(self,user): 
		# page番号つきget
		self.setAuthHandler()
		s = "http://"+self.url+"/statuses/user_timeline/"+user+".json"
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)
	
	def getWithUserPage(self,username,num): 
		# page番号つきget
		self.setAuthHandler()
		s = "http://"+self.url+"/statuses/user_timeline/"+username+".json?page="+str(num)
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSON(a)

	def getFollowersLite(self,username):
		# followerを取得	
		
		self.setAuthHandler()
		# ここ変える
		s = "http://"+self.url+"/statuses/followers.json?lite=true"
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		a = json.read(urlstring)
		return self.parseTwitJSONFollowers(a)
	
	def parseTwitJSON(self,a):
		result = []
		for x in a:
			resultSub = []
			#resultSub.append(x['created_at'])
			y = x['user']
			resultSub.append(y['screen_name'])
			resultSub.append(x['text'])
			resultSub.append(x['created_at'])
			result.append(resultSub)
			#print resultSub[0]+resultSub[1]
		return result
	
	def parseTwitJSONDM(self,a):
		result = []
		for x in a:
			resultSub = []
			#resultSub.append(x['created_at'])
			y = x['sender']
			resultSub.append(y['screen_name'])
			resultSub.append(x['text'])
			resultSub.append(x['created_at'])
			result.append(resultSub)
			#print resultSub[0]+resultSub[1]
		return result	
	
	def parseTwitJSONFollowers(self,a):
		result = []
		for x in a:
			resultSub = []
			#resultSub.append(x['created_at'])
			#y = x['sender']
			resultSub.append(x['screen_name'])
			#resultSub.append(x['text'])
			#resultSub.append(x['created_at'])
			result.append(resultSub)
			#print resultSub[0]+resultSub[1]
		return result		
	
	def put(self,s):
		self.setAuthHandler()
		postdata = {}
		postdata['status'] = s.encode('utf-8')
		#postdata['source'] = s
		param = urllib.urlencode(postdata)
		data = urllib2.urlopen("http://"+self.url+"/statuses/update.json",param)
		print data.read()
	"""
		サインインします
		In: なし(クラスメンバ変数でuser,pass)
	"""
	"""def signIn(self):
		import cookielib
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		return opener
	def putHtml(self,s):
		import cookielib
		
		#cookie管理オブジェクト作る
		try:
			opener = signIn()

		except:
			pass

		opener.open("http://twitter.com/sessions","username=&s&password%s" % (self.user['user'],self.user["pass"]))
		postdata = {}
		postdata['status'] = s.encode('utf-8')
		#postdata['source'] = s
		param = urllib.urlencode(postdata)
		data = urllib2.urlopen("http://"+self.url+"/statuses/update",param)
		print data.read()"""
	def getUserPageWithScraping(self,user,num):
		self.setAuthHandler()
		s = "http://"+self.url+"/"+user+"?page="+str(num)
		print "url+" +s
		data = urllib2.urlopen(s)
		urlstring = data.read()
		if num == 1:
			return self.scrapeTwit(urlstring,True)
		else:
			return self.scrapeTwit(urlstring,False)
		
	# HTMLをスクレイプします。
	def scrapeTwit(self,a,isFirst):
		import re
		# <span class="entry-title entry-content">~</span>(最短)
		#reg = re.compile(r'<(.*?)>')
		retList = []
		
		reg = re.compile("<span class=\"entry-title entry-content\">([\w\W]*?)</span>[\w\W]*?<abbr class=\"published\" title=\"([\w\W]*?)\">.*?</abbr>",re.MULTILINE)
		reg2 = re.compile("<span class=\"entry-content\">([\w\W]*?)</span>[\w\W]*?<abbr class=\"published\" title=\"([\w\W]*?)\">.*?</abbr>",re.MULTILINE)
		# もし1ページ目なら、最新の発言も取ってくる
		#if isFirst :
		#	a3 = reg.findall(a)
		#	retList.append( a3[0] )

		a2 = reg2.findall(a)
		for aa in a2:
			retList.append( (aa[0].strip(),aa[1]) )

		return retList
