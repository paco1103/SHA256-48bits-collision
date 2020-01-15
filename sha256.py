import hashlib
#48bits = first 12 c, each 4bit = 1c -> 256bit = 64c
o_name = "Test".encode("utf-8")	#orginal student name	encrypt by utf-8
o_sid = "1234".encode("utf-8")		#orginal student id	encrypt by utf-8

hash_dict = {					#存新id:name in dict +now
		hashlib.sha256(o_sid).hexdigest()[:12] : o_sid,
		hashlib.sha256(o_name).hexdigest()[:12] : o_name	
	}
backup_dict = {					#存id:name in dict 上一個
		hashlib.sha256(o_sid).hexdigest()[:12] : o_sid,
		hashlib.sha256(o_name).hexdigest()[:12] : o_name	
	}
startLoop = True				#break loop
#揾第一個match and end program
if hash_dict[hashlib.sha256(o_sid).hexdigest()[:12]] ==  hash_dict[hashlib.sha256(o_name).hexdigest()[:12]]:
	print("X:", o_name.decode("utf-8"))
	print("Y:", o_sid.decode("utf-8"))
	print("H(X):", hashlib.sha256(o_name).hexdigest())
	print("H(Y):", hashlib.sha256(o_sid).hexdigest())
	print("First 48 bits same hash value:", hashlib.sha256(o_name).hexdigest()[:12])
	startLoop = False

i = 0
while startLoop:
	#將字串+n, for matching
	temp_name = o_name + str(i).encode("utf-8")
	temp_sid = o_sid + str(i).encode("utf-8")
	temp_namehash12 = hashlib.sha256(temp_name).hexdigest()[:12]
	temp_sidhash12 = hashlib.sha256(temp_sid).hexdigest()[:12]
	
	#update dict hash_dict
	hash_dict.update({temp_sidhash12 : temp_sid})
	#compare hash_dict id同value and backup_dict id同value
	if len(hash_dict) == len(backup_dict) and hash_dict[temp_sidhash12][:1] != backup_dict[temp_sidhash12][:1]:
		print("Find:")
		print("X:", backup_dict[temp_sidhash12].decode("utf-8"))
		print("Y:", hash_dict[temp_sidhash12].decode("utf-8"))
		print("H(X):", hashlib.sha256(backup_dict[temp_sidhash12]).hexdigest())
		print("H(Y):", hashlib.sha256(hash_dict[temp_sidhash12]).hexdigest())
		print("First 48 bits same hash value:", temp_sidhash12)
		break
	else:
		backup_dict.update({temp_sidhash12 : temp_sid})

	#同上,但相反output
	hash_dict.update({temp_namehash12 : temp_name})
	if len(hash_dict) == len(backup_dict) and hash_dict[temp_namehash12][:1] != backup_dict[temp_namehash12][:1]:
		print("Find:")
		print("X:", hash_dict[temp_namehash12].decode("utf-8"))
		print("Y:", backup_dict[temp_namehash12].decode("utf-8"))
		print("H(X):", hashlib.sha256(hash_dict[temp_namehash12]).hexdigest())
		print("H(Y):", hashlib.sha256(backup_dict[temp_namehash12]).hexdigest())
		print("First 48 bits same hash value:", temp_namehash12)
		break
	else:
		backup_dict.update({temp_namehash12 : temp_name})

	i += 1
	