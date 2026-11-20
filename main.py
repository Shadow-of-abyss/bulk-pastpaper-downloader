import os
import time
import requests


# sub = int(input("enter the subject code :"))
# years = int(input("how many years of pastpaper do you want to download : "))




def downloader(years,sub):
    stuff = ["qp", "in","ms"]
    year_from = 25
    sessions = ["s","w","m"]
    # type = input(f"the subject {sub}. is it extended subject or normal (y/N): ")
    # if type == "y":
    #     practical = input("paper 6? (y/N) : ")
    #     if practical == "y":
    #         variants = ["22","21","23","41","42","43","61","62","63"]
    #     else:
    #         variants = ["22","21","23","41","42","43"]
    # else:
    variants = ["11","12","13","21","22","23"]
    
    
    for i in range(years):
        year_start = year_from - i 

        for s in sessions:
            

            for v in variants:
            
                    
                if s=="s":
                    path = f"{sub}_pastpapers/20{year_start}/May_June/{v}"
                
                elif s=="w":
                    path = f"{sub}_pastpapers/20{year_start}/Oct_nov/{v}"
                elif s=="m":
                    path = f"{sub}_pastpapers/20{year_start}/Feb_march/{v}"
                else:
                    print("error")

                os.makedirs(path, exist_ok=True)
                for st in stuff:


                    paper_code = f"{sub}_{s}{year_start}_{st}_{v}.pdf"

                    print("downloading "+ paper_code)
            

                    url = f"https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{paper_code}"


                    retry_delay = 5

                    while True:
                        try:
                            response = requests.get(url, timeout=90)

                            if response.status_code == 404:
                                print(f"[NOT FOUND] {paper_code}")
                                break

                            response.raise_for_status()
                            with open((path + f"/{paper_code}"), "wb") as file:
                                file.write(response.content)
                            
                                print(f"Downloaded and saved as {path}")
                            break  # Request successful, exit retry loop

                        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                            print(f"[Internet slow/disconnected. Retrying in {retry_delay}s...")
                            time.sleep(retry_delay)
                            retry_delay = min(retry_delay * 2, 60)

                        except requests.exceptions.HTTPError as e:
                            print(f"[HTTP ERROR] {e}")
                            break



                





subject = ["0990","0510","0511","0991"]
for i in subject:

    downloader(15,i)