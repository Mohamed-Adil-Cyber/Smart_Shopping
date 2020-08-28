# Data set of people and iteams they have bougth and the amount they bought 
#0 means either they havent bought it yet.
import mysql.connector as db

db = db.connect(
    host="remotemysql.com",
    user="VLwIyxlKeg",
    passwd="RPAo4fNBiy",
    database='VLwIyxlKeg'
)

myCursor = db.cursor()


myCursor.execute(f"""
        SELECT Product_Name FROM Products_Table
""")
x = myCursor.fetchall()



dataset={
			'Shopper1': {x[0]: 5, 
							x[1]: 5,
							x[2]: 0, 
							'Shampoo': 0, 
							'Hair Conditioner': 0,
							  'Ladder':0,
							},

			'Shopper2': {x[0]: 5, 
							x[1]: 5,
							x[2]: 4,
							 'Shampoo': 0,
							  'Hair Conditioner':0,
							  'Ladder':0,  
							 },

			'Shopper3': {x[0]: 0, 
								x[1]: 0,
								x[2]: 0,
								 'Shampoo': 5,
								 'Hair Conditioner':5,
							  'Ladder':0,
								 },



			'Shopper4': {x[0]: 0, 
							x[1]: 0,
							x[2]: 0, 
							'Shampoo': 4,
							'Hair Conditioner': 0,
							  'Ladder':0}}





def Recommend(item):

    myCursor.execute(f"""
                INSERT INTO Recommendation (Cart_ID, Recommend_Image, Recommend_Item, Origin_Item) VALUES (%s, %s, %s, %s)
                        """, ("1", "https://diegoinstudiocity.files.wordpress.com/2019/10/recom.jpg?w=400&h=282&crop=1", item, ""))

    db.commit()


