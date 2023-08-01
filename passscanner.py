import pyfiglet as fg
ole= fg.figlet_format('passscanner')
olee="#########.by olever.#############"
print(ole)
print(olee)


password=input('[1] enter your password:')

passwords=['12345678910','123','1234','12345','123456','1234567','12345678','123456789','mohammed2023','helloworld',1234, 'aprilqueen','12/1/1999','13/1/1999','14/1/1999','naser1999','naser2000','naser2001','abc123','iloveyou','I_Love_You','0000000000','princess','americanboy','americangirl','qwerty','password','azerty','dragon','killer','fuckin','alexandre','7777777','football','barcelona2023','123barcelona','barcelona123','baseball','mohammedgamer','omanigamer','gamers','footballplayer', 'drmohammed','drali','drmaryam','drlana','drsara','drlaya','rose2023','killer','pubg','pubgplayer','pubgmobileplayer','pubgmobile', 'callofduty','CallOfDuty','callofdutyplayer','ilovemybby','imlovingwithmygirlfriend','boyfriend','girlfriend'
,'sunshine','lazyboy','lazygirl','monkey','michael','michael123','tigger','colleagepassword','colleagepassword123','windowsuser','taylorswiftfan','leonardofan','fanage','chocolate','password123','password12','password123456789','mypassword', 'liverpool','liverpoolstudent','liverpoolcolleage','fuckyou','rashaad33','rashed123','ali1234','ali123','ali12345','ali123456','ali1234567','ali12345678' ,'aphcueqgglktu','internet','computer','whatever','starwars','benjamin','11111111', 'victoria','987654321','q1w2e3r4','elephant','jonathan','88888888','creative','passw0rd','mypassw0rd','scorpion','metallica','december','spiderman','slipknot','november123','november','123november','christian123','123christian']

if password in passwords:

 print(password +'\nyour password easy to hack')

else:

 print('good NotFound')

yes='yes'
no='no'
print('-----------------------')
print('Wait a Minute')
print('-----------------------')
advice=input('Whether your password is in the list or not, do you want tips to protect your password from guessing? yes/no\n')

if advice == no :
 print('ok thank U')

elif advice == yes :
 print('-------------------------------------------------------------------')
 print('[1]dont use personal information ,birthday,your full name,movies,\n')
 print('-------------------------------------------------------------------')
 print('[2]Make sure it contains symbols,numbers,capital and small letters\n')
 print('-------------------------------------------------------------------')
 print('[3]Dont Trust Two Factor Authentication There are always ways for hackers')
 print('-------------------------------------------------------------------')
 print('[4]thanks for understanding')
