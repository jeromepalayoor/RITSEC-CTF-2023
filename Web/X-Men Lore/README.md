![image](https://user-images.githubusercontent.com/63996033/231525812-e81f9c3e-4273-48d6-b196-9d4a3bb2a2e0.png)

Hint 1: The flag is in it's own file, it shouldn't be too hard to find. Once you're in, try to read the flags

Hint 2: The flag file does not have a file extension

[link](https://xmen-lore-web.challenges.ctf.ritsec.club/)

Opening the site shows us different X Men that we can choose from:

![image](https://user-images.githubusercontent.com/66698256/229508636-0437331b-805d-46ac-b46d-b7139dc5b235.png)

Checking the code:

![image](https://user-images.githubusercontent.com/66698256/229509551-f960f9b0-0f07-479e-9bf2-e525fe59b9e1.png)

Base 64 decoding it:

https://user-images.githubusercontent.com/66698256/229514057-e00e2b98-a18f-4999-83dd-e888751a1536.png

We have an XXE(XML External Entity) in here.

Using XXE, we can make it read the flag in its server:

![](https://user-images.githubusercontent.com/66698256/229520336-bb798ba5-0809-4b6e-8962-a4a0f2238f04.png)

Flag: `RS{XM3N_L0R3?_M0R3_L1K3_XM3N_3XT3RN4L_3NT1TY!}`
