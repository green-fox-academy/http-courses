from .fleet import Fleet
from .thing import Thing

fleet = Fleet()

# Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

get_milk = Thing('Get milk')
remove_obstacles = Thing('Remove obstacles')
stand_up = Thing('Stand up')
eat_lunch = Thing('Eat lunch')
stand_up.complete()
eat_lunch.complete()

fleet.add(get_milk)
fleet.add(remove_obstacles)
fleet.add(stand_up)
fleet.add(eat_lunch)

print(fleet)