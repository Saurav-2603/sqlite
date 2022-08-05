# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

def DataUpdate(id, name, email, joinDate, salary):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (id, name, email, joinDate, salary)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

class ActionSubmit(Action):
        def name(self) -> Text:
            return "action_hello_world"
        async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            id=tracker.get_slot('id')
            name=tracker.get_slot('name')
            salary=tracker.get_slot('salary')
            email=tracker.get_slot('email')
            joinDate=tracker.get_slot('date')
            DataUpdate(id, name, email, joinDate, salary)
            dispatcher.utter_message("Thanks for the valuable information.")
            return()

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_sum_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            # def readSqliteTable():
                try:
                    sqliteConnection = sqlite3.connect('SQLite_Python.db')
                    cursor = sqliteConnection.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """select * from SqliteDb_developers where joining_date >= '2015-02-21'"""
                    cursor.execute(sqlite_select_query)
                    records = cursor.fetchmany()
                    for record in records:
                        print(record)
                        records = """The detail is as follows {}.""".format(record)
                        dispatcher.utter_message(records)
#"""working"""
                    # sql_select_query = """select * from SqliteDb_developers where id = 2"""
                    # cursor.execute(sql_select_query)#, (id,))
                    # records = cursor.fetchall()
                    # print("Printing ID ", id)
                  
                    # for row in records:
                    #     dispatcher.utter_message("Name = ", row[1])
                    #     dispatcher.utter_message("Email  = ", row[2])
                    #     dispatcher.utter_message("JoiningDate  = ", row[3])
                    #     dispatcher.utter_message("Salary  = ", row[4])
                    # cursor.close()

                    #     dispatcher.utter_message("Id: ", row[0])
                    #     dispatcher.utter_message("Name: ", row[1])
                    #     dispatcher.utter_message("Email: ", row[2])
                    #     dispatcher.utter_message("JoiningDate: ", row[3])
                    #     dispatcher.utter_message("Salary: ", row[4])
                    #     dispatcher.utter_message("\n")
                    cursor.close()

                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                print("The SQLite connection is closed")
                dispatcher.utter_message(text="Hello World!")

                return []
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             sqliteConnection = sqlite3.connect('SQLite_Python.db')
#             sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
#                                         id INTEGER PRIMARY KEY,
#                                         name TEXT NOT NULL,
#                                         email text NOT NULL UNIQUE,
#                                         joining_date datetime,
#                                         salary REAL NOT NULL);'''

#             cursor = sqliteConnection.cursor()
#             print("Successfully Connected to SQLite")
#             cursor.execute(sqlite_create_table_query)
#             sqliteConnection.commit()
#             print("SQLite table created")

#             cursor.close()

#         except sqlite3.Error as error:
#             print("Error while creating a sqlite table", error)
#         finally:
#             if sqliteConnection:
#                 sqliteConnection.close()
#                 print("sqlite connection is closed")
#                 dispatcher.utter_message(text="Hello World!")

#                 return []
###THIS IS MANUAL DB FILL THROUGH CHATBOT###
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             date=tracker.get_slot('date'),
#             email=tracker.get_slot('email'),
#             id=tracker.get_slot('id'),
#             name=tracker.get_slot('name'),
#             salary=tracker.get_slot('salary')
#             try:
#                 sqliteConnection = sqlite3.connect('SQLite_Python.db')
#                 cursor = sqliteConnection.cursor()
#                 print("Successfully Connected to SQLite")

#                 sqlite_insert_with_param = """INSERT INTO SqliteDb_developers1 (salary) VALUES (?)"""
#                 data_tuple = (salary)
#                 cursor.execute(sqlite_insert_with_param, data_tuple)
#                 sqliteConnection.commit()
#                 # sqlite_insert_query = """INSERT INTO SqliteDb_developers
#                                     # (name, email, joining_date, salary) 
#                                     # VALUES (name,email,date,salary)"""
#                 print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
#                 cursor.close()

#             except sqlite3.Error as error:
#                 print("Failed to insert data into sqlite table", error)
#             finally:
#                 if sqliteConnection:
#                     sqliteConnection.close()
#                     print("The SQLite connection is closed")
#             dispatcher.utter_message(text="Hello World!")

#             return []


###THIS IS MANUAL DB FILL###
# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")

#     sqlite_insert_query = """INSERT INTO SqliteDb_developers
#                           (id, name, email, joining_date, salary) 
#                            VALUES 
#                           (1,'James','james@pynative.com','2019-03-17',8000)"""

#     count = cursor.execute(sqlite_insert_query)
#     sqliteConnection.commit()
#     print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Failed to insert data into sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")
