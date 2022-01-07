# import speech_recognition as sr
#
# class ChatBot():
#
#     def __init__(self, name):
#         print("---Starting up", name, "----")
#         self.name = name
#
#     def speech_to_text(self):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as mic:
#             print("Listening... ")
#             audio = recognizer.listen(mic)
#             self.text = "Error"
#
