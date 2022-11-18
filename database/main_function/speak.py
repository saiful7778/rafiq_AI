import pyttsx3

def Say(Text):
  engine = pyttsx3.init("sapi5")
  voice = engine.getProperty('voices')
  engine.setProperty('voice', voice[0].id)
  volume = engine.getProperty('volume')
  engine.setProperty('volume',0.8)
  engine.setProperty('rate', 190)
  print("    ")
  print(f"Rafiq A.I.: {Text}")
  engine.say(text=Text)
  engine.runAndWait()

def Say_in_arabic(Text, speed):
  engine = pyttsx3.init("sapi5")
  voice = engine.getProperty('voices')
  engine.setProperty('voice', voice[2].id)
  volume = engine.getProperty('volume')
  engine.setProperty('volume',1.0)
  engine.setProperty('rate', speed)
  print("    ")
  print(f"Rafiq A.I.: {Text}")
  engine.say(text=Text)
  engine.runAndWait()
