'''
Checkpoint 1 - heart_rate.py
Abi Priebe
4/22/21
'''

'''
When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at 
least 20 minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per 
minute. Your heart simply will not beat faster than this maximum (220 - age). When exercising to strengthen your 
heart, you should keep your heart rate between 65% and 85% of your heart's maximum.
'''

age = int(input("Please enter your age: "))

max = 220 - age
low = max * 0.65
high = max * 0.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {low} and {high} beats per minute.")
