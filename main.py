my_mood = input("Please write your mood: ")
a_good_mood = "happy"
a_bad_mood = "sad"

if my_mood == a_good_mood: # (if True that good mood)
    print("Only if good mood")
    print("It is great to see you happy!")
elif my_mood == a_bad_mood: # (if True that bad mood)
    print("Only if bad mood")
    print("Hope you feel better.")
else: # (if not True any of above)
    print("Only if unknown mood")
    print("Sorry, I don't recognize this mood you're in.")

print("Regardless of the conditional")
print("At the end")
