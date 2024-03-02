import pymysql

def create_connection():
    # Change these values based on your MySQL setup
    host = '172.17.0.2'
    user = 'root'
    password = 'root'
    database = 'KYC'

    # Create a connection
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    return connection

def create_table(connection):
    # Create 'students' table if not exists
    with connection.cursor() as cursor:
        cursor.execute('''                                                                                                                                                                                                    CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        ''')
        connection.commit()

def enter_student_name(connection):
    while True:
        name = input("Enter student name (or type 'quit' to exit): ")

        if name.lower() == 'quit':
            break

        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO students (name) VALUES (%s)', [name])
            connection.commit()

        print(f"Student '{name}' added to the database.")

def main():
    connection = create_connection()
    create_table(connection)

    while True:
        print("\nOptions:")
        print("1. Enter student name")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            enter_student_name(connection)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    connection.close()

if __name__ == "__main__":
    main()
