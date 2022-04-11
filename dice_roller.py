import random
import time
def rolling():
    dice_list =  ["1","2","3","4","5","6"]
    print(f"the answer is ==> {random.choice(dice_list)}")

if __name__ =="__main__":

    while True:
        try:
            rolling()
            time.sleep(5)
        except KeyboardInterrupt:
          print("quitted")
          break
