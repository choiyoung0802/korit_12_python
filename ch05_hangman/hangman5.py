import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = """
  ,---,                                                 ____                          
,--.' |                                               ,'  , `.                        
|  |  :                      ,---,                 ,-+-,.' _ |                 ,---,  
:  :  :                  ,-+-. /  |  ,----._,.  ,-+-. ;   , ||             ,-+-. /  | 
:  |  |,--.  ,--.--.    ,--.'|'   | /   /  ' / ,--.'|'   |  || ,--.--.    ,--.'|'   | 
|  :  '   | /       \  |   |  ,"' ||   :     ||   |  ,', |  |,/       \  |   |  ,"' | 
|  |   /' :.--.  .-. | |   | /  | ||   | .\  .|   | /  | |--'.--.  .-. | |   | /  | | 
'  :  | | | \__\/: . . |   | |  | |.   ; ';  ||   : |  | ,    \__\/: . . |   | |  | | 
|  |  ' | : ," .--.; | |   | |  |/ '   .   . ||   : |  |/     ," .--.; | |   | |  |/  
|  :  :_:,'/  /  ,.  | |   | |--'   `---`-'| ||   | |`-'     /  /  ,.  | |   | |--'   
|  | ,'   ;  :   .'   \|   |/       .'__/\_: ||   ;/        ;  :   .'   \|   |/       
`--''     |  ,     .-./'---'        |   :    :'---'         |  ,     .-./'---'        
           `--`---'                  \   \  /                `--`---'                 
                                      `--`-'                                          
"""
# 행맨 게임용 단어 리스트 (총 400개)
word_list = [
    # Animals (동물)
    "dog", "cat", "lion", "tiger", "elephant", "giraffe", "rabbit", "squirrel", "panda", "bear",
    "wolf", "fox", "hippo", "rhino", "zebra", "deer", "camel", "kangaroo", "monkey", "gorilla",
    "chimpanzee", "sloth", "otter", "seahorse", "seal", "whale", "shark", "dolphin", "turtle", "crocodile",
    "snake", "lizard", "frog", "toad", "penguin", "ostrich", "eagle", "owl", "sparrow", "pigeon",
    # Fruits & Vegetables (과일 및 채소)
    "apple", "banana", "grape", "strawberry", "watermelon", "melon", "peach", "plum", "apricot", "persimmon",
    "tangerine", "orange", "lemon", "lime", "mango", "pineapple", "kiwi", "blueberry", "cherry", "pomegranate",
    "fig", "date", "chestnut", "walnut", "peanut", "almond", "coconut", "avocado", "papaya", "lychee",
    "pear", "quince", "citron", "raspberry", "berry", "cabbage", "radish", "onion", "garlic", "potato",
    "sweetpotato", "carrot", "cucumber", "pumpkin", "eggplant", "lettuce", "spinach", "broccoli", "tomato", "corn",
    # Furniture & Household (가구 및 가전)
    "bed", "desk", "chair", "sofa", "table", "closet", "drawer", "bookshelf", "mirror", "hanger",
    "bench", "stool", "couch", "cushion", "carpet", "curtain", "lamp", "clock", "frame", "shelf",
    "refrigerator", "washer", "dryer", "airconditioner", "vacuum", "television", "computer", "laptop", "monitor", "keyboard",
    "mouse", "printer", "speaker", "tablet", "camera", "microwave", "oven", "airfryer", "toaster", "blender",
    # Kitchen & Items (주방 및 소품)
    "pot", "pan", "knife", "fork", "spoon", "plate", "bowl", "cup", "glass", "bottle",
    "kettle", "tray", "apron", "towel", "soap", "shampoo", "toothbrush", "toothpaste", "comb", "razor",
    "umbrella", "wallet", "watch", "glasses", "ring", "necklace", "bracelet", "earrings", "handkerchief", "mask",
    # Clothing (의류)
    "tshirt", "pants", "jeans", "skirt", "dress", "shirt", "sweater", "cardigan", "jacket", "coat",
    "padding", "shorts", "socks", "stockings", "hat", "gloves", "scarf", "shoes", "boots", "sneakers",
    # School & Office (학교 및 사무)
    "pencil", "pen", "eraser", "sharpener", "ruler", "scissors", "glue", "tape", "notebook", "paper",
    "folder", "calculator", "chalk", "blackboard", "backpack", "stapler", "clip", "stamp", "ink", "diary",
    # Transportation (교통)
    "car", "bus", "taxi", "train", "subway", "airplane", "ship", "bicycle", "motorcycle", "scooter",
    "truck", "helicopter", "spaceship", "stroller", "ambulance", "fireengine", "policecar", "boat", "rocket", "van",
    # Nature & Space (자연 및 우주)
    "sky", "cloud", "sun", "moon", "star", "rain", "snow", "wind", "thunder", "rainbow",
    "mountain", "ocean", "river", "lake", "forest", "tree", "flower", "grass", "soil", "stone",
    "island", "desert", "valley", "cave", "beach", "cliff", "earth", "mars", "jupiter", "saturn",
    # Jobs (직업)
    "teacher", "student", "doctor", "nurse", "chef", "police", "firefighter", "pilot", "lawyer", "artist",
    "singer", "dancer", "actor", "writer", "scientist", "farmer", "soldier", "engineer", "dentist", "baker",
    # Sports & Hobbies (스포츠 및 취미)
    "soccer", "basketball", "baseball", "volleyball", "swimming", "tennis", "golf", "hiking", "yoga", "running",
    "music", "painting", "movie", "reading", "travel", "cooking", "photo", "game", "dance", "fishing",
    # Places (장소)
    "school", "office", "hospital", "bank", "mart", "store", "pharmacy", "library", "park", "theater",
    "cafe", "restaurant", "gym", "hotel", "museum", "airport", "station", "bakery", "church", "zoo",
    # Feelings & Adjectives (감정 및 형용사)
    "happy", "sad", "angry", "excited", "brave", "nervous", "calm", "gloomy", "proud", "lonely",
    "kind", "honest", "lazy", "smart", "modest", "diligent", "gentle", "strong", "weak", "fast",
    "slow", "heavy", "light", "small", "large", "bright", "dark", "sweet", "salty", "bitter",
    "hot", "cold", "warm", "cool", "pretty", "ugly", "clean", "dirty", "easy", "hard",
    # Abstract & Others (기타)
    "time", "date", "today", "tomorrow", "yesterday", "morning", "afternoon", "evening", "night", "dawn",
    "dream", "hope", "peace", "love", "friend", "family", "neighbor", "success", "effort", "goal",
    "justice", "freedom", "health", "energy", "power", "money", "price", "market", "trade", "tax",
    "sound", "smell", "taste", "color", "shape", "size", "weight", "number", "point", "zero",
    "spring", "summer", "autumn", "winter", "north", "south", "east", "west", "center", "edge",
    "create", "improve", "reduce", "expand", "pause", "start", "finish", "change", "move", "stay"
]
chosen_word = random.choice(word_list)
print(logo)
display = []
for _ in range(len(chosen_word)):
    display.append("_")
lives = 6
end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input("입력하세요 >>> ")
    for _ in range(len(chosen_word)):
        if guess == chosen_word[_]:
            display[_] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} 단어는 없음. 남은 기회:{lives}")
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print("컷")
            print(f"정답은 {chosen_word} 입니다.")
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("정답입니다.")
print("게임 종료")