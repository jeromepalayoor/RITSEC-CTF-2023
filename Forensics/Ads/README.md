![image](https://user-images.githubusercontent.com/63996033/230438258-0accd907-b113-4cf9-b196-888ca35ce642.png)

[ads.pcapng](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Ads/ads.pcapng)

Hint: Our network engineering team was able to isolate some suspicious ICMP traffic coming through our routers. We're still not sure what to make of it, though.

Solution:
```
The description reads:
  We had to release a marketing intern because he failed security training. We monitored his activity for the last two weeks and captured this network traffic. 
  We're worried that he was exfiltrating data. Can you confirm?
  
This indicates that we are looking for some form of hidden traffic within the capture.
Looking through the capture, we can notice an ICMP packet that says "Mobile IP Advertisement". 
Futher along, we see another packet that says "Router Solicitation". 
This is another clue, because Solicitation is a synonym for Advertisement.
Diving into the packets, Mobile IP Advertisement are ICMP type 9. Router Solicitation are ICMP type 10. 
If then search for every packet that has ICMP type 9 or ICMP type 10, we get a large string of packets. 
Looking at all of these, we can start to formulate some ideas about where this is going.
By mapping, in order, every ICMP type 9 and ICMP type 10 packets to 0 and 1, respectfully, we get a binary string.
We then convert that to ascii, and we have our flag.
```

Solve: `tshark -r ads.pcapng -Y 'icmp.type == 10 || icmp.type == 9' | sed 's/Mobile.*/0/;s/Router.*/1/' | awk '{print $8}' | paste -sd '' | perl -lpe '$_=pack"B*", $_'`

![image](https://user-images.githubusercontent.com/63996033/230438458-5877e1ea-211e-401c-b08c-aa0bec5c340e.png)

Flag: `RS{g00gle_Add_s3rv1c3s}`
