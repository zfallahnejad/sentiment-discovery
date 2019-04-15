# Prepare Input data

## Crawl persian tweets

## Extract unique tweets
Extract unique tweets from crawled tweets(`--input_file`) and remove mentions and urls and # marks.
```
python3.6 prepare_data.py --get_unique_tweets --input_file ./data/twitter/tweets.iran.txt --output_json_file ./data/twitter/tweets_iran_unique.json
```

## Train
```
python3.6 main.py --nhid 64 --seed 123 --data ./data/twitter/tweets_iran_unique.json --loose-json \
        --save output/lang_model_nhid64_ds128/lang_model_nhid64_ds128.pt
```


## Initial steps:



6.Apply following changes to transfer.py:
	* For non cuda systems change this line:
		```
		sd = x = torch.load(f)  -->  sd = x = torch.load(f, map_location='cpu')
		```
	* A little change at end of this file:
		remove exit() and change if to if not.
	* For `Persian` version change following lines:
		```
		data_parser.set_defaults(split='1.', data='data/binary_sst/train.csv')
		data_parser.set_defaults(valid='data/binary_sst/val.csv', test='data/binary_sst/test.csv')
		-->
		data_parser.set_defaults(split='1.', data='data/Label/train.csv')
		data_parser.set_defaults(valid='data/Label/val.csv', test='data/Label/test.csv')
		```
7. Apply following changes to classifier.py:
	* change this line:
	```
	num_char = length_batch.sum().data[0]--> num_char = length_batch.sum().data.item()
	```
	* A little change at end of this file:
		remove exit() and change if to if not.
