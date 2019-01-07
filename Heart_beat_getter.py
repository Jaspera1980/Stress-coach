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

#Function to measure heart rate
#Tries to measure heart rate 3x times
def heart_rate():
    BPM = band.get_heart_rate_one_time()
    for count in range(4):
        if BPM == 0:
            if count < 3:
                print("Hartslag niet gemeten, we proberen het nog een keer")
                BPM = band.get_heart_rate_one_time()                
            else:
                print("Hartslag niet gemeten")
        else:
            print("Hartslag is %s" %BPM)
            break
    return BPM