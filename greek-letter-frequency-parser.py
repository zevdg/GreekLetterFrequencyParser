import sys
import unicodedata
import collections

filename = 'plato book 1.txt'
koronisOrd = 8125;

def remove_accents(inputChar):
	if ord(inputChar) == koronisOrd:
		return inputChar
	nkfd_form = unicodedata.normalize('NFKD', inputChar)
	return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


print(sys.stdout.encoding)
d = dict()

with open(filename,  encoding="utf8") as f:
	while True:
		c = f.read(1)
		if not c:
			print("End of file")
			break
		
		#get ascii or utf-8 code as integer
		ordC = ord(c)
		
		#if this isn't a greek letter
		#913-969 is basic greek (no accents)
		#7936-8191 (0x1f00 - 0x1fff) is Greek Extented (with accents)
		if ordC not in range(913, 969) and ordC not in range(7936, 8191):
			continue
			
		cNorm = remove_accents(c)
		upperC = cNorm.upper()
		
		if upperC in d:
			d[upperC] += 1
		else:
			d[upperC]=1
		
	sortedDict = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
	for key in sortedDict:
		label = key
		if(ord(key) == koronisOrd):
			label = "Koronis"
		print("{0}:{1}".format( label, d[key]))


