import os, random, string, requests, colorama, keyboard, json, time; from colorama import Fore, Style
colorama.init();os.system("cls")
def main():
    i=1
    print(" ");print(Fore.LIGHTGREEN_EX+"             > discord nitro generator and checker <");print(Fore.RED + "                 > press 'ctrl+shift+q' to quit <\n")
    while keyboard.is_pressed('ctrl+shift+q') == False:
        n=''.join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{n}?with_application=false&with_subscription_plan=true")
        i+=1
        if r.status_code==200:
            print(Fore.GREEN+f" [!] Gift Code {n} available");f=open('working_gift_codes.txt', 'w', encoding="utf-8");f.write(f"https://discord.gift/{n} \n");f.close()
        elif r.status_code==429:
            data = json.loads(r.text)
            print(Fore.RED+"\n [x] Rate limit (waiting "+str(data["retry_after"])+"ms)")
            time.sleep(data["retry_after"])
        else:
            print(Fore.RED+f"[x] Gift Code {n} unavailabe. {i} tries", end="\r")
    print(" ");print(Fore.LIGHTGREEN_EX+"\n                           > finished < ")

if __name__ == "__main__":
    main()