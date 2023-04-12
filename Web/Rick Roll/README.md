![image](https://user-images.githubusercontent.com/63996033/231523040-e27c6cf4-60a3-419a-85fb-9ab455d365be.png)

[link](https://rickroll-web.challenges.ctf.ritsec.club/)

Visiting the site shows us a site about Rick Astley and the Rick Roll song. 1 part of the flag was found immediately in 2.css which was imported by the site:

`RS{/\/eveRG0nna_`

Similarly digging through the files that were requested by other files shows us the other parts of the flag.

```
1.html : TuRna30unD_
1.css  : G1v3y0uuP_
         |3tY0|_|d0vvn_
2.css  : RS{/\/eveRG0nna_
Don't.html:	D3s3RTy0u}
```
 Piecing it together gives the flag.
 
 Flag: `RS{/\/eveRG0nna_G1v3y0uuP_|3tY0|_|d0vvn_TuRna30unD_D3s3RTy0u}`
