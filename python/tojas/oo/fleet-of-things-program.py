from fleet import Fleet
from thing import Thing

fleet = Fleet()

# Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

fleet.add(Thing('Get milk'))
fleet.add(Thing('Remove the obstacles'))
thing2 = Thing('Stand up')
thing2.complete()
fleet.add(thing2)
thing3 = Thing('Eat lunch')
thing3.complete()
fleet.add(thing3)

print(fleet)