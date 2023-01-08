"""
Database Initialization Upon Startup of the Docker Container
"""
import db_actions
import logs_and_alerts as la

if __name__ == "__main__":
    log_directory = "preprocessor_utils_logs/init_db" # Directory for the logs
    try:
        # Connect to the database
        db_actions.connect_to_db()

        ### LOG AND ALERT ###
        message = "Successfully connected to the database"
        # Log the successful database connection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful database connection
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to connect to the database"
        # Log the failed database connection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed database connection
        la.Alerts().error_alert(message)
        ######################

        # Exit the program
        exit()

    # Check if Info Collection is empty
    if db_actions.Info.objects.count() == 0:
        try:
            # Populate the Info Collection
            print("Info Collection is empty, populating...")
            db_actions.save_info_from_json()

            ### LOG AND ALERT ###
            message = "Successfully populated the Info Collection"
            # Log the successful population of the Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful population of the Info Collection
            la.Alerts().success_alert(message)
            ######################
        except:
            ### LOG AND ALERT ###
            message = "Failed to populate the Info Collection"
            # Log the failed population of the Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed population of the Info Collection
            la.Alerts().error_alert(message)
            ######################

            # Exit the program
            exit()

    ### LOG AND ALERT ###
    message = "Successfully initialized the database"
    # Log the successful database initialization in the success_log.txt file
    la.Logs().success_log(message, log_directory)
    # Alert the successful database initialization
    la.Alerts().success_alert(message)
    ######################

    # Close the connection to the database
    db_actions.disconnect_from_db()
