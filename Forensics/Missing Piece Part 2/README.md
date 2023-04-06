![image](https://user-images.githubusercontent.com/63996033/230440519-829d0ce3-959d-4dca-ba2d-ce2e22052452.png)

[https://drive.google.com/file/d/1vX1M8zlNtC8L2FTSwnaJmLW-36wTACeS/view?usp=sharing](https://drive.google.com/file/d/1vX1M8zlNtC8L2FTSwnaJmLW-36wTACeS/view?usp=sharing)

Solution:
```
Looking into the memory dump more, running linux_pslist will show a process named "RS".
Running linux_psaux shows the filepath of the script as "/RS".
The linux_find_file plugin can be used to find the inode value of that file, 
which can then be used with the same plugin to extract the script which contains the base64 encoded flag.
```

Flag: `RS{PR0C355_HUN71NG_1N_M3M}`
