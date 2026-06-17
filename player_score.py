# Match Score using Tuple

players = (
    (1, "Virat", 98),
    (2, "Rohit", 100),
    (3, "Vaibhav", 99),
    (4, "Mahi", 101)
)

# 1. Print Max Score and Player Name
max_player = players[0]

for player in players:
    if player[2] > max_player[2]:
        max_player = player

print("Max Score Player:")
print("ID :", max_player[0])
print("Name :", max_player[1])
print("Score :", max_player[2])


# 2. Total Score
total_score = 0

for player in players:
    total_score += player[2]

print("\nTotal Score :", total_score)


# 3. Top 3 Players
top_3_players = sorted(players, key=lambda x: x[2], reverse=True)

print("\nTop 3 Players:")

for player in top_3_players[:3]:
    print(player)