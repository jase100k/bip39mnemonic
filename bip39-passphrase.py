#!/usr/bin/env python3

## Test code for generating 


from mnemonic import Mnemonic 
import getpass

mnemo = Mnemonic("english")

#seed_words = "winter globe evidence sad ivory total fix cry replace crucial trust excess"
print("Please input seed words:")
seed_words = input()
if mnemo.check(seed_words) == True:
    print("Seed words check: OK")
else: 
    print("Seed words check: FAIL")
    print("Exiting: -1")
    exit(-1)
# Get passphrase and renter passphrase from user
passphrase = getpass.getpass(prompt="Please input passphrase: ")
passphrase2 = getpass.getpass(prompt="Passphrase again: ")

# Exit if passphrases don't match
if passphrase != passphrase2:
    print("Error: passphrase don't match")
    print("Exiting: -3")
    exit(-3)



# Convert mnemonic + passphrase to seed
seed = mnemo.to_seed(seed_words, passphrase)
xprv = mnemo.to_hd_master_key(seed)

# Display the XPRV
print("Xprv: " + xprv)


