![image](https://user-images.githubusercontent.com/63996033/230422507-b999fb34-d4db-4808-b6f8-4aef4c166462.png)

[auth.log](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Red%20Team%20Activity%202/auth.log)

Using grep to get all systemctl calls we find the bluetooth serive being enabled.

![image](https://user-images.githubusercontent.com/63996033/230423392-75d498cb-e7da-4f62-8117-0c83ed0676a8.png)

Hashing `bluetoothd.service` with md5 gives us `a9f8f8a0abe37193f5b136a0d9c3d869`

Flag: `RS{a9f8f8a0abe37193f5b136a0d9c3d869}`
