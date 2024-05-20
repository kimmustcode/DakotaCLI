from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
from e621 import E621
import random
from tkinter import messagebox as mb 
import time

api = E621()



# Takes url and returns ImageTK object
class dURLImage:
    def __init__(self, url):
        t = time.time()
        with urllib.request.urlopen(url) as u:
            raw_Data = u.read()
        
        image = Image.open(io.BytesIO(raw_Data))
        
        width = 1920 / 2
        height = 1920 / 2
        image.thumbnail((int(width), int(height)))
        self.image = ImageTk.PhotoImage(image)
        print(time.time() - t)
    
    def get(self):
        return self.image
    

class e621App:
    def __init__(self, nt, np):
        self.numTurns = nt
        self.turn = 0
        self.posts = api.posts.search(["male", "-f", "rating:explicit", "-scat", "-young", "-gore", "-shota", "-smegma", "-urine", "-feral", "-vagina"], limit=np, ignore_pagination=True)
        self.used = []
        self.avoided = [] 
        self.votes = []
        self.vtags = []
        self.post1 = None
        self.post2 = None

        self.root = Tk()

        # Set window settings 
        self.root.wm_title("e621 game")
        self.root.geometry("1920x1080")
        self.root.configure(bg='black')

        # Get images of first 2 posts
        self.first = dURLImage(self.randoImage()).get()
        self.second = dURLImage(self.randoImage()).get()

        # Create labels to host images
        self.label1 = Label(self.root, image=self.first)
        self.label2 = Label(self.root, image=self.second)
        self.label1.grid(column=0,row=0)
        self.label2.grid(column=10,row=0)

        # Turn counter label
        self.labelTurns = Label(self.root, text=str(self.turn + 1))
        self.labelTurns.grid(column=5,row=35)
        
        # Vote Buttons
        self.button1 = Button(self.root, text = 'Vote', command=self.button1).grid(column=10,row=40)
        self.button2 = Button(self.root, text = 'Vote', command=self.button2).grid(column=0,row=40)
        self.button1 = Button(self.root, text = 'Neither', command=self.neither).grid(column=5,row=40)

        self.root.mainloop()
        self.total()


    # Totals, Sorts, and Displays Tags
    def total(self):
        bTags = ["5_fingers", 'anthro', 'fingers', 'abstract_background', 'ambiguous_gender', 'clothing', 'fur', 'male_focus', 'male', 'genitals', 'penis', 'balls']
        totalTags = [] 
        nums = []
        avTags = [] 
        avnum = []

        # Totals
        for tags in self.vtags:
            for tag in tags:
                if tag not in totalTags:
                    totalTags.append(tag)
                    nums.append(1)
                else: 
                    nums[totalTags.index(tag)] += 1

        for tags in self.avoided:
            for tag in tags: 
                if tag in avTags:
                    avnum[avTags.index(tag)] += 1 
                elif tag not in totalTags and tag not in avTags:
                    avTags.append(tag)
                    avnum.append(1)                    

        # Sorts 
        totalTags, nums = self.pllArr(totalTags, nums)
        avTags, avnum = self.pllArr(avTags, avnum)
        
        # Displays
        self.endDialogue(totalTags, avTags)

    # Gets random post from search
    def randoImage(self):
        deny = ['webm', 'gif', 'mp4'] 
        rand = random.randint(0, len(self.posts) - 1)

        # If the post is already used or if the extension is invalid, regen post number
        while rand in self.used or self.posts[rand].file_obj.ext in deny:
            rand = random.randint(0, len(self.posts) - 1)
        
        self.used.append(rand)
        
        if self.post2 == None: 
            self.post2 = self.posts[rand]
        else: 
            self.post1 = self.posts[rand]


        return self.posts[rand].file_obj.url

    # Sort Parallel arrays 
    def pllArr(self, arr1, arr2):
        cnt = 1
        while cnt > 0:
            cnt = 0
            for i in range(len(arr2) - 1):
                if arr2[i] < arr2[i + 1]:
                    temp = arr2[i]
                    arr2[i] = arr2[i + 1]
                    arr2[i + 1] = temp
                    temp2 = arr1[i]
                    arr1[i] = arr1[i + 1]
                    arr1[i + 1] = temp2
                    cnt += 1

        return arr1, arr2 

    # Update labels
    def update(self):
        self.first = dURLImage(self.randoImage()).get()
        self.second = dURLImage(self.randoImage()).get()
        
        self.labelTurns.config(text=str(self.turn + 1))
        self.label1.config(image=self.first)
        self.label2.config(image=self.second)
        return 

    # When first button is pressed
    def button1(self):
        self.votes.append(self.first)
        if self.post1 != None:
            self.vtags.append(self.post1.tags.general)
            self.avoided.append(self.post2.tags.general)

        self.turn += 1 
        self.post1 = None
        self.post2 = None

        if self.turn < self.numTurns:   
            self.update()
        else:
            self.root.quit()
    
    # Displays results in a window 
    def endDialogue(self, tags1, tags2):
        bTags = ["5_fingers", 'anthro', 'fingers', 'abstract_background', 'ambiguous_gender', 'clothing', 'fur', 'male_focus', 'male', 'genitals', 'penis', 'balls', 'solo', 'simple_background']
        temp = []
        cnt = 0
        for tag in tags1:
            if tag not in bTags and cnt < 10:
                temp.append(tag)
                cnt += 1
            elif cnt == 10: 
                break 
        
        results = 'Favorite Tags:'

        for tag in temp: 
            results += ("\n" + tag)

        tags = tags2[:10]
        results += "\n\nAvoided Tags: "
        for tag in tags: 
            results += ("\n" + tag)

            
        mb.showinfo('Results', results)

 
        
        return 
        
    # When second button is pressed
    def button2(self):
        self.votes.append(self.second)
        if self.post2 != None:
            self.vtags.append(self.post2.tags.general)
            self.avoided.append(self.post1.tags.general)

        self.turn += 1 
        self.post1 = None
        self.post2 = None
        
        if self.turn < self.numTurns:   
            self.update()
        else:
            self.root.quit()

    # User likes neither post
    def neither(self):
        self.avoided.append(self.post1.tags.general)
        self.avoided.append(self.post2.tags.general)    
        self.post1 = None
        self.post2 = None
        
        self.turn += 1

        if self.turn < self.numTurns:   
            self.update()
        else:
            self.root.quit()

def mod_start(np, nt):
    e621App(np, nt)
