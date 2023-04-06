![image](https://user-images.githubusercontent.com/63996033/230430036-c7a2e070-9c2a-4cbd-83e1-2e3b0cc2d140.png)

[weboflies.pcapng](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Web%20of%20Lies/weboflies.pcapng)

Opening up the pcapng file in wireshark shows us a lot of HTTP request.

![image](https://user-images.githubusercontent.com/63996033/230432707-6447af58-2ecb-433d-934f-28fb25e5fb81.png)

Looking at only the HTTP request:

![image](https://user-images.githubusercontent.com/63996033/230433150-43e30a9a-4db6-40f3-8aac-98b1ac6b2038.png)

It looks as though it alternates between /flag and /fl4g request. Filter it using: `http.request.method==GET`

![image](https://user-images.githubusercontent.com/63996033/230433490-cd573cf5-1c2a-4245-858f-b204a391d050.png)

It looks like it can be converted to 1s and 0s. 

![image](https://user-images.githubusercontent.com/63996033/230433810-49c75dfc-9f17-4499-bb7e-5f3cc381fc40.png)

Export it to csv

![image](https://user-images.githubusercontent.com/63996033/230433999-24ef080a-07e2-488f-a0d3-78089475406a.png)

Time for some regex to just get the a and 4.

![image](https://user-images.githubusercontent.com/63996033/230434284-717e37ed-2d94-4914-a8e0-2808c4c3c12d.png)

![image](https://user-images.githubusercontent.com/63996033/230434378-1e1b3e95-297e-41b2-bc3e-5a0a95150dda.png)

![image](https://user-images.githubusercontent.com/63996033/230434488-1154f6a5-6266-4eec-945b-50e8739cd320.png)

![image](https://user-images.githubusercontent.com/63996033/230434570-5e7b956c-595c-44e1-b098-7d2f71f541e7.png)

Ok now converting it to 1s and 0s. (might need to do it twice since we do not know which one is 1 and which ons is 0)

`101011011010110010000100101011011001101010011001100011011100110010001100100101111010101110010111110011001010111111001011100110001100110010000010`

This does not give us the flag so it must be the other way round.

 `010100100101001101111011010100100110010101100110011100100011001101110011011010000101010001101000001100110101000000110100011001110011001101111101`
 
 Decoding it gives the flag.
 
 ![image](https://user-images.githubusercontent.com/63996033/230435182-d07e0b12-e093-4d27-bab8-da72d4358fba.png)

Flag: `RS{Refr3shTh3P4g3}`
