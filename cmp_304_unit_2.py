# importing libraries
import pandas as pd

# initialising variables
tsvFile = 'dnd_chars_all.tsv'
csvTable = pd.read_table(tsvFile, sep = '\t')

# Convert file to csv file
csvTable.to_csv('dnd_chars_all.csv', index = False)

# Output to show that it worked
print('Table converted Successfully!')

# Remove unneccessary Data
csvTable.drop('ip', inplace = True, axis = 1)
csvTable.drop('finger', inplace = True, axis = 1)
csvTable.drop('name', inplace = True, axis = 1)

# Output to show that it worked
print('Columns Dropped')

# removing duplicates from the dataset
csvTable.drop_duplicates(subset=['alias'], inplace = True)

# sorting characters based on current level
csvTable.sort_values('level', axis = 0, ascending = True, inplace = True, na_position='first')
print('Csv File ordered by level!')

# extracting array into variable based on main class
artificer = csvTable[csvTable['justClass'] == 'Artificer']
barbarian = csvTable[csvTable['justClass'] == 'Barbarian']
bard = csvTable[csvTable['justClass'] == 'Bard']
cleric = csvTable[csvTable['justClass'] == 'Cleric']
druid = csvTable[csvTable['justClass'] == 'Druid']
fighter = csvTable[csvTable['justClass'] == 'Fighter']
monk = csvTable[csvTable['justClass'] == 'Monk']
paladin = csvTable[csvTable['justClass'] == 'Paladin']
ranger = csvTable[csvTable['justClass'] == 'Ranger']
rogue = csvTable[csvTable['justClass'] == 'Rogue']
sorcerer = csvTable[csvTable['justClass'] == 'Sorcerer']
warlock = csvTable[csvTable['justClass'] == 'Warlock']
wizard = csvTable[csvTable['justClass'] == 'Wizard']


# exporting data to seperate csv files
artificer.to_csv('Artificers.csv', index = False)
barbarian.to_csv('Barbarians.csv', index = False)
bard.to_csv('Bards.csv', index = False)
cleric.to_csv('Clerics.csv', index = False)
druid.to_csv('Druids.csv', index = False)
fighter.to_csv('Fighters.csv', index = False)
monk.to_csv('Monks.csv', index = False)
paladin.to_csv('Paladins.csv', index = False)
ranger.to_csv('Rangers.csv', index = False)
rogue.to_csv('Rogues.csv', index = False)
sorcerer.to_csv('Sorcerers.csv', index = False)
warlock.to_csv('Warlocks.csv', index = False)
wizard.to_csv('Wizards.csv', index = False)

print('Classes sorted into csv Files!')