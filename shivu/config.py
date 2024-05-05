class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5937246417"
    sudo_users = "7011799629"
    GROUP_ID = -1002145420408
    TOKEN = "6707490163:7152462980:AAFIuHy0xlvPgjO-ZDGWNOGphOItAEtPL6A"
    mongo_url = "mongodb+srv://ravi:ravi12345@cluster0.hndinhj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://mallucampaign.in/images/img_1714881106.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Rulers_Bots_Support"
    UPDATE_CHAT = "DRIFTERSNETWORK"
    BOT_USERNAME = "waifuproxbot"
    CHARA_CHANNEL_ID = "-1002089288943"
    api_id = 23693234
    api_hash = "8e084a4919847164a4833587e2eb7e3b"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
