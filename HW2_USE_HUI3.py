import HW2 as eq

#print perfect health score
print("Score for 'perfect' health: [1,1,1,1,1,1,1,1]")
print(eq.scoreHUI3(vision=1, hearing=1, speech=1, ambulation=1, dexterity=1, emotion=1, cognition=1, pain=1))

#print health score with a variety of values
print("Score for potential patient: [4,2,1,2,1,2,3,1]")
print(eq.scoreHUI3(vision=4, hearing=2, speech=1, ambulation=2, dexterity=1, emotion=2, cognition=3, pain=1))

