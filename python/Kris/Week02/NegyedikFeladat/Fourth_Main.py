# nekem megoldotta az import problémát az,
# hogy a .vscode/settings.json -ön belül
# "python.languageServer": "Jedi" -re változtattam a
# "python.languageServer": "Microsoft" helyett

from Fleet import Fleet
from Thing import Thing

fleet = Fleet()

get_milk = Thing("Get milk")
remove_obstacles = Thing("Remove the obstacles")
stand_up = Thing("Stand up")
stand_up.complete()
eat_lunch = Thing("Eat lunch")
eat_lunch.complete()

fleet.add(get_milk)
fleet.add(remove_obstacles)
fleet.add(stand_up)
fleet.add(eat_lunch)

# Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)