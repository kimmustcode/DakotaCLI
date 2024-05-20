from e621 import E621
import urllib
import os 

api = E621()

def downloadposts_fromtags(tags=[]):
    posts = api.posts.search(tags, limit=900, ignore_pagination=True)

    x= input(str(len(list(filter('None'.__ne__, posts)))) + " Posts. Download? (y/n): ")

    if x == 'y':
        for post in posts:
            print(str(post.id) + " was downloaded!")
            if post.file_obj.url != None:
                path = "Bay/" + str(post.id) + "." + str(post.file_obj.ext)
                urllib.request.urlretrieve(post.file_obj.url, path)
        input("All files are downloaded to my bay :3. Enter to continue.")

    return

def mod_start(dir_path):
    exit = False 
    if os.path.exists(dir_path + '/Bay/') == False:
        os.mkdir(dir_path + "/Bay/")
        
    while exit == False:
        os.system('cls')    

        # E6 Program Intro
        print (r"""
                 ___
             _.-|   |          |\__/,|   (`\
             {  |   |          |o o  |__ _) )
             "-.|___|        _.( T   )  `  /
              .--'-`-.     _((_ `^--' /_<  \
            .+|______|__.-||__)`-'(((/  (((/
        
        """)
        
        print("A E621 post downloader.\n--pool\n--search\n--(return)\n")
        inp = input("\n>")

        if inp == 'pool':
            pool_id = int(input("Enter Pool ID: "))
            downloadposts_frompool(pool_id)

        elif inp == 'search':
            tags = []
            x = 1
            while x != '0':
                x = input("Enter Tags (0 to end): ")
                if x != '0':
                    fit_x = str(x)
                    tags.append(fit_x)
            if tags == []:
                print("")
            else:
                downloadposts_fromtags(tags)

        elif inp == 'return':
            exit = True
    return

def downloadposts_frompool(pool_id=""):
    if pool_id != "":
        pool = api.pools.get(pool_id)

    posts = []
    poolname = ''

    for item in pool:
        if item[0] == 'post_ids':
            posts = item[1]   
        if item[0] == 'name':
            poolname = item[1]
    
    x= input(str(len(posts)) + " Posts. Download? (y/n): ")
    
    if x == 'y':
        os.mkdir("Bay/" + poolname)

        for ids in posts:
            temp = api.posts.get(ids)
            
            if temp.file_obj.url != None:
                path = "Bay/" + poolname + "/" + str(temp.id) + "." + str(temp.file_obj.ext)
                urllib.request.urlretrieve(temp.file_obj.url, path)
                print(str(temp.id) + " was downloaded!")
        input("All files are downloaded to my bay :3. Enter to continue.")
    return
