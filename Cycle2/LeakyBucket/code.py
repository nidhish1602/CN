op = int(input("Enter output rate: "))   #output rate 
bc = int(input("Bucket capacity: "))    #capacity 
n = int(input("Number of packets:"))

i = 0
while i < n:
    pc = int(input("\npacket size: ")) #packet size
    if ( pc < bc ):
        print("Bucket output successful")
        if( pc < op ):
            print("last " + str(pc) + " byte(s) were sent.")
            continue
        elif( pc > op ):
            a = abs(op - pc)
            print(str(op) + " bytes outputted.")
            print("Last " + str(a) + " byte(s) sent")
            continue
    else:
        print("Bucket overflow")
        break
    i+=1
