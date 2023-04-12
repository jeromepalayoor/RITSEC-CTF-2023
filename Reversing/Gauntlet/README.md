![image](https://user-images.githubusercontent.com/63996033/231539896-88b531cf-52ac-4d3d-8da9-d87ccb08d0a3.png)

[gauntlet.exe]()

Solution: 
```
Situational awareness with active malware sample debugging. Handling multiple concurrent issues at once.

patch the ret instruction in main to int 3
then let the program run
it will hang for abit at int 3
```

Flag: `RS{Quick_check_vector_this_exception_important_time_is_hash_WetPitttTld}`
