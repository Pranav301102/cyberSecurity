# importing library
import requests
import os
import mongo
# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
	print('-----------Subdomain Scanner Started-----------\n')
	
	# loop for getting URLs
	result = []
	for subdomain in sub_domnames:
		# making url by putting subdomain one by one
		url = f"https://{subdomain}.{domain_name}"
		
		# using try catch block to avoid crash of
		# the program

		try:
				# sending get request to the url
			requests.get(url, timeout=2)
				
				# if after putting subdomain one by one url
				# is valid then printing the url
			result.append(f'{url}')
		# if url is invalid then pass it
		except:
			pass
	return(result)
print('\n')
 
# main function
if __name__ == '__main__':
	dom_name = 'github.com'

	# opening the subdomain text file
with open('Subdomain_names.txt','r') as file:
	
		# reading the file
		name = file.read()
		
		# using splitlines() function storing the
		# list of splitted strings
		sub_dom = name.splitlines()
		
	# calling the function for scanning the subdomains
	# and getting the url
print('\n'.join(domain_scanner(dom_name,sub_dom)))

def audit(foo, id):
    result = domain_scanner(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
