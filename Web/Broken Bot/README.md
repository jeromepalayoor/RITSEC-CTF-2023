![image](https://user-images.githubusercontent.com/63996033/231527298-9044dd5d-73be-4a75-bc4d-624ec8e2e961.png)

[link](https://brokenbot-web.challenges.ctf.ritsec.club/)

Checking the site shows a login page:

![image](https://user-images.githubusercontent.com/63996033/231527476-025139aa-6b2c-4f84-b27a-9b617f76be1a.png)

We can try to deobfuscate this javascript code:

![image](https://user-images.githubusercontent.com/63996033/231527980-e53107fb-88ac-4d1e-bc6e-be1244864736.png)

There is a request to the telegram api with the name RIT_CTF_Telegram_Bot, which I searched in Telegram.

![image](https://user-images.githubusercontent.com/63996033/231529949-ccda9d71-2c0c-413e-9e78-a2d5cdef418c.png)

Flag: `Flag{Always_Check_For_Misconfigurations}`
