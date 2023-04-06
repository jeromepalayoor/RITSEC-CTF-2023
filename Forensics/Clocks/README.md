![image](https://user-images.githubusercontent.com/63996033/230439205-24885263-f7e7-4bc3-9fe7-bcefe2a6d69e.png)

Hint: It's just turned five o'clock somewhere.

[clocks.pcapng](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Clocks/clocks.pcapng)

Solution:
```
Find the NTP protocol stream with a timestamp = Jan 1, 1970 05:00:00.000000000 UTC
You follow the stream and you get all the seconds values of the 4 timestamps:
 - Reference Timestamp: 00
 - Origin Timestamp: 01
 - Receive Timestamp: 01
 - Transmit Timestamp: 02
----------------------------
 - Reference Timestamp: 02
 - Origin Timestamp: 02
 - Receive Timestamp: 03
 - Transmit Timestamp: 03
etc etc
Find the logic behind the seconds values:
 - We know that the flag start with `RS{` and ends with `}`
 - We encode `RS{` in binary : 01010010 01010011 01111011
 - Now guess the Logic:
    - we start with 0 if the seconds next number is == to the actual seconds number is == to 0
Examble: 
|00|01|01|02|02|02|03|03| |03|04|04|05|05|05|06|07|
| 0| 1| 0| 1| 0| 0| 1| 0| | 0| 1| 0| 1| 0| 0| 1| 1|
      01010010 = R           01010011 = S
```

Solve: `tshark -r clocks.pcapng -Y 'ip.addr eq 129.21.1.111' -Tfields -e ntp.reftime -e ntp.org -e ntp.rec -e ntp.xmt | uniq | grep -oP 'Jan.*?UTC' | xargs -Iz date -d z +%s | awk '{ prev=cur; cur=$0; if (prev != "") print cur-prev; else print 0 }' | paste -sd '' | perl -lpe '$_=pack"B*", $_'`

![image](https://user-images.githubusercontent.com/63996033/230439869-215ac2df-b8f8-4fc4-a428-4aa197f8bbc7.png)

Flag: `RS{Tim3_k33per!}`
