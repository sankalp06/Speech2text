import os
import speech_recognition as sr
from pydub import AudioSegment
import json


def conv_mp3_to_wav(input_file,wav_file): 
    sound = AudioSegment.from_mp3(input_file)
    sound.export(wav_file, format="wav")

def jaccard_similarity(x,y):
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  similarity = intersection_cardinality/float(union_cardinality)*100
  return similarity


def determine_grade(scores):
    if scores >= 90 and scores <= 100:
        return 10
    elif scores >= 80 and scores <= 89:
        return 8
    elif scores >= 70 and scores <= 79:
        return 6
    elif scores >= 60 and scores <= 69:
        return 4
    elif scores >= 50 and scores <= 59:
        return 2
    else:
        return 1
    

    
def speech2text(filepath,transcript,student_name):
    r = sr.Recognizer()   
    with sr.AudioFile(filepath) as source:   
        audio_data = r.record(source)    
        text = r.recognize_google(audio_data, language = 'en-IN')
        print(text)
        print("")
        transcript = open(transcript).read()
        similarity = jaccard_similarity(text.lower(), transcript.lower())
        #score = fuzz.ratio(text.lower(), transcript.lower())
        print(f"similarity: {similarity:.2f}")
        score = determine_grade(similarity)
        print("Score:",score)
        data = {'student_name':student_name,'similarity':similarity, 'Score':score}
        overall = json.dumps(data)
        with open("student_name.json", "w") as file_object:
            json.dump(overall, file_object)
        print(overall)

    return similarity,score,overall