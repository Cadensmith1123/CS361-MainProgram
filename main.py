import random


workouts = [] #store generated workouts

# Sample workouts
sampleWorkouts = [
    "10 push-ups, 15 squats, 20 sit-ups",
    "5 pull-ups, 10 lunges per leg, 30-second plank",
    "20 burpees, 15 mountain climbers, 10 tricep dips",
    "15 jumping jacks, 20 bicycle crunches, 10 push-ups",
    "10 minutes running, 20 squats, 10 push-ups",
    "5 rounds of 10 kettlebell swings, 15 sit-ups, 20 squats",
    "3 sets of 10 bicep curls, 15 crunches, 20 lunges",
]

# Sample motivational quotes
motivationalQuotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "The only bad workout is the one that didn’t happen.",
    "Don’t limit your challenges, challenge your limits.",
    "Wake up with determination, go to bed with satisfaction.",
    "You don’t have to be extreme, just consistent.",
    "It’s not about having time, it’s about making time.",
    "Exercise not only changes your body, it changes your mind, your attitude, and your mood."
]

def generateWorkout():
    
    workout = random.choice(sampleWorkouts) #select random workout and add it to workout list
    workouts.append(workout)
    return workout

def repeatWorkout():
    # repeat the previous workout
    
    if workouts:
        print(f"\nRepeating Last Workout: {workouts[-1]}")
    
    else:
        print("\nNo workouts generated yet. Please generate a workout first.")

def displayWorkouts():
    # display previous
    if workouts:
        print("\nPreviously Generated Workouts:")
        
        for i, workout in enumerate(workouts, start=1):
            print(f"{i}. {workout}")
    
    else:
        print("\nNo workouts generated yet.")

def deleteWorkout():
    
    if not workouts:
        print("\nNo workouts available to delete.")
        return

    displayWorkouts() #display previous workout list so user can see what to delete
    
    try:
        choice = int(input("\nEnter the number of the workout to delete, or 0 to cancel: "))
        
        if choice == 0:
            print("Deletion canceled.") #cancel the deletion process
        
        elif 1 <= choice <= len(workouts):
            workout_to_delete = workouts[choice - 1]
            confirm = input(f"Are you sure you want to delete this workout? '{workout_to_delete}' (y/n): ").strip().lower() #confirm user choice
            
            if confirm == 'y': #
                removedWorkout = workouts.pop(choice - 1)
                print(f"Deleted workout: {removedWorkout}") #display the deleted workout
            
            else:
                print("Workout not deleted.") 
        
        else:
            print("Invalid choice. Please select a valid workout number.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def showQuote():
    # randomly display a motivational quote
    quote = random.choice(motivationalQuotes)
    print(f"\nMotivational Quote: {quote}")

def main():
    
    while True:
        # user prompt
        print("\nSelect an option:")
        print("1 - Generate a random workout")
        print("2 - Repeat the previous workout")
        print("3 - Display all previous workouts")
        print("4 - Display previous workouts and delete one")
        print("5 - Receive a motivational quote")
        print("6 - Exit")

        # grab user input
        choice = input("Enter your choice: ")

        if choice == '1':
            workout = generateWorkout()
            print(f"\nGenerated Workout: {workout}")
        
        elif choice == '2':
            repeatWorkout()
        
        elif choice == '3':
            displayWorkouts()
        
        elif choice == '4':
            deleteWorkout()
        
        elif choice == '5':
            showQuote()
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
