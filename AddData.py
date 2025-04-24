from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Supabase client created successfully.")

student1 = {
    "id": 766329,
    "name": "Richie Dix",
    "major": "Computer Science",
    "starting_year": 2022,
    "total_attendance": 15,
    "standing": "Good",
    "year": 2026,
    "last_attended": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

student2 = {
    "id": 110384,
    "name": "Kevin Ma Boy",
    "major": "Art",
    "starting_year": 2020,
    "total_attendance": 23,
    "standing": "G",
    "year": 2024,
    "last_attended": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

student3 = {
    "id": 451327,
    "name": "Julian Kim",
    "major": "Computer Science",
    "starting_year": 2022,
    "total_attendance": 21,
    "standing": "A",
    "year": 2026,
    "last_attended": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# response = supabase.table("sensor_data").insert(student1).execute()
# response = supabase.table("sensor_data").insert(student2).execute()
# response = supabase.table("sensor_data").insert(student3).execute()


# print("Response from Supabase:", response)
