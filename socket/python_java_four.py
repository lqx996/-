import socket
import sys 
sys.path.append("./") 
import python_object_detction_client_float_def
from python_object_detction_client_float_def import object_detection
from python_object_detction_client_float_def import gray
from python_object_detction_client_float_def import equalization
from python_object_detction_client_float_def import denoising
from python_object_detction_client_float_def import dehaze

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("create socket succ!")

    sock.bind(('',8555))
    print('bind socket succ!')

    sock.listen(5)
    print('listen succ!')

except:
    print("init socket error!")

while True:
    print("listen for client...")
    conn,addr=sock.accept()
    print("get client")
    print(addr)
    

    conn.settimeout(30)
    szBuf=conn.recv(1024)
    print("recv:"+str(szBuf,'gbk'))
    method_path =str(szBuf,'utf-8')
    method = method_path.split("||")[0]
    paths =  method_path.split("||")[-1]
    #results=python_object_detction_client_float_def.object_detection(path=str(szBuf,'utf-8'))
    if method == "gray":
        results=python_object_detction_client_float_def.gray(path=paths)
        conn.send(str.encode(str(results)))
    # elif method == "gray":
    #     results=python_object_detction_client_float_def.gray(path=paths)
    #     conn.send(str.encode(str(results)))
    elif method == "equalization":
        results=python_object_detction_client_float_def.equalization(path=paths)
        conn.send(str.encode(str(results)))
    elif method == "denoising":
        results=python_object_detction_client_float_def.denoising(path=paths)
        conn.send(str.encode(str(results)))
    elif method == "dehaze":
        results=python_object_detction_client_float_def.dehaze(path=paths)
        conn.send(str.encode(str(results)))
    else:
        conn.send(b"no_model")

    conn.close()
    print("end of servive")

    
        
         


    
"""
    if "0"==szBuf:
        conn.send(b"exit")
    else:
       # bytes(s, encoding = "utf8")
        conn.send(str.encode(str(results)))
        #str.encode(results)
"""

    