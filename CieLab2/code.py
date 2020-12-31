def start():
    op = 42      #42kbps
    cap = 400    #400kb
    n = [60, 300, 600]

    i=0
    while i<3:
        print("\nPacket size is "+str(n[i]))
        if (n[i]<cap):
            if(n[i]<op):
                print("\t"+n[i]+" bytes were outputted")

            elif(n[i]>op):
                while n[i]>op:
                    print("\t"+str(op)+" bytes were outputted")
                    n[i]-=op
                print("\t"+"Last "+str(n[i])+" bytes sent")

        else:
            print("\t"+"Bucket overflow")
            break
        i+=1

start()
