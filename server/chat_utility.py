# import pymongo
import datetime
from fastapi import FastAPI
# app = FastAPI()

url = "mongodb+srv://Cherlord1:Cherlord1@cluster0.2img3.mongodb.net/?retryWrites=true&w=majority"
# client = pymongo.MongoClient(url)
# db = client["Database"]

# acc_coll = db["Accounts"]
# msg_coll = db["Messages"]

# fields for accounts
username = "username"

# fields for msg
message = "message"
from_user_key = "from_user"
to_user_key = "to_user"
conversation_key = "conversation_key"
created_at = "created_at"

# for initial tests
# def initDummyMesages():
#     for msg in "1234":
#             str = "ab"
#             addMessage(msg, str[0], str[1])
#     for msg in "5678":
#             str = "ab"
#             addMessage(msg, str[1], str[0])
    
# def getAllMessages():
#     docs = msg_coll.find({})
#     for doc in docs: print(doc)

# def maybeForDemo():
#     msg_coll.delete_many({})
#     addMessage("Hi there!", "Eric", "Lily")
#     addMessage("Hi there!", "Eric", "Lily")
#     addMessage("Hi there!", "Eric", "Lily")
#     addMessage("Hi there!", "Eric", "Lily")
#     addMessage("Hi there!", "Eric", "Lily")
#     addMessage("Hi there!", "Eric", "Lily")
    
# def returnAllMessages():
#     docs = msg_coll.find({})
#     return docs

# # utility methods 
# # @app.post("/send_message")
# # def addMessage(msg, from_user, to_user):
# #     key = f"{from_user}{to_user}" if from_user < to_user else f"{to_user}{from_user}"
    
# #     doc = {
# #         message : msg,
# #         from_user_key : from_user,
# #         to_user_key : to_user,
# #         conversation_key : key,
# #         created_at : datetime.datetime.utcnow()
# #     }
    
# #     msg_coll.insert_one(doc)
    
# def getMessages(current_user):
#     pipeline = [
#         # messages involving current user
#         {
#             "$match" : {
#                 "$or" : [
#                     { from_user_key : current_user },
#                     { to_user_key : current_user }
#                 ]
#             }
#         },
#         # grouped by conservation key
#         {
#             "$group" : {
#                 "_id" : f'${conversation_key}'
#             }
#         },
#         # sort by most recent
#         {
#             "$sort" : {
#                 created_at : -1 
#             }
#         }
#     ]
    
#     docs = msg_coll.aggregate(
#         pipeline
#     )
    
#     print(list(docs))
    
#     # for doc in docs: 
#     #     for a in doc:
#     #         print(a)
#     print("jhio")
    
# # msg_coll.delete_many({})
# # msg_coll.insert_one({"msg":"hi there"})
# # initDummyMesages()
# # getAllMessages()
# # getMessages("a")