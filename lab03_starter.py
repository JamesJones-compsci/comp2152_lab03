# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Dice options dynamically created
diceOptions = list(range(1, 7))
print("Dice Options:", diceOptions)

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("\nAvailable Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Get combat strength for hero
combatStrength = input("\nEnter your combat strength (Number between 1-6): ")
while not (combatStrength.isnumeric() and 1 <= int(combatStrength) <= 6):
    print("Invalid input. Please enter a number between 1 and 6.")
    combatStrength = input("Enter your combat strength (Number between 1-6): ")
combatStrength = int(combatStrength)

# Get combat strength for monster
mCombatStrength = input("\nEnter monster's combat strength (Number between 1-6): ")
while not (mCombatStrength.isnumeric() and 1 <= int(mCombatStrength) <= 6):
    print("Invalid input. Please enter a number between 1 and 6.")
    mCombatStrength = input("Enter monster's combat strength (Number between 1-6): ")
mCombatStrength = int(mCombatStrength)

# Roll dice for health points
input("\nRoll the dice for your health points (Press Enter)")
healthPoints = random.choice(diceOptions)
print("You rolled", healthPoints, "health points")

input("Roll the dice for the monster's health points (Press Enter)")
mHealthPoints = random.choice(diceOptions)
print("Monster rolled", mHealthPoints, "health points")

# Roll the dice for finding a healing potion
input("\nRoll the dice to see if you find a healing potion (Press Enter)")
healingPotion = random.choice([0, 1])  # 0 = no potion, 1 = potion
print("Did you find a healing potion?:", bool(healingPotion))

# Roll the dice for weapon selection
weaponRoll = random.choice(range(len(weapons)))  # Randomly select a weapon index
combatStrength += weaponRoll  # Add weapon roll to hero's combat strength
print("\nYour weapon is:", weapons[weaponRoll])

# Weapon quality feedback
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if weapons[weaponRoll] != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Analyze the roll
input("\nAnalyze the roll (Press Enter)")
print("--- You are matched in strength:", combatStrength == mCombatStrength)
print("--- You have a strong player:", (combatStrength + healthPoints) >= 15)
print("--- Remember to take a healing potion!:", healingPotion == 1 and healthPoints <= 6)
print("--- Phew, you have a healing potion:",
      not (healthPoints < mCombatStrength) and healingPotion == 1)
print("--- Things are getting dangerous:", healingPotion == 0 or healthPoints == 1)
print("--- Is it possible to roll 0 on the dice?:", 0 in diceOptions)

# Expanded health check logic
if healthPoints >= 5:
    print("\n--- Your health is ok.")
elif healingPotion == 1:
    healthPoints = max(diceOptions)  # Set health to full
    healingPotion = 0  # Consume the potion
    print("--- Using your healing potion... Your Health Points are now full at", healthPoints)
else:
    print("--- Your health is low at", healthPoints, "and you have no healing potions!")

# Battle sequence
print("\nYou meet the monster. FIGHT!!")
input("You strike first (Press Enter)")

print(f"Your attack ({combatStrength}) ---> Monster's health ({mHealthPoints})")
if combatStrength >= mHealthPoints:
    print("You've killed the monster!")
else:
    mHealthPoints -= combatStrength
    print(f"You reduced the monster's health to: {mHealthPoints}")
    print("The monster strikes back!")
    print(f"Monster's attack ({mCombatStrength}) ---> Your health ({healthPoints})")
    if mCombatStrength >= healthPoints:
        print("You're dead!")
    else:
        healthPoints -= mCombatStrength
        print(f"The monster reduced your health to: {healthPoints}")
