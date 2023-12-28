import psycopg2

def cursor():
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        database="DataBase_Name",
        user="DataBase_Username",
        password="password",
        host="host_name",
        port="port_number"
    )

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Define the features you want to retrieve
    features_to_select =["\"AT\"", "\"RH\"", "\"Rain_Hourly\"", "\"Pressure\"", "\"WD_10M\"", "\"WS_10M_Hrly\""]


    # Initialize variables for each field
    AT_data, RH_data, Rain_Hourly_data, Pressure_data, WD_10M_data, WS_10M_Hrly_data = ([] for _ in range(6))

    for feature in features_to_select:
        # Construct the SQL query for the specific feature
        query = f"SELECT members_member.{feature} FROM members_member"

        # Execute the query to retrieve data
        cursor.execute(query)

        # Fetch all the rows
        data = cursor.fetchall()

        # Assign values to the respective variables
        if feature == "\"AT\"":
            AT_data = [row[0] for row in data]
        elif feature == "\"RH\"":
            RH_data = [row[0] for row in data]
        elif feature == "\"Rain_Hourly\"":
            Rain_Hourly_data = [row[0] for row in data]
        elif feature == "\"Pressure\"":
            Pressure_data = [row[0] for row in data]
        elif feature == "\"WD_10M\"":
            WD_10M_data = [row[0] for row in data]
        elif feature == "\"WS_10M_Hrly\"":
            WS_10M_Hrly_data = [row[0] for row in data]

        # Further processing or storage logic can be added here

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Return the data
    return AT_data, RH_data, Rain_Hourly_data, Pressure_data, WD_10M_data, WS_10M_Hrly_data

