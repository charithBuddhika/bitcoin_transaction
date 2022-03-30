from bit import PrivateKeyTestnet

#user1
my_key = PrivateKeyTestnet('cT2gHVP6z7wtsGSArVBmmWq4MFEhSMr7ZdhKU7fHh8VRFPHJPE5d')
print(my_key.address)
balance = my_key.get_balance('btc')
print(balance)

outputs = [
    # user2
    ('mtXh676GL8mQFWTz2n1Gpcrv4DKm2VMneH', 0.0005, 'btc'),
    # user1 (change)
    ('mxXXcgUWymuGWJ3ekk9q3eLr639e7SRNfN', 0.0001, 'btc')
]

my_key.send(outputs)