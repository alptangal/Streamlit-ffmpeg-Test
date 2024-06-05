import os,sys
import server
import asyncio
import requests

async def main():
    try:
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        print('Client closed')
        pid = os.fork() 
        if pid > 0:
        
            print("\nIn parent process")
            # Wait for the completion 
            # of child process and    
            # get its pid and 
            # exit status indication using
            # os.wait() method
            info = os.waitpid(pid, 0)
        
            
            # os.waitpid() method returns a tuple
            # first attribute represents child's pid
            # while second one represents
            # exit status indication
        
            # Get the Exit code 
            # used by the child process
            # in os._exit() method
            
            # firstly check if
            # os.WIFEXITED() is True or not
            if os.WIFEXITED(info[1]) :
                code = os.WEXITSTATUS(info[1])
                print("Child's exit code:", code)
        
        else :
            print("In child process")
            print("Process ID:", os.getpid())
            print("Hello ! Geeks")
            print("Child exiting..")
            
            # Exit with status os.EX_OK
            # using os._exit() method
            # The value of os.EX_OK is 0        
            os._exit(os.EX_OK)
    except Exception as error:
        print(error)
        #if 'No connection could be made because the target machine actively refused it' in str(error) or ('req' in locals() and req.status_code>=400):
        server.b()  
        os.system('''
                npm install @dank074/discord-video-stream@latest
                npm install discord.js-selfbot-v13@latest
                ''')
        os.system('node main.js')
asyncio.run(main())