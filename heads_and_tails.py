import random 
import time



if __name__ == "__main__":
    heads_and_tails = ["heads","tails"]
    while True:
        try:
            print(random.choice(heads_and_tails))
            time.sleep(5)
        except KeyboardInterrupt:
            print("quitted")
            break
        

    
 
