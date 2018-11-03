import math
class CuckooHash:
	
	def __init__(self):
		self.len=100#length of tables
		self.hashtable=[[None for _ in range(self.len)] for _ in range(3)]
		self.stash=list()#stash to store elements that create infinite loops
		self.population=0

	def stringHashFunction(self,str):
		p1=37#a prime number
		sum1,sum2,sum3=37,5381,0
		for i in range(len(str)-1,-1,-1):
			sum1 = (sum1+ord(str[i]))*p1#calculated using Horner's rule
			sum2 = ((sum2 << 5) + sum2) + ord(str[i]) #djb2 algorithm
			sum3 = ord(str[i]) + (sum3 << 6) + (sum3 << 16) - sum3#sdbm algorithm
		sum1=sum1%self.len
		sum2=sum2%self.len
		sum3=sum3%self.len
		return (sum1,sum2,sum3)

	def integerHashFunction(self,key): 
		#MAD function
		A = ((5**(1/2))-1)/2 #Conjugate of Golden Ratio
		b = 29 #random prime number
		ans1 = math.floor(A*key + b) % self.len
		#Combination of Mid-squared method and Random Generator
		key = key**2
		l = 10 ** (len(str(key))//2 + 2)
		key = key % l #Removing the front of the unwanted digits
		l = 3 if key>999 else len(str(key))
		key=int(str(key)[0:l]) #getting the final middle 3 digits of the squared key
		random.seed(key) #seeding the random generator with the middle 3 digits
		ans2 = math.floor(random.random()*self.len)
		#Basic Multiplication method
		A = ((5**(1/2))-1)/2 #Conjugate of Golden Ratio
		ans3 = math.floor(self.len * ((key*A) % 1))
		return (ans1,ans2,ans3)

	def insert(self,key,count=0,i=0):
		if(isinstance(key,int)):
			hashvalues=self.integerHashFunction(key)
		else:
			hashvalues=self.stringHashFunction(key)
		if(count>math.floor(math.log(self.len))):
			self.insertIntoStash(key)
			return
		if(self.hashtable[i][hashvalues[i]]==None):
			self.hashtable[i][hashvalues[i]]=key
		else:
			temp=self.hashtable[i][hashvalues[i]]
			self.hashtable[i][hashvalues[i]]=key
			self.insert(temp,count+1,(i+1)%3)
		self.population += 1
		if self.population

	def insertIntoStash(self,key):

	def delete(self,key):
		if isinstance(key,int):
			index = self.integerHashFunction(key)
		else:
			index = self.stringHashFunction(key)
		if hashtable[0][index[0]]==key:
			hashtable[0][index[0]]=None
		elif hashtable[1][index[1]]==key:
			hashtable[1][index[1]]=None
		elif hashtable[2][index[2]]==key:
			hashtable[2][index[2]]=key
		else:
			self.deleteFromStash(key)

	def deleteFromStash(self,key):
		s,e=0,len(self.stash)
		while s<=e:
			m=(s+e)//2
			if self.stash[m]==key:
				self.stash.pop(key)
			elif self.stash[m]>key:
				e=m-1
			else
				s=m+1

	def lookup(self,key):
		if(isinstance(key,int)):
			hashvalues=self.integerHashFunction(key)
		else:
			hashvalues=self.stringHashFunction(key)
		if hashtable[0][index[0]]==key:

		elif hashtable[1][index[1]]==key:
			
		elif hashtable[2][index[2]]==key:
			
		else:
			self.lookupInStash(key)

	def rehash(self):

	def print(self):

def main():




