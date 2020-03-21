# Simple Web Server Made With Python  
  ![enter image description here](https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png =100x100)  
  
  
  
This server run in localhost for web test or conection test..

# Sudo 

Run server using:  
```bash
sudo python httpserver.py
```

# Lib to install 

If file dont run in your machine, and your python need install other libs serach the lib in pip and run **pip install name-lib**

# Change page body

If you need change body:  
```python
self.wfile.write("""<h1>My page body</h1>""")
```  
to escape " in html tags you need  """ when begin body and """ when finish.

# Change port

To change server port change 80 for your port number:  
```python
PORT_NUMBER = 80
``` 
