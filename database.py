import mysql.connector

def convert_data(file_name):
	with open(file_name, 'rb') as file:
		binary_data = file.read()
	return binary_data


try:
	connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        database = "xplatform" 
)
	cursor = connection.cursor()

	create_table = """CREATE TABLE demo(id INT PRIMARY KEY,\
	name VARCHAR (255) NOT NULL, profile_pic BLOB NOT NULL, \
	imp_files BLOB NOT NULL) """

	cursor.execute(create_table)
	print("Table created Successfully")

	query = """ INSERT INTO demo(id, name, profile_pic, imp_files)\
	VALUES (%s,%s,%s,%s)"""

	student_id = "1"
	student_name = "Shubham"
	first_profile_picture = convert_data("D:\GFG\images\shubham.png")
	first_text_file = convert_data('D:\GFG\details1.txt')

	result = cursor.execute(
		query, (student_id, student_name, first_profile_picture, first_text_file))
	connection.commit()
	print("Successfully Inserted Values")

except mysql.connector.Error as error:
	print(format(error))

finally:

	if connection.is_connected():
	
		cursor.close()
		connection.close()
		print("MySQL connection is closed")