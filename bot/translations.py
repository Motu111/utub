class Messages: 

    START_MSG = (
        "Hi there {}.\n\nI'm telegram to YouTube video uploader bot. "
        "you can learn how to use me from my owner. click /help for next step.\n\nThank you."
    ) 

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. after upload youtube will process the video so be patience, "
        "if you upload copyrighted content may video get block keep your videos private "
        "have you got it.\n\nRead how i work ok dont skip.",
        "**Lets learn how I work.**\n\n**Step 1:** __You have to authorise to use me.see pages "
        "this in comming pages.__\n\n**Step 2:** __You have to forward me videos only.__\n\n**Step 3:** __reply with"
        "__/upload __to the forwarded video file. You can give me the file name otherwise "
        "__`/upload`.__If no title is given, filename will be used as title.__"
        "\n\n**Step 4:** __i will upload it to YouTube with high speed.__\n\n**Step 5:** __I "
        "send you the Youtube link after upload.__",
        "**You should have an YouTube channel okk **\n\n hmm lets go to the point"
        "Making of  yt channel .\n\n**Step 1:** __Sign in to YouTube ."
        "__\n\n**Step 2:** __hmmm, "
        "Make the YouTube channel.__\n\n**Step 3:** __may you have all this before and i am not telling "
        "Here.__\n\n**Step 4:** __Check the details and confirm to create your new channel.__",
        "**Verify your YouTube account**\n\nverify your account to upload videos longer than 15 mins"
        "your Youtube account. Once you've verified your account, you will be able to upload videos longer than 15 "
        "minutes. If you haven't verified your account every video uploaded which are longer than 15 minutes will be "
         "removed.\n[Verify your Youtube account here.](http://www.youtube.com/verify)\n\n__Remember to verify "
        "Ok.__",
        "**Now lets authorise.**\n\nclick on link and here's the "
        "Way `/authorise copied-code` and "
        "send it.\n\n**Fear not!**\nthanks"
        "now you got it. please subscribe my gaming youtube Channel "
        "i worked so hard at computer screen.",
    ] 

    NOT_A_REPLY_MSG = "Please reply to some video file." 

    NOT_A_MEDIA_MSG = "No media file found. " + NOT_A_REPLY_MSG 

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media" 

    DAILY_QOUTA_REACHED = "you can't upload more than 6 videos."
    "I know this one process will fail!!" 

    PROCESSING = "Processing....." 

    NOT_AUTHENTICATED_MSG = "first authenticate then upload. see /help to authenticate" 

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code" 

    AUTH_SUCCESS_MSG = "all done now give me the video.\nyou are looking happy!" 

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}" 

    AUTH_DATA_SAVE_SUCCESS = "Successfully saved the given auth data!"
