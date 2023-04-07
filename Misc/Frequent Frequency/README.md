![image](https://user-images.githubusercontent.com/63996033/230642931-20352011-ddd5-480b-8ce8-12e42d841774.png)

Hint: Sample rate is 1 MSPS :)

[frequent_frequency.c32]()

Solution:
```
This is a signal that uses OOK modulation. 
Decode the signal and you will get 1s and 0s that output an ELF executable. 
It is just a binary that prints the flag. 
The competetor could also just run strings on the file to get the flag but this is intentional.

The Signal Parameters:
The scheme is quite simple really. 4000 Baud symbol rate, 1 MSPS sample rate, and a 100 KHz carrier frequency. 
If a symbol has an amplitude of 1 then it is a "1" bit, if the signal has an aplitude of 0 the bit is "0."

Solution
I have a GNU Radio flowgraph that will decode the file. 
There are many ways to demodulate this data but GRC is the recommended way.
```

Flag: `RS{THE_K3Y_1S_H3RE}`
