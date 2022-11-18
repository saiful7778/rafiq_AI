import speech_recognition as sr
import time


def Listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    start_time = time.time()
    print("Listening....")
    r.pause_threshold = 1
    audio = r.listen(source)
  
  
  try:
    print("Recognizing...")
    query = r.recognize_google(audio,language="en-in")
    print(f"You said : {query.lower()}")


  except:
    return ""

  query = str(query)
  end_time = time.time()
  print(str((end_time-start_time)*1000)+" millisecond")
  return query.lower()
  
