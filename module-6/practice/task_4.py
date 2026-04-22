network = {
    "me": {"Alice", "Bob"}, 
    "Alice": {"me", "Charlie", "Bob"}, 
    "Bob": {"me", "David", "Eva"},
    "Charlie": {"Alice"},
    "David": {"Alice", "Bob"}, 
    "Eva": {"Bob"}
}
user = "me"
my_friends = network[user]
print(my_friends)


friends_of_friends = set()
for friend in my_friends:
    if friend in network:
        friends_of_friends.update(network[friend])

new_friends = friends_of_friends - my_friends - {user}

print(new_friends)