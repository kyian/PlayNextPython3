#!/usr/bin/env
import os
import shelve


#To not run the playfile or data record.
exclusionList=['Playnext.py', 'nextStop']
	
class FileWalker:
	#get the list and find last place
	def __init__(self):
		self.baseDir = os.getcwd()
		self.curDir = os.getcwd()
		[self.nextStop,self.curDir, self.size] = self.getShelv()
		self.itr = os.walk(self.baseDir)
		self.fileNumber=0
		self.fileList=[]
		self.playFirst = False
		if self.size == 0:
			self.initList()
		else:
			self.moveToPoint()
			
		

	def setShelv(self):
		db = shelve.open("nextStop")
		db['last'] = self.nextStop
		db['dir'] = self.curDir
		db.close()
		
	
	def getShelv(self):
		db = shelve.open("nextStop")
		size = len(db)
		if(size!=0):
			nextStop= db['last']
			diir=db['dir']
		else:
			nextStop='empty'
			diir='empty'
		db.close()
		return [nextStop, diir, size]

	def playFile(self,loc):
		# Play the file at loc
		os.startfile(loc)
		
	def initList(self):
		print('New list has been generated')
		#new list get first entry
		self.itr = os.walk(self.baseDir)
		[dirname,subdirs,files] = next(self.itr)
		self.nextStop=files[0]
		print(self.nextStop)
		self.curDir=dirname
		self.fileList=files
		self.setShelv()
		self.playFirst=True
		
	# Moves the iterator to the correct point.  If thhe point doesn't exist
	#    Thhe initList function is called to make a new list.
	def moveToPoint(self):
		#move the walk to the dir of curdir nextStop
		try:
			[dirname,subdirs,files] = next(self.itr)
		except:
			print('If this didn\'t work you are pretty much screwed \n')
		if self.curDir == dirname:
			return
		
		while True:
			#move to next subdir
			try:
				[dirname,subdirs,files] = next(self.itr)
				if self.curDir == dirname:
					self.fileList=files
					break
			except:
				print('directory not found')
				initList()
				return 2
		#end while loop
		#find the index and start anew if there are no matches
		try:
			self.fileNumber = self.fileList.index(self.nextStop)
		
		except:
			print('file not found')
			initList()
			return 1
		return 0
		
	def moveToNext(self):
		try:
			#moves the file in the list.  returns the full file dir
			if self.fileNumber+1 < len(self.fileList):
				# more entries in list so just increase size
				self.fileNumber = self.fileNumber + 1
				print('inpath')

			else:
				#done in current dir.  Move to next
				print('it went else')
				[dirname,subdirs,files] = next(self.itr)
			
				# make sure there are files in the next dir
				while len(files) == 0:
					[dirname,subdirs,files] = next(self.itr)
				
				#set the walker junk
				self.fileNumber=0
				self.curDir = dirname
				self.fileList= files
				
			self.nextStop = self.fileList[self.fileNumber]
				
			self.setShelv()
			
			return os.path.join(self.curDir,self.nextStop)
		except:
			print('There is a problem moving to the next thing')
			initList()
			return 'Oh god why?'
		
	def playNext(self):
		self.excluMoveOff()
		#move iterator and play the next file
		temp = self.moveToNext()
		self.excluMoveOff()
		print(self.playFirst)
		if self.playFirst:
                        self.playCurrent()
                        self.playFirst=False
                        return
		self.playFile(temp)
		self.setShelv()
		
		
	def playCurrent(self):
	#play the current file
		self.excluMoveOff()
		print(os.path.join(self.curDir,self.nextStop))
		self.playFile(os.path.join(self.curDir,self.nextStop))
		
	def excluMoveOff(self):
		while self.exclCheck():
			temp = 'ttt'
		return 0
		
		
	def exclCheck(self):
		if self.nextStop in exclusionList:
			self.moveToNext()
			return True
		return False
		
		
if __name__== '__main__':
	print('what')

	temp = FileWalker()
#	temp.playCurrent()
	temp.playNext()
	
	input('press enter to quit')
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
