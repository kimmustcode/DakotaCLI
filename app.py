from modules import e621_grabber as e6
from modules import fileManage as fm
from modules import TFTools as tftt
from modules import e621game as e6g
from modules import spotifyDL as sdl
import os
import glob
import shutil

class Dakota:
    def __init__(self, path):
        self.dwnldMsg = "All files are downloaded to my vault :3. Enter to continue."
        self.path = path 
        self.intro_p()
        return 
   
    # Intros the bot
    def intro_p(self):
        exit = False
        while exit == False:
            os.system('cls')
            print(r"""

                ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░  
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
                ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓████████▓▒░ 
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
                ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
                     |\      _,,,---,,_
               ZZZzz /,`.-'`'    -.  ;-;;,_
                    |,4-  ) )-,_. ,\ (  `'-'
                    '---''(_/--'  `-'\_) 
                                    """)

            print("I'm your Little Cat Helper ^.^\nThese are my functionalities.")
            print("\n--(e621) downloader\n--(spotify) downloader\n--(tft) tools\n--e621 (game)\n--(open) bay\n--(clean) bay\n--(exit)")
            x = input("\n>")
            

        # E621 API Interface 
            if x == 'e621':
                e6.mod_start(self.path)    
        # Spotify Downloader
            elif x == 'spotify':
                sdl.mod_start()
        # Storage and File Management
            elif x == 'file':
                fm.temp()
        # Clean Vault
            elif x == 'clean':
                self.cleanVault_p(self.path)
        # TFT Tools Interface
            elif x == 'tft':
                tftt.mod_start()
        # e6 game 
            elif x == 'game':
                nt = input("How many sets?\n\n>")
                np = input("How many totals posts to pool? (Affects Start Up Time: Recommended 1000 - 2000)\n\n>")
                print('Loading Now... Give it a second.')
                e6g.mod_start(int(nt), int(np))
        # Open Bay    
            elif x == 'open':
                os.startfile(self.path + "/Bay")
        # Exit
            elif x == 'exit':
                exit = True


        return 

    def cleanVault_p(self, path):
        os.system('cls')
        inp = input("Are you sure? All the files in your Bay will be deleted? (y/n)\n>")

        if inp == 'y':
            files = glob.glob(path + '/Bay/*')
            for file in files: 
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(file_path + " was deleted!")
            
                    except OSError as e: 
                        print("Failed with:", e.strerror) 
                        print("Error code:", e.code) 
                    

        input("\nEnter to continue.")
        return 

   
if __name__ == "__main__":
    Dakota(str(os.path.join(os.path.dirname(__file__))))



