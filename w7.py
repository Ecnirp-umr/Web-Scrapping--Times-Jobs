#lxml library must be install
#praser library must be install

from bs4 import BeautifulSoup # module
import requests


unfimilar_skills = input(" Enter unfimilar_skills : ")
print("Flittering.....")



def find_jobs():
    
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?earchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0").text
                                         
                                                # Load  the webpage content
                                                # .text,print help in print html text
                                                # if we won't use .text,then output"Response 222"
                                                #Put your url in a single and straight line
                                                

    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all("li","clearfix job-bx wht-shd-bx")

                                                        # It'lxml'-  will prettify or decorate our html code
                                                        # and work with its tags like python object.
                                                
                                                                      


                                                           #"""lxml, parsing is defined as the processing of a piece of python program and
                                                            #converting these codes into machine language.
                                                             #In general, we can say parse is a command for dividing the given program code
                                                            #into a small piece of code for analyzing the correct syntax."""

    


                                                                                                     #class_ , not class because class is bult in keyword in  python,
                                                                                                     #here we create python class,
                                                                                                     #so that's why we will add underscore ( _ ) after class



    for i in jobs:
        published_date=i.find("span",class_="sim-posted").span.text
        if "few" in published_date:
            company_name=i.find("h3", class_ ='joblist-comp-name').text.replace(" ","")
            skills=i.find("span",class_="srp-skills").text.replace(" ","")
            job_des=i.find("ul",class_="list-job-dtl clearfix").text.replace("\n","")#.replace("\r","")
            link=i.header.h2.a["href"]

                                             #"here we won't use .text and .find ,if we use .find, it will everything"
                                            #"inside h2 header and if we use .text, it will give nothing, only space"
                                               #"value due to we will use something else funct."

            if unfimilar_skills not in skills:
        

                print(f"Company Name : ",company_name.strip())
                print(f"Skills : ",skills.strip())
                print(f"link : ",link)
                                              #print(job_des)

                print(" ")


print(find_jobs())
        
         
        


    




