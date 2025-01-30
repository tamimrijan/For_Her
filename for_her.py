import time
import sys

def type_out(text, delay=0.09):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_shared_heart():
    shared_heart = """
          ******         ******
        **********     **********
      *************   *************
     *************** ***************
    *********************************
    *********************************
     *******************************
      *****************************
       ***************************
        *************************
          *********************
            *****************
              *************
                *********
                  *****
                   ***
                    *
    """
    type_out(shared_heart, delay=0.02)

if __name__ == "__main__":
    try:
        with open("blue_lyrics_for_her.txt", "r", encoding="utf-8") as file:
            for line in file:
                type_out(line.strip())
                time.sleep(1.1)
                
                if "Know you're all that I want this life" in line or "will always bring me to you" in line:
                    type_shared_heart()
    except FileNotFoundError:
        print("Lyrics file not found! Make sure 'blue_lyrics_for_her.txt' exists.")