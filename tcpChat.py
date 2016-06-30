import threading
import server
import client



def Main():
    friendIP = input("enter your friend's IP:")
    senderThread = threading.Thread(target=server.main())
    recieverThread = threading.Thread(target=client.main(), args=(friendIP))
    senderThread.start()
    recieverThread.start()

Main()









