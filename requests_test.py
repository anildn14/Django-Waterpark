import requests
import random
import string
import json

def random_generator(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

url="http://127.0.0.1:8000/park/"

admin_access_token="23a042bf5fd8e98688cf659c633667c92d555396"
normal_access_token="6f38cf38677a2f033a831f1d2cd09f894b821815"

# if content-type in header is kept blank it works properly
# elif "Content-type":"application/json" then throws utf error
# elif "Content-type":"multipart/form-data" {"detail":"Multipart form parse error - Invalid boundary in multipart: None"}
# "Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"
# content-type to be kept empty, the request methods automatically sets the content type acc to get/post/put/patch/delete

######################## GET #########################

headers={"Authorization":'Token {}'.format(normal_access_token)}
req=requests.get(url,headers=headers,timeout=5)	#url+"1/"
print "\nreq :",req
print "\nreq.status_code :",req.status_code
print "\nreq.text ",req.text
print "\nreq.content :",req.content
print "\nreq.encoding :",req.encoding
print "\nreq.headers :",req.headers
print "\n######################## GET FINISH #########################"
result = json.loads(req.text)   # will NOT work; see above
print len(result)
for i in range(len(result)):
	print "result:",result[i]['park_docs']

######################## POST ########################
'''
headers={"Authorization":'Token {}'.format(admin_access_token)}
files = {'park_logo': open('/home/user/Desktop/porc.jpg','rb'),"park_docs":open('/home/user/Desktop/auto_install_softwares.sh','rb')}
params=dict(
    park_name= random_generator(),
    park_address= "Mumbai",
    park_time= "9:00 AM to 7:00 PM",
    park_url= "http://www.shangrilawaterpark.com/",
    park_price= "888",
    park_likes= 5,
    is_fav= False)
print "\nparams :",type(params),params
print "\nfiles :",type(files),files
par=json.dumps(params)
# fil=json.dumps(files)
print "\nparams :",par,type(par)
req=requests.post(url,headers=headers,data=params,files=files)
req.encoding = 'utf-8'
print "\nreq :",req
print "\nreq.status_code :",req.status_code
print "\nreq.text :",req.text
print "\nreq.content :",req.content
print "\nreq.encoding :",req.encoding
print "\nreq.headers :",req.headers
print "\n######################## POST FINISH ########################"
'''
######################## PUT #########################
'''
wp_id=13
headers={"Authorization":'Token {}'.format(admin_access_token)}
files = {'park_logo': open('/home/user/Desktop/porc.jpg','rb'),"park_docs":open('/home/user/Desktop/auto_install_softwares.sh','rb')}
params=dict(
    park_name= "U2W6LODL",
    park_address= random_generator(),
    park_time= "9:00 AM to 7:00 PM",
    park_url= "http://www.shangrilawaterpark.com/",
    park_price= "888",
    park_likes= 5,
    is_fav= False)
print "\nparams :",params
req=requests.put(url+"%s/"%wp_id,headers=headers,data=params,files=files)
print "\nreq :",req
print "\nreq.status_code :",req.status_code
print "\nreq.text ",req.text
print "\nreq.content :",req.content
print "######################## PUT FINISH #########################"
'''
####################### PATCH ########################
'''
wp_id=6
headers={"Authorization":'Token {}'.format(admin_access_token)}
# params=dict(park_address= random_generator())
# print "\nparams :",params
files = {"park_docs":open('/home/user/Desktop/waterparks_list.txt','rb')}
print "files :",files
req=requests.patch(url+"%s/"%wp_id,headers=headers,files=files)#,data=params)
print "\nreq :",req
print "\nreq.status_code :",req.status_code
print "\nreq.text ",req.text
print "\nreq.content :",req.content
print "\n####################### PATCH FINISH ########################"
'''
####################### DELETE #######################
'''
wp_id=35
headers={"Authorization":'Token {}'.format(admin_access_token)}
req=requests.delete(url+"%s/"%wp_id,headers=headers)
print "\nreq :",req
print "\nreq.status_code :",req.status_code
print "\nreq.text ",req.text
print "\nreq.content :",req.content
print "\n###################### DELETE FINISH ########################"
'''
##########################################################
'''
wp_list=[
['Accoland', 'Guwahati, Assam','10:00 AM to 6:30 PM','http://www.accoland.in/','500',0,0,'http://www.accoland.in/images/accoland.jpg','/home/user/Desktop/dummy.pdf'],
['Amaazia', 'Surat, Gujarat','10:30 AM to 5:30 PM','https://www.amaazia.com/','899',0,0,'https://www.amaazia.com/images/LandingImages/categories/waterpark.png','/home/user/Desktop/dummy.pdf'],
['Anandi Water Park', 'Lucknow, Uttar Pradesh','10:00 AM to 5:00 PM','http://www.anandiwaterpark.co.in/','500',0,0,'http://www.anandiwaterpark.co.in/images/logo.png','/home/user/Desktop/dummy.pdf'],
['Aqua Marina Water Parks and Resorts', 'Hooghly, Kolkata','10:00 AM to 6:00 PM','http://www.aquamarinapark.com/','500',0,0,'http://www.aquamarinapark.com/images/thevedamvillage.png','/home/user/Desktop/dummy.pdf'],
['Aqua Village', 'Pinjore, Haryana','10:00 AM to 7:00 PM','http://www.aquavillage.in','800',0,0,'https://scontent-bom1-1.xx.fbcdn.net/v/t1.0-1/p720x720/57071018_2353809264686862_1885432128309559296_n.jpg?_nc_cat=107&_nc_ht=scontent-bom1-1.xx&oh=ed225ffab2efded48f8cdd772f5d1822&oe=5D3623BD','/home/user/Desktop/dummy.pdf'],
['Aquamagica, Adlabs Imagica', 'Khopoli, Maharashtra','10:00 AM to 7:00 PM','https://www.adlabsimagica.com/','899',0,0,'https://www.entryeticket.com/image/cache/data/Theme%20park/imagica-800x800.jpg','/home/user/Desktop/dummy.pdf'],
['Aquatica', 'Kouchpukur, Kolkata','10:00 AM to 6:00 PM','http://www.aquaticaindia.in/','1000',0,0,'http://www.aquaticaindia.in/assets/images/logo.png','/home/user/Desktop/dummy.pdf'],
['Black Thunder', 'Mettupalayam, Tamil Nadu','10:00 AM to 6:00 PM','http://btpark.org/','750',0,0,'http://btpark.org/assets/wp-content/uploads/2015/04/logo2.png','/home/user/Desktop/dummy.pdf'],
['Dolphin the Water World', 'Agra, Uttar Pradesh','12:00 PM to 6:00 PM','http://www.dolphinwaterworld.com/','500',0,0,'http://www.dolphinwaterworld.com/images/logo1.png','/home/user/Desktop/dummy.pdf'],
['Dream World', 'Thrissur, Kerala','10:30 AM to 6:00 PM','http://dreamworldwaterpark.com/','800',0,0,'https://scontent-bom1-1.xx.fbcdn.net/v/t1.0-9/20664396_1308072319302696_5288013518806834900_n.jpg?_nc_cat=111&_nc_ht=scontent-bom1-1.xx&oh=0c1c60e657200fd418c36572ac4d0fb1&oe=5D31618E','/home/user/Desktop/dummy.pdf'],
['Fantasy Park', 'Palakkad, Kolkata','10:00 AM to 6:00 PM','http://fantasypark.in/','600',0,0,'https://media-cdn.tripadvisor.com/media/photo-o/09/89/85/01/fantasy-park.jpg','/home/user/Desktop/dummy.pdf'],
['Fun N Food Park', 'Gurgaon, New Delhi','9:30 AM to 7:00 PM','https://www.funnfood.com/delhi/index.php','1000',0,0,'https://www.funnfood.com/delhi/images/logo.png','/home/user/Desktop/dummy.pdf'],
['Fun N Food Park', 'Nagpur, Maharashtra','9:30 AM to 7:00 PM','https://www.funnfood.com/nagpur/index.php','1380',0,0,'https://www.funnfood.com/nagpur/images/logo.png','/home/user/Desktop/dummy.pdf'],
['Funcity', 'Panchkula, Haryana','9:30 AM to 6:30 PM','https://www.funcitysurya.com/','1090',0,0,'https://www.funcitysurya.com/wp-content/uploads/2016/09/fclogo4.png','/home/user/Desktop/dummy.pdf'],
['Funtasia Water Park', 'Patna, Bihar','10:00 AM to 6:00 PM','http://www.funtasiaisland.com/','500',0,0,'http://www.funtasiaisland.com/templates/ecoplanet-fts/images/logo.png','/home/user/Desktop/dummy.pdf']
]
# print wp_list[0][7].split('.')[-1]

######################## POST ########################

for x in range(len(wp_list)):
	headers={"Authorization":'Token {}'.format(admin_access_token)}
	image_url=wp_list[x][7]
	image_ext=wp_list[x][7].split('.')[-1]
	r = requests.get(image_url)
	image_name='media/%s.%s'%(wp_list[x][0],image_ext)
	with open(image_name,'wb') as f: 
		f.write(r.content)
	# files = {'park_logo': open(image_name,'rb'),"park_docs":open(wp_list[x][8],'rb')}
	# params=dict(
	#     park_name= wp_list[x][0],
	#     park_address= wp_list[x][1],
	#     park_time= wp_list[x][2],
	#     park_url= wp_list[x][3],
	#     park_price= wp_list[x][4],
	#     park_likes= wp_list[x][5],
	#     is_fav= wp_list[x][6])
	# # print "\nparams :",type(params),params
	# # print "\nfiles :",type(files),files
	# req=requests.post(url,headers=headers,data=params,files=files)
	# req.encoding = 'utf-8'
	# print "\nreq :",req
	# print "\nreq.status_code :",req.status_code
	# print "\nreq.text :",req.text
	# print "\nreq.content :",req.content
	# print "\nreq.encoding :",req.encoding
	# print "\nreq.headers :",req.headers
print "\n######################## POST FINISH ########################"

'''