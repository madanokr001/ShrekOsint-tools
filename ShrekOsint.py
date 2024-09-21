import socket
import requests
import random
import whois

class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    PURPLE = '\033[35m'

def logo():
    print(TextColors.GREEN + """   
███████╗██╗  ██╗██████╗ ███████╗██╗  ██╗   ██████╗ ███████╗██╗███╗   ██╗████████╗ 
██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝   ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝ 
███████╗███████║██████╔╝█████╗  █████╔╝    ██║   ██║███████╗██║██╔██╗ ██║   ██║ 
╚════██║██╔══██║██╔══██╗██╔══╝  ██╔═██╗    ██║   ██║╚════██║██║██║╚██╗██║   ██║    
███████║██║  ██║██║  ██║███████╗██║  ██╗   ╚██████╔╝███████║██║██║ ╚████║   ██║    
          """ + TextColors.RESET)
logo()
def menu():
    print(TextColors.GREEN + "-------------------SHREK OSINT MENU-------------------" + TextColors.RESET)
    print(TextColors.YELLOW + "[1] IP TRACKER" + TextColors.RESET)
    print(TextColors.YELLOW + "[2] USER FINDER" + TextColors.RESET)
    print(TextColors.YELLOW + "[3] WHOIS" + TextColors.RESET)
    print(TextColors.YELLOW + "[4] Exit" + TextColors.RESET)
    print(TextColors.GREEN + "-------------------SHREK OSINT MENU--------------------- \n" + TextColors.RESET)

menu()

select = input(TextColors.CYAN + "ShrekOsint_root:~$ : " + TextColors.RESET)

