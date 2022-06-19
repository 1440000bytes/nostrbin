# nostrbin

### Requirements

[noscl](https://github.com/fiatjaf/noscl)  
python  
flask


### Usage

1. Run `noscl` and set a private key:
   ```
   noscl key-gen
   noscl setprivate <private key>
   ```
2. Add a relay using `noscl add relay wss://nostr-pub.wellorder.net` or try other [relays](https://nostr-registry.netlify.app/)
3. Run `nosclapi.py` and test it using postman

   ![image](https://user-images.githubusercontent.com/94559964/174482678-7196addb-7c61-4a2f-9e5f-8a77e7508734.png)
   
4. Run `app.py` and use the browser to submit text. It will return the `eventid`.

![image](https://user-images.githubusercontent.com/94559964/174483252-e7b19df2-7a67-4d2e-ac69-3ed8bc28a1ff.png)

![image](https://user-images.githubusercontent.com/94559964/174483284-4f0e1bfe-c6db-4c9c-9d4d-1c39f55d065a.png)

### Todo

- Add endpoint to check contents with eventid



