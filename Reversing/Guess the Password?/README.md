![image](https://user-images.githubusercontent.com/63996033/231537600-88af8008-d876-484c-8e28-36a0b3f40467.png)

[encoding.py]() [server.py]() [supersecret.json]()

We cannot bruteforce the numbers as there is rate limiting. So the json file has a key and a secret; key is a hash and secret is... corrupted. We'll need to run our password against the server later to get the real flag
Taking a quick peek at encoding.py, it looks like check_input() hashes user_input and checks if it's equal to the key. flag_from_pwd() takes a key, xor's it against secret and returns it. 
There's no way to xor the flag without knowing the password. Luckily since we have the source code, we can get rid of that pesky rate limiting, and since the password is a 8 digit long integer brute forcing it should be easy.

```py
from encoding import Encoder


def main():
    encoder = Encoder("supersecret.json")

    # We know the password is 8 digits, so lets generate all possible combinations
    possible_answers = []
    for i in range(100000000):
        possible_answer = str(i)
        possible_answer = "0"*(8-len(possible_answer)) + possible_answer

        possible_answers.append(possible_answer)

    print("Generated possible passwords...\nStarting checks...")

    # now possible_answers is a set that has "00000000", "00000001", ..., "99999999"
    # we can now try brute forcing the flag

    for possible_answer in possible_answers:
        if encoder.check_input(possible_answer):
            print(f"The password is probably: {possible_answer}")
            flag = encoder.flag_from_pwd(possible_answer)
            print(f"That means the flag is something like <RS{ {flag} }>")
            break

    print("Done with checks!")

    # The user could also feed the secret to the server, and it should spit out the flag




if __name__ == "__main__":
    main()
    
>>> 54744973
```

Use that number to get the flag.

Flag: `RS{'PyCr@ckd'}`
