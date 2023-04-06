![image](https://user-images.githubusercontent.com/63996033/230427511-ef697cb6-df3e-4dfc-9cd0-23705160781c.png)

[auth.log](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/d016d1c7b1ebc394b7d3c06bd8f2ac7a682cdbf8/Forensics/Red%20Team%20Activity%204/auth.log)

After a bit of trial and error, there is a chmod priviledge elevation of this file which can be found using grep.

![image](https://user-images.githubusercontent.com/63996033/230427199-64f339de-a8f7-4d26-a650-bfa9aaf46370.png)

Hashing `/usr/bin/find` with md5 gives `7fd5884f493f4aaf96abee286ee04120`

Flag: `RS{7fd5884f493f4aaf96abee286ee04120}`
