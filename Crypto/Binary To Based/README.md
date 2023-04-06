![image](https://user-images.githubusercontent.com/63996033/230413505-81759b0a-9432-48f3-9688-27b9831fc067.png)

[Circuit.png](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Crypto/Binary%20To%20Based/Circuit.png)
[Circuit2.png](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Crypto/Binary%20To%20Based/Circuit2.png)
[Circuit3.png](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Crypto/Binary%20To%20Based/Circuit3.png)
[Circuit4.png](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Crypto/Binary%20To%20Based/Circuit4.png)

The Random String: `FIAAQF*ED PC-EDUPEZKESN8*3EZ2`

Hint 1: Circuit.png is not necessary to solve the challenge.

Hint 2: Understand that the waveform has inputs necessary for solve, binary numbers are read right to left so a0 is the furthest right.

Solution: Given sets of numbers you must convert them to binary then put them through the adder/subtractor. After getting all the solutions, multiply the numbers together to get 45 and use an base 45 decoder to get the flag

Flag: `RS{CircuitsareCool}`
