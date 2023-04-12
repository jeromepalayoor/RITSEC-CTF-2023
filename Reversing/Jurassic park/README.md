![image](https://user-images.githubusercontent.com/63996033/231539153-72afe685-9884-4b3d-8f65-9ec0d1b5b0dd.png)

[JurassicPark](https://github.com/jeromepalayoor/RITSEC-CTF-2023/blob/main/Reversing/Jurassic%20park/JurassicPark)

Solution:

```
You will likely see that there is no way to effect the running code inside of so
best to start looking at what you can clean about the code via various reversing methods.
You will find the following results when you run binwalk on ther executable:

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 64-bit LSB executable, AMD x86-64, version 1 (SYSV)
690719        0xA8A1F         Unix path: /dev/stderr/dev/stdout30517578125: frame.sp=ApatosaurusCarnotaurusDeinonychusDives_AkuruGOMEMLIMIT=GOTRACEBACKHadrosaurusIdeogra
696648        0xAA148         Unix path: /usr/lib/locale/TZ/14901161193847656257450580596923828125Canadian_AboriginalGC work not flushedIDS_Binary_OperatorKhitan_Small_S
697733        0xAA585         Unix path: /usr/share/zoneinfo/37252902984619140625Egyptian_HieroglyphsIDS_Trinary_OperatorMeroitic_HieroglyphsSIGALRM: alarm clockSIGTERM:
699372        0xAABEC         Unix path: /lib/time/zoneinfo.zip4656612873077392578125Inscriptional_ParthianNyiakeng_Puachue_HmongSIGSTKFLT: stack faultSIGTSTP: keyboard
701287        0xAB367         Unix path: /usr/share/lib/zoneinfo/116415321826934814453125582076609134674072265625bad defer entry in panicbypassed recovery failedcan't sc
721248        0xB0160         PNG image, 954 x 249, 8-bit/color RGBA, non-interlaced
721289        0xB0189         Zlib compressed data, compressed
832912        0xCB590         Unix path: /usr/lib/golang
894496        0xDA620         Unix path: /usr/lib/golang/src/internal/cpu/cpu.go
1232192       0x12CD40        Unix path: /sys/kernel/mm/transparent_hugepage/hpage_pmd_size
1480176       0x1695F0        Unix path: /usr/lib/golang/src/runtime/runtime-gdb.py

From this you can glean that this is golang, likewise you can also seen an emebeded png inside of the executable that you might be able to extract.
Doing some quick google searching you can find the following command is able to extract all pngs from a file:
binwalk -D 'png:png:convert %e %e' [input file]
Running this commands will ouput a png with the flag in it
```

Flag: `RS{G0_3MB3D_TH3_FLAG}`
