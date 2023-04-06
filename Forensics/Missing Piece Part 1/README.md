![image](https://user-images.githubusercontent.com/63996033/230440114-abcbc650-24db-46e3-9394-d3c684b5898e.png)

[https://drive.google.com/file/d/1vX1M8zlNtC8L2FTSwnaJmLW-36wTACeS/view?usp=sharing](https://drive.google.com/file/d/1vX1M8zlNtC8L2FTSwnaJmLW-36wTACeS/view?usp=sharing)

Hint: 18.04, 5.4.0-84-generic

Solution:
```
Volatility profile/symbol table creation challenge, actually getting volatility to parse the file is the hard part.
Technically this part can be solved with vol2 or vol3, but part 2 requires vol2 so the rest of this will  explain that method.
The memory dump is from an Ubuntu 18.04 system with kernel version 5.4.0-generic, this can be determined using the vol3 banner plugin. 
So a custom profile for linux-image-5.4.0-84-generic needs to get made so volatility can analyze the memory dump.
There are several online resources for this, this is what I used to make/test it: 
https://beguier.eu/nicolas/articles/security-tips-3-volatility-linux-profiles.html.
But there's a lot of methods to get the right profile.
Once the profile is working, running the linux_bash plugin shows the base64 encoded flag.
```

Flag: `RS{D1Y_L1NUX_$YM60L$}`
