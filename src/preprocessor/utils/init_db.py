# Initialization of the database
import db_actions

if __name__ == "__main__":
    # Connect to the database
    db_actions.connect_to_db()

    # Check if Info Collection is empty
    if db_actions.Info.objects.count() == 0:
        print("Info Collection is empty, populating...")
        db_actions.save_info_from_json()
    print("Database initialized")
