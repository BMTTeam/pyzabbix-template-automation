1) Setting Virtual Environment .  
    <h3> a) For Windows : </h3>        
       
            $ pip install virtualenv  
            $ pip3 install virtualenv  
            $ py -3 -m venv ZabEnv
            $ ZabEnv\Scripts\activate.bat
            $ pip install -r requirements.txt	
            
            $ ZabEnv\Scripts\deactivate.bat	
    
    ------------------------------------------------    
                
    <h3> b) For Linux : </h3>        
            
        $ sudo apt install python3-pip
        $ sudo apt install -y python3-venv
        $ python3 -m venv zabEnv
        $ source zabEnv/bin/activate
        $ pip install -r requirements.txt
        
        $ deactivate
     
2) Add the Credentials and zabbix master url in Properties/Credentials.ini file

3) In Settings.py run the command os.getcwd() and store it in ROOT_DIR variable

4) Check the path are correct by printing variables in settings.py , if not do changes accordingly

5) check if we are able to connect to zabbix by running the APIs/conn.py file  