![image](https://user-images.githubusercontent.com/63996033/230424836-9fed2237-3b8b-4e22-b2c4-0705decaa2f5.png)

[auth.log](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Forensics/Red%20Team%20Activity%203/auth.log)

Using grep to find crontabs gives us the full path.

![image](https://user-images.githubusercontent.com/63996033/230425175-494fffd5-b15c-4b80-a0d3-c6c8ece5fd9a.png)

Hashing `/var/spool/cron/crontabs/root` with md5 gives `c1da8fd57f17c95c731c38ee630f6aea`

Flag: `RS{c1da8fd57f17c95c731c38ee630f6aea}`
