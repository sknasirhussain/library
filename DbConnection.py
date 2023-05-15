import serial
import mysql.connector
import time

# Set up serial communication with Arduino
ser = serial.Serial('com3', 9600)

print("Trying to connect to database...")
try: 
# Set up MySQL database connection
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "library"
        )
        mycursor = mydb.cursor()
        print("Database connected!")
except:
       print("Database not connected!")
       
# Clear the input buffer
ser.reset_input_buffer()

# Wait for Arduino to start
time.sleep(5)

while True:
    # Wait for Arduino to send tag data
    if ser.in_waiting > 0:
        # Read the tag data from Arduino
        data = ser.readline().decode().strip()
        print(data)
        

# Check if it's the student tag or the book tag
        if data.startswith("Student:"):
                tag_data = data.split(":")[1]

            # Search for the student in the database
                mycursor.execute("SELECT * FROM studentdetails WHERE StudentRFID = %s", (tag_data,))
                result = mycursor.fetchone()
                print(result)

            # If student is found, insert their details into the details_table
                if result:
                    student_details = result
                    print("Student details saved")
                    time.sleep(3)

                else:
                    print("Student not found")
                    time.sleep(5)

    # when the book tag has been scanned
    if data.startswith("Book:"):
        tag_data = data.split(":")[1]
            # Search for the book in the database
        mycursor.execute("SELECT * FROM books WHERE BookRFID = %s", (tag_data,))
        result = mycursor.fetchone()
        print(result)

            # If book is found, insert its details into the details_table
        if result:
            sql = "INSERT INTO issuedetails (StudentID, StudentName, StudentRFID, BookID, BookRFID, Bname, Author) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (student_details[0], student_details[1], student_details[2], result[0], result[1], result[2], result[3])
            mycursor.execute(sql, val)
            mydb.commit()
            print("Student and book details inserted")
            break

        else:
            print("Book not found")    
            break      
     