from enigmaop import enigmaop

e1=enigmaop.start()
msg=e1.encrypt('0000000000000000000')
key=e1.getkey()
print(msg)
print(key)




dmsg=e1.decrypt(msg,key)
print(dmsg)