if select == "1" or select == "IP TRACKER":
    def logo():
        print(TextColors.GREEN + """
██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║ 
╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        """ + TextColors.RESET)
    
    logo()

    def get_ip_info(ip_address):
        url = f"https://ipinfo.io/{ip_address}/json"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            ip_info = response.json()
            print(TextColors.YELLOW + "[*] IP Address:", ip_info.get("ip", "N/A") +TextColors.RESET)
            print(TextColors.YELLOW +"[*] City:", ip_info.get("city", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Region:", ip_info.get("region", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Country:", ip_info.get("country", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Location:", ip_info.get("loc", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Organization:", ip_info.get("org", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Postal Code:", ip_info.get("postal", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Timezone:", ip_info.get("timezone", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Hostname:", ip_info.get("hostname", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] ISP:", ip_info.get("isp", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Country Name:", ip_info.get("country_name", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Region Name:", ip_info.get("region_name", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] City Name:", ip_info.get("city_name", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Latitude:", ip_info.get("latitude", "N/A")+TextColors.RESET)
            print(TextColors.YELLOW +"[*] Longitude:", ip_info.get("longitude", "N/A") +TextColors.RESET)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    if __name__ == "__main__":
        ip = input("[+] ENTER THE IP ADDRESS : ")
        get_ip_info(ip)

if select == "2" or select == "USER FIND":
    def logo():
        print(TextColors.GREEN + """
██╗   ██╗███████╗███████╗██████╗     ███████╗██╗███╗   ██╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝██║████╗  ██║██╔══██╗
██║   ██║███████╗█████╗  ██████╔╝    █████╗  ██║██╔██╗ ██║██║  ██║
██║   ██║╚════██║██╔══╝  ██╔══██╗    ██╔══╝  ██║██║╚██╗██║██║  ██║
╚██████╔╝███████║███████╗██║  ██║    ██║     ██║██║ ╚████║██████╔╝
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝  social media finder
          """ + TextColors.RESET)

    logo()

    def url_user(username):
        return {
            'Twitter': f"https://twitter.com/{username}",
            'Instagram': f"https://www.instagram.com/{username}/",
            'Facebook': f"https://www.facebook.com/{username}",
            'LinkedIn': f"https://www.linkedin.com/in/{username}/",
            'GitHub': f"https://github.com/{username}",
            'TikTok': f"https://www.tiktok.com/@{username}",
            'Snapchat': f"https://www.snapchat.com/add/{username}",
            'Pinterest': f"https://www.pinterest.com/{username}/",
            'Reddit': f"https://www.reddit.com/user/{username}/",
            'YouTube': f"https://www.youtube.com/user/{username}",
            'Vimeo': f"https://vimeo.com/{username}",
            'Tumblr': f"https://{username}.tumblr.com/",
            'Flickr': f"https://www.flickr.com/photos/{username}/",
            'Quora': f"https://www.quora.com/profile/{username}",
            'Steam': f"https://steamcommunity.com/id/{username}/",
            'Discord': f"https://discord.com/users/{username}",
            'MySpace': f"https://myspace.com/{username}",
            'SoundCloud': f"https://soundcloud.com/{username}",
            'Last.fm': f"https://www.last.fm/user/{username}",
            'DeviantArt': f"https://www.deviantart.com/{username}",
            'Behance': f"https://www.behance.net/{username}",
            'Dribbble': f"https://dribbble.com/{username}",
            'Mixcloud': f"https://www.mixcloud.com/{username}/",
            'VK': f"https://vk.com/{username}",
            'Weibo': f"https://www.weibo.com/{username}",
            'Blogger': f"https://{username}.blogspot.com/",
            'LiveJournal': f"https://{username}.livejournal.com/",
            'Periscope': f"https://www.pscp.tv/{username}",
            'Clubhouse': f"https://www.joinclubhouse.com/@{username}",
            'Meetup': f"https://www.meetup.com/members/{username}/",
            'Yelp': f"https://www.yelp.com/user_details?userid={username}",
            'Vero': f"https://www.vero.co/{username}",
            'Letterboxd': f"https://letterboxd.com/{username}/",
            'OpenSea': f"https://opensea.io/{username}",
            'Couchsurfing': f"https://www.couchsurfing.com/people/{username}",
            'Xing': f"https://www.xing.com/profile/{username}",
            'Ravelry': f"https://www.ravelry.com/people/{username}",
            'Goodreads': f"https://www.goodreads.com/user/show/{username}",
            'Cricut': f"https://design.cricut.com/user/{username}",
            'Wattpad': f"https://www.wattpad.com/user/{username}",
            'Gab': f"https://gab.com/{username}",
            'Foursquare': f"https://foursquare.com/{username}",
            'Twitch': f"https://www.twitch.tv/{username}",
            'Dailymotion': f"https://www.dailymotion.com/{username}",
            'Bitbucket': f"https://bitbucket.org/{username}/",
            'ReverbNation': f"https://www.reverbnation.com/{username}",
            'Bandcamp': f"https://{username}.bandcamp.com/",
            '9GAG': f"https://9gag.com/u/{username}",
            'Typepad': f"https://{username}.typepad.com/",
            'FanFiction': f"https://www.fanfiction.net/u/{username}/",
            'Substack': f"https://{username}.substack.com/",
            'Anchor': f"https://anchor.fm/{username}",
            'Trello': f"https://trello.com/{username}",
            'Mix': f"https://mix.com/{username}",
            'Product Hunt': f"https://www.producthunt.com/@{username}",
            'Steemit': f"https://steemit.com/@{username}",
            'Etsy': f"https://www.etsy.com/shop/{username}",
            'Medium': f"https://medium.com/@{username}",
            'MyAnimeList': f"https://myanimelist.net/profile/{username}",
            'Food52': f"https://food52.com/profile/{username}",
            'Rumble': f"https://rumble.com/c/{username}",
            'Patreon': f"https://www.patreon.com/{username}",
            'Parler': f"https://parler.com/profile/{username}",
            'Tidal': f"https://tidal.com/user/{username}",
            'Mastodon': f"https://mastodon.social/@{username}",
            'Snapfish': f"https://www.snapfish.com/user/{username}",
            'Duolingo': f"https://www.duolingo.com/profile/{username}",
            'Scribophile': f"https://www.scribophile.com/profile/{username}",
            'Skillshare': f"https://www.skillshare.com/user/{username}",
            'Houseparty': f"https://www.houseparty.com/{username}",
            'WebMD': f"https://www.webmd.com/user/{username}",
            'Pandora': f"https://www.pandora.com/user/{username}",
            'Rappi': f"https://www.rappi.com/user/{username}",
            'Omegle': f"https://omegle.com/{username}",
            'Flixster': f"https://www.flixster.com/user/{username}",
            'Crunchyroll': f"https://www.crunchyroll.com/user/{username}",
            'Funimation': f"https://www.funimation.com/user/{username}",
            'TeeSpring': f"https://www.teespring.com/stores/{username}",
            'Wix': f"https://www.wix.com/{username}",
            'Badoo': f"https://badoo.com/{username}",
            'MeetMe': f"https://www.meetme.com/{username}",
            'DLive': f"https://dlive.tv/{username}",
            'AllTrails': f"https://www.alltrails.com/members/{username}",
            'Drip': f"https://drip.com/{username}",
            '7 Cups': f"https://www.7cups.com/{username}",
            'Twiddle': f"https://twiddle.com/{username}",
            'Yubo': f"https://yubo.live/{username}",
        }

    def check_user_profiles(username):
        profile_urls = url_user(username)
        for platform, url in profile_urls.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(TextColors.CYAN + f"[+] FOUND USER : {url}" + TextColors.RESET)
                else:
                    print(TextColors.RED + f"[-] NOT FOUND USER : {url}" + TextColors.RESET)
            except requests.exceptions.RequestException:
                print(TextColors.RED + f"[-] ERROR URL PATH : {url}" + TextColors.RESET)

    if __name__ == "__main__":
        username = input("[+] ENTER THE USERNAME : ")
        check_user_profiles(username)
        print("\n[+] USER FINDER COMPLETE !! Press Enter to exit...")
        input()

    # USER FINDER

if select == "3" or select == "WHOIS":
    def logo():
        print(TextColors.GREEN + """
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝
██║ █╗ ██║███████║██║   ██║██║███████╗
██║███╗██║██╔══██║██║   ██║██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
          """+ TextColors.RESET)
    
    logo()

    def whois_lookup(domain: str):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.iana.org", 43))
        s.send(f"{domain}\r\n".encode())
        response = s.recv(4096).decode()
        s.close()
        return response

    domain = input("[+] ENTER THE URL : ")
    result = whois_lookup(domain)
    print(result)


