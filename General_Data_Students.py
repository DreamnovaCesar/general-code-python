import pandas as pd
import random
from random import randint

# Function add a new student randomly
def New_Data(df, iter):

   Random_Name = ('Tom', 'Nick', 'Chris', 'Jack', 'Thompson')
   Random_Classroom = ('A', 'B', 'C', 'D', 'E')

   for i in range(iter):
    
      new_row = pd.DataFrame( {  'Name':random.choice(Random_Name),
                                 'Age':randint(16, 21),
                                 'Classroom':random.choice(Random_Classroom),
                                 'Height':randint(160, 190),
                                 'Math':randint(70, 100),
                                 'Chemistry':randint(70, 100),
                                 'Physics':randint(70, 100),
                                 'Literature':randint(70, 100)}, index = [i]  )

      df = pd.concat([df, new_row])

    
   return df

def main():
   
   
   # Create a new DataFrame
   df = pd.DataFrame()
    
   # Updated DataFrame with new data
   df = New_Data(df, 2000)

   # Print the output.
   print(df)

if __name__ == "__main__":
   main()