8. pip install seaborn
9. Apply following changes to generate.py:
	* change these lines:
	```
	neuron = neuron[0] --> neuron = neuron.item()
	```
	*For Persian version:
	```
	args.data_size = 256 --> args.data_size = 128
	```
	```
	matplotlib.use('Agg')
	import matplotlib.pyplot as plt
	--> 
	import matplotlib.pyplot as plt
	plt.switch_backend('agg')
	```
	* For Persian version add these lines:
	```
	vocabulary_map = {'\u0627': 0,'\u0628': 1,'\u067e': 2,'\u062a': 3,'\u062b': 4,'\u062c': 5,'\u0686': 6,'\u062d': 7,'\u062e': 8,'\u062f': 9,'\u0630': 10,'\u0631': 11,'\u0632': 12,'\u0698': 13,'\u0633': 14,'\u0634': 15,'\u0635': 16,'\u0636': 17,'\u0637': 18,'\u0638': 19,'\u0639': 20,'\u063a': 21,'\u0641': 22,'\u0642': 23,'\u0643': 24,'\u06af': 25,'\u0644': 26,'\u0645': 27,'\u0646': 28,'\u0648': 29,'\u0647': 30,'\u0649': 31,'\ufefb': 32,'\u0621': 33,'\U0001f602': 34,'\U0001f534': 35,'\U0001f539': 36,'\u270c': 37,'\U0001f447': 38,'\U0001f538': 39,'\U0001f339': 40,'\u2764': 41,'\U0001f448': 42,'\u2b55': 43,'\U0001f601': 44,'\U0001f53b': 45,'\U0001f3fb': 46,'\U0001f1f7': 47,'\U0001f614': 48,'\U0001f64f': 49,'\U0001f1ee': 50,'\U0001f610': 51,'\U0001f923': 52,'\U0001f622': 53,'\u0660': 54,'\u0661': 55,'\u0662': 56,'\u0663': 57,'\u0664': 58,'\u0665': 59,'\u0666': 60,'\u0667': 61,'\u0668': 62,'\u0669': 63,' ': 64,'\u200c': 65,'\u066b': 66,'\u061b': 67,'\u060c': 68,'?': 69,'\u061f': 70,'a':71,'b':72,'c':73,'d':74,'e':75,'f':76,'g':77,'h':78,'i':79,'j':80,'k':81,'l':82,'m':83,'n':84,'o':85,'p':86,'q':87,'r':88,'s':89,'t':90,'u':91,'v':92,'w':93,'x':94,'y':95,'z':96,'\n':97,'_':98,u'\u2026':99,u'\u200d':100,u'\u201d':101,u'\u201c':102,u'\u2666':103,u'\u2013':104,u'\U0001f4a5':105,u'\U0001f914':106,u'\U0001f44f':107,u'\U0001f53a':108,u'\U0001f38b':109,u'\U0001f60a':110,u'\U0001f605':111,u'\U0001f62d':112,u'\U0001f60d':113,u'\U0001f341':114,u'\U0001f5a4':115,u'\U0001f604':116,u'\U0001f490':117,u'\U0001f609':118,u'\U0001f44a':119,u'\U0001f44d':120,u'\U0001f611':121,u'\u270a':122,u'\U0001f499':123,u'\U0001f60f':124,u'\U0001f621':125,u'\U0001f337':126,u'\U0001f494':127}
	vocabulary_map_reverse = {0: '\u0627',1: '\u0628',2: '\u067e',3: '\u062a',4: '\u062b',5: '\u062c',6: '\u0686',7: '\u062d',8: '\u062e',9: '\u062f',10: '\u0630',11: '\u0631',12: '\u0632',13: '\u0698',14: '\u0633',15: '\u0634',16: '\u0635',17: '\u0636',18: '\u0637',19: '\u0638',20: '\u0639',21: '\u063a',22: '\u0641',23: '\u0642',24: '\u0643',25: '\u06af',26: '\u0644',27: '\u0645',28: '\u0646',29: '\u0648',30: '\u0647',31: '\u0649',32: '\ufefb',33: '\u0621',34: '\U0001f602',35: '\U0001f534',36: '\U0001f539',37: '\u270c',38: '\U0001f447',39: '\U0001f538',40: '\U0001f339',41: '\u2764',42: '\U0001f448',43: '\u2b55',44: '\U0001f601',45: '\U0001f53b',46: '\U0001f3fb',47: '\U0001f1f7',48: '\U0001f614',49: '\U0001f64f',50: '\U0001f1ee',51: '\U0001f610',52: '\U0001f923',53: '\U0001f622',54: '\u0660',55: '\u0661',56: '\u0662',57: '\u0663',58: '\u0664',59: '\u0665',60: '\u0666',61: '\u0667',62: '\u0668',63: '\u0669',64: ' ',65: '\u200c',66: '\u066b',67: '\u061b',68: '\u060c',69: '?',70: '\u061f',71:'a',72:'b',73:'c',74:'d',75:'e',76:'f',77:'g',78:'h',79:'i',80:'j',81:'k',82:'l',83:'m',84:'n',85:'o',86:'p',87:'q',88:'r',89:'s',90:'t',91:'u',92:'v',93:'w',94:'x',95:'y',96:'z',97:'\n',98:'_',99:u'\u2026',100:u'\u200d',101:u'\u201d',102:u'\u201c',103:u'\u2666',104:u'\u2013',105:u'\U0001f4a5',106:u'\U0001f914',107:u'\U0001f44f',108:u'\U0001f53a',109:u'\U0001f38b',110:u'\U0001f60a',111:u'\U0001f605',112:u'\U0001f62d',113:u'\U0001f60d',114:u'\U0001f341',115:u'\U0001f5a4',116:u'\U0001f604',117:u'\U0001f490',118:u'\U0001f609',119:u'\U0001f44a',120:u'\U0001f44d',121:u'\U0001f611',122:u'\u270a',123:u'\U0001f499',124:u'\U0001f60f',125:u'\U0001f621',126:u'\U0001f337',127:u'\U0001f494'}
	```
	* For Persian version you must add these arguments:
		** nhid,load_model,save,text,gen_length,visualize,seed
	* Warning: if you choose gen_length to be a small number, you may face an error in heatmap part of the code(because of the small size of figure)