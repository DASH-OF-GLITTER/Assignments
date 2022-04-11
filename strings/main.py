# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Create variable for every player that scored
player_scored_1 = "Ruud Gullit"
player_scored_2 = "Marco van Basten"

# Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when, according to the format
scorers = player_scored_1 + " " + str(goal_0) + ", " + player_scored_2 + " " + str(goal_1)
print(scorers)

# Use f-strings or the plus operator to create a single string with information about who scored when in the format:
report = f"{player_scored_1} scored in the {str(goal_0)}nd minute\n{player_scored_2} scored in the {str(goal_1)}th minute"
print(report)

# Part 2
player = "Frank Rijkaard"
first_name = (player[0:player.find(' ')])
print(first_name)
last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)
name_short = (player[0:1] + '.'+ player[player.find(' '):])
print(name_short)
chant = (first_name + '! ') * (len(first_name) -1) + (first_name + '!')
print(chant)

good_chant = (chant[len(chant)-1:] !=' ')
print(good_chant)

