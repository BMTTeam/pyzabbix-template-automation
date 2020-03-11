# Directory Info 
_______________________________________________________
1) **APIs**  : Below folder contain method/class to do CRUD operation for below elements 
    
    - Hostgroups
    - Hosts
    - Templates 
      
2) **Data** : This contain the csv files which we are going to use to add host in server
    
    * SampleData1.csv        
    * SampleData2.csv 

3) **Docs** :    
     
    - Runme.md       : This file will have basic info regarding to how to run programms
    - Host.md        :  This has documentation related to classes and there method for Host Component    
    - Template.md    :  This has documentation related to classes and there method for Host Component    
    - Hostgroups.md  :  This has documentation related to classes and there method for Host Component    
        
           
4) **Logs** : 
    - connections.log : It will contain logs related to connection to zabbix master url
    - hosts.log       : It will contain log related to host addition , updation etc
    - XXXXX.log       : You can create any log file you want          

5) **Properties** :           
    
    - **credentials.ini**   :  It is Must file here we specify our Zabbix Url , username , password
    - demoConfiguration.ini 
        . This is configuration file for Data/sampleData1.csv
    
    
6) **SampleRun** :           

7) **Utils** : This directory contain modules which contains the utillity function which are helpful in for 
                data modification , validation etc   
    
    - myLogger.py - Used for getting logger object so we can store our logs in Log Folder
    - utilfun.py  - This module contain utility functions 
    - VM.py       - It contain class which we will pass appropriate paramater then it will process this data and we 
                     will get required groupIdList , TemplateIdList etc for Add respective vm in Server
    
settings.py :   
    - It contains the path for Logs Directory , Project Root Directory , Properties Directory   
                                 
------------------------