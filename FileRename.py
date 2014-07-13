import os 
baseDir = "/home/philkuz/Videos/TV/";
archer = baseDir+"Archer/[2014]Season 05/";
fargo = baseDir+"Fargo/[2014]Season 01/";
got = baseDir+"Game of Thrones/Season 04/";
review = baseDir+"Review (Comedy Central)/Season 01/";
season = 3;

def rewriteWf(filename):
	
	output = "WilfredS"+str(season)+"E";
	idx = filename.find(".");
	for char in filename:
		if char == ".":
			break;
		if char.isdigit():
			output+=char;
	output+=filename[idx:];
	print output;
	#os.rename(filename, output);
def adjustment(filename):
	output = filename[:7]+"0"+filename[8:];
	os.rename(filename, output);
def archerSus(filename):
	splat = filename.split(".");
	output = "Archer";
	for string in splat:
		if string.upper().find("S05") != -1:
			output+=string;
	output+="."+splat[len(splat)-1];
	if not (len(splat) < 3):
		os.rename(filename,output);
def fargoSus(filename):
	splat = filename.split(".");
	output = "";
	for string in splat:
		if string != splat[len(splat)-1]:
			output+=string;
	output += "."+splat[len(splat)-1];
	os.rename(filename, output);
#Used for when it has the title and the season and episode formated like this: S02E05
def gotSus(directory):
	count = 0;
	nigLst = [];
	nigDic = {};
	curLst = [];
	output = [];
	cert = [];
	title = "";
	for filename in os.listdir(directory):

		curLst = titleHandler(filename);
		if count == 0:
			nigLst = curLst;
			for cur in curLst:
				nigDic[cur] = 1;
		else:
			for key in nigDic:
				for cur in curLst:
					if cur == key:
						nigDic[key] += 1;
		count+=1;
	for key in nigDic:
		if nigDic[key] >= count:
			cert.append(key);
	for nig in nigLst:
		if nig in cert and not isExtension(nig) and not cliche(nig):
			output.append(nig);
	print output;
	for out in output:
		title+=out.title();
	print title;
	for filename in os.listdir(directory):
		curLst = titleHandler(filename);
		index = -1;
		for ass in curLst:
			index+=1;
			if ass.upper().find("S01") != -1:
				break;
		output = title+curLst[index].upper()+"."+curLst[len(curLst)-1];
		print output;
		#print filename;
		os.rename(filename, output);
#breaks up the title into an array
def titleHandler(filename):
	specChar = [" "];
	for c in filename:
		if (not c.isalnum()) and c != " ":
			contained = False;
			for char in specChar:
				if char == c:
					contained = True;
					break;
			if not contained:
				specChar.append(c);
	lst  = filename.split(specChar[0]);
	if len(specChar) > 1:
		for i in range(1, len(specChar)):
			tempLst = [];
			for lol in lst:
				tempLst.append(lol.split(specChar[i]));
			#print tempLst;
			lst = [];
			for tmp in tempLst:
				if type(tmp) is not str:
					for word in tmp:
						lst.append(word);
				else:
					lst.append(tmp);
	return lst;
#Used to update when the name is in this format : Episode1.avi;
def noSes(directory):
	season = "01";
	title = "Review";
	for filename in os.listdir(directory):
		curN = "";
		output = title+"S"+season+"E";
		fucka = filename.split(".");
		for k in fucka[0]:
			if(k.isdigit()):
				curN+=k;
		if len(curN) < 2:
			curN = "0"+curN;		
		output+=curN+"."+fucka[len(fucka)-1];
		print output;
		os.rename(filename, output);
def isExtension(string):
	ext =["mp4", "mkv", "avi"];
	if string in ext:
		return True;
	else:
		return False;
def cliche(string):
	clicheL = ["hd"];
	for clch in clicheL:
		if string.lower().find(clch) != -1:
			return True;
	return False;
os.chdir(review);
noSes(review);
