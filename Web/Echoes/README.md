![image](https://user-images.githubusercontent.com/63996033/231517757-e4a54adf-a295-4572-86ea-9cb47a36d2fb.png)

[link](https://echoes-web.challenges.ctf.ritsec.club/)

Going to the site:

![image](https://user-images.githubusercontent.com/63996033/231518431-31b3caec-a9b8-447a-be81-5a61e2eafd86.png)

Input anything just outputs itself 3 times:

![image](https://user-images.githubusercontent.com/63996033/231520533-6e8332bd-da40-4ca8-af89-55a16174164e.png)

Maybe we can try using `;` to close the echo command and execute shell commands using, `;<shell command>`. First try `ls` command to see files.

![image](https://user-images.githubusercontent.com/63996033/231520652-3888c40e-c083-4248-97ab-9ee8de6c4f88.png)

There we go! Just `cat` out the flag now.

![image](https://user-images.githubusercontent.com/63996033/231520680-4b17c346-bf5c-4920-86bb-21ff7889cebb.png)

Flag: `RS{R3S0UND1NG_SUCS3SS!}`
