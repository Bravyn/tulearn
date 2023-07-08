import pandas as pd

describe_data = ["Indeed, Mastermind. But we must tread carefully, \
                for even the smallest clue can lead us astray. Shall we shed light upon the \
                dataset's essence with summary statistics?",
                """
               Indeed, Mastermind. Each thread we unravel brings us closer to the heart of the mystery. 
               The meticulous organization of these details speaks volumes about the mind behind these crimes. 
               Let us continue to connect the dots and expose the secrets hidden within the shadows of our city.
            """]

import random

def generate_dataset():
   """Generates a sample 200 row dataset with the given columns."""
   dataset = []

   from datetime import date, timedelta

   # Generate a random date within a specific range
   start_date = date(2022, 1, 1)
   end_date = date(2023, 7, 8)

   time_delta = end_date - start_date
   random_days = random.randint(0, time_delta.days)
   random_date = start_date + timedelta(days=random_days)


   
   for _ in range(200):
      date_ = random_date.isoformat()
      location = random.choice(["Home", "Work", "Street", "Park", "Store"])
      crime_type = random.choice(["Robbery", "Assault", "Burglary", "Fraud", "Murder"])
      suspects = random.randint(0, 5)
      witnesses = random.randint(0, 5)
      dataset.append([date_, location, crime_type, suspects, witnesses])
   return dataset

columns = ['date_', 'location', 'crime_type', 'suspects', 'witnesses']
dataset = generate_dataset()
dataset_frame = pd.DataFrame(dataset, columns= columns)


