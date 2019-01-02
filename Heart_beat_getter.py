import auth

#Set MAC Address
MAC_ADDR = "F0:44:40:28:C6:94"

#Load Band settings
band = auth.MiBand3(MAC_ADDR, debug=True)
band.setSecurityLevel(level = "medium")

#to initilize connection
#band.initialize()

#If the band is already initialized authentification is enough
band.authenticate()
   
#print(heart_beat())
#print("heart rate :", band.get_heart_rate_one_time())
#print("Merry Christmas!!!") 

def heart_rate():
    BPM = band.get_heart_rate_one_time()
    for count in range(4):
        if BPM == 0:
            if count < 3:
                print("BPM not measured, BPM will be measured again")
                BPM = band.get_heart_rate_one_time()                
            else:
                print("BPM not measured")
        else:
            print("BPM is %s" %BPM)
            break
    return BPM
    
        

x = heart_rate()
print(x)