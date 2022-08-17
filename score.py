
import urlopen
import sys
import re
import time


## Read the scores from the web link and display it
## in a window

class ServerTalk():
    __url__ = "http://www.bcci.com/Matches/M0033_48/M0033_48_mini.html"

    def talk(self):
        try:
            score = "Not Available"
            fp =  urlopen(self.__url__)
            data = fp.read()
            strip_data = self.strip_ml_tags(data)
            clean_score = re.sub(r"\s\n", "" ,strip_data )

        except Exception as inst:
            print (inst.args)
            print ("Unexpected error:",sys.exc_info()[0])
            return "Not available" 
                
        return clean_score  


    def strip_ml_tags(self,in_text):
     
      # convert in_text to a mutable object (e.g. list)
      s_list = list(in_text)
      i,j = 0,0
    
      while i < len(s_list):
          # iterate until a left-angle bracket is found
          if s_list[i] == '<':
              while s_list[i] != '>':
                  # pop everything from the the left-angle bracket until the right-angle bracket
                  s_list.pop(i)
                
              # pops the right-angle bracket, too
              s_list.pop(i)
          else:
              i=i+1
            
      # convert the list back into text
      join_char=''
      return join_char.join(s_list)


class ScoreCard():
      
    def __init__(self):
        print ("in init of ScoreCard ") 
 

    def getWindow(self):
        ## Get a window to show the score
        return
    
    def getScores(self):
        ## Get the score and display it
        talker =ServerTalk() 
        data = talker.talk()
    
        
        return data
        
    def updateScores(self):
        ## Redisplay the scores in the window
        return 



def main():
    s = ScoreCard()
    

    while (True):
        data = s.getScores()
        print (data)
        print ("sleeping for some time") 

        time.sleep(20)
        # Update the UI
        #updateScores() 


if __name__ == '__main__':
    main()