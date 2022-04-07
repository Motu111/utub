class Messages:

    START_MSG = (
        "Hello freind 😀 {}.\n\nMyself telegram to YouTube uploader bot 😎. I upload videosfrom telegram to YouTube 😯 "
        "next step /help if you have access .\n\nthis bot will not work until you got access from my boss Thank you."
    )

    HELP_MSG = [
        ".",
        "Hello boss.\n\nHii. Every video uploaded by you is processed by YT, "
        "if you upload copyright video then you can be blocked "
        "so be alert, and you will not be able to publish the video.\n\nRead all pages carefully.",
        "**Here i will tell how i work.**\n\n**Call 1:** __Authorise me to upload to your youtube channel "
        "It is so easy.__\n\n**Call 2:** __forward me any Telegram file of any size.__\n\n**Call 3:** __You have to reply "
        "__/upload __to the forwarded video file.You can also give me a title, its your "
        "choise.Title will follow the __`/upload`.__If no title means file name as title.__"
        "\n\n**Call 4:** __I will download it and upload it on YT.__\n\n**Call 5:** __I "
        "Will send you the link after uploading.__",
        "**Verifying the YT account **\n\nYoutube is not flower its a fire 🔥. So you are asked to verify "
        " after verifying your account you can upload videos longer than 15 minutes "
        "minutes. this is why it is very important, otherwise the video will be deleted"
        "or removed.\n[Verify your Youtube account here.](http://www.youtube.com/verify)\n\n__Now go to next page 🌟🌟 "
        "okk.__",
        "** authorisation.**\n\nI cant upload videos until you give me access.For that "
        "open the below link and copy the code amd send it to me and type `/authorise copied-code` and "
        "send it.\n\n**Last page!**\nAll done it was an long process "
        " meet u in uploading videos "
        "byy.",
    ]

    NOT_A_REPLY_MSG = "Please reply to some video file."

    NOT_A_MEDIA_MSG = "No media file found. " + NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media"

    DAILY_QOUTA_REACHED = "Looks like you are trying to upload more than 6 videos today! By default youtube only "
    "allows about 6 uploads daily, so this request might fail!!"

    PROCESSING = "Processing....."

    NOT_AUTHENTICATED_MSG = "You have not authenticated me to upload video to any account. see /help to authenticate"

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code"

    AUTH_SUCCESS_MSG = "Congrats, you have successfully authenticated me to upload to Youtube.\nHappy uploading!"

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}"

    AUTH_DATA_SAVE_SUCCESS = "Successfully saved the given auth data!"
