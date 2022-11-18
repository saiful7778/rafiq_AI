import random
import json
import torch
from main_function import NeuralNetwork, NeuralNet, bag_of_words, tokenize
from essential_function import dirlocation

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open(f"{dirlocation()}\database\main_function\intents.json",'r') as json_data:
  intents = json.load(json_data)

FILE = f"{dirlocation()}\TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# =======================
Name = "Rafiq"

from main_function import Listen, Say, Say_in_arabic, NonInputExecution, InputExecution

global stop_this
stop_this = False

def Main():
  sentence = Listen()
  result = str(sentence)
  

  if sentence == "bye":
    exit()
  
  sentence = tokenize(sentence)
  X = bag_of_words(sentence, all_words)
  X = X.reshape(1,X.shape[0])
  X = torch.from_numpy(X).to(device)

  output = model(X)

  _ , predicted = torch.max(output,dim=1)

  tag = tags[predicted.item()]

  probs = torch.softmax(output, dim=1)
  prob = probs[0][predicted.item()]

  if prob.item() > 0.75:
    for intent in intents['intents']:
      if tag == intent["tag"]:
        reply = random.choice(intent["responses"])

        if "time" in reply:
          NonInputExecution(reply)

        elif "exit_loop" in reply:
          global stop_this
          stop_this = True
        
        elif "rafiq" in reply:
          NonInputExecution(reply)

        elif "open" in reply:
          InputExecution(reply, sentence)

        elif "close" in reply:
          InputExecution(reply, sentence)

        elif "date" in reply:
          NonInputExecution(reply)

        elif "wikipedia" in reply:
          InputExecution(reply, sentence)

        elif "ctrweb" in reply:
          InputExecution(reply, sentence)

        elif "google" in reply:
          InputExecution(reply, result)
          
        elif "health" in reply:
          NonInputExecution(reply)

        else:
          Say(reply)

while True:
  Main()
  if stop_this == True:
    break
  else:
    continue

