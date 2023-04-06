![image](https://user-images.githubusercontent.com/63996033/230420489-cf6f9e15-8dab-4e4a-b1fd-7b5582a69731.png)

[auth.log](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Red%20Team%20Activity%201/auth.log)

Using grep to find all .sh file in the log reveals a suspicious file.

![image](https://user-images.githubusercontent.com/63996033/230421530-0e55d40b-7178-4a4d-87ec-ab73c0ea747a.png)

After hashing `_script2980.sh` with md5 => `5d8b854103d79677b911a1a316284128` we get our flag.

Flag: `RS{5d8b854103d79677b911a1a316284128}`
