clients  = [
    (1, "111", "a@x.com"), 
    (2, "111", "b@x.com"),
    (3, "222", "c@x.com"),
    (4, "333", "c@x.com"), 
    (5, "444", "d@x.com")
]

phones = {}
emails = {}

for id, number, email in clients:
    phones.setdefault(number, set()).add(id)
    emails.setdefault(email, set()).add(id)

duplicates = []
for o in (phones, emails):
    for ids in o.values():
        if len(ids) > 1:
            duplicates.append(ids)
print(duplicates)

duplicate_ids  = set()
for n in duplicates:
    duplicate_ids |= n

# unique_clients = [client for client in clients if client[0] not in duplicate_ids]

unique_clients = []
for client in clients:
    if client[0] not in duplicate_ids:
        unique_clients.append(client)

print(duplicate_ids)
print(unique_clients)