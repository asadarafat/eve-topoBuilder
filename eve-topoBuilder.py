import requests
import json
import time
import datetime
#from sandbox import credential

# aarafat-tag:
# lab object with default parameter
class lab(object): 
    defaults = {
        'path':'/api-folder',
        'name':'from-api',
        'version':'1',
        'author':'Asad',
        'description':'NSP'
        }
    
    def __init__(self, name=None):
        if name:
            lab.defaults['name'] = name
        for key, value in lab.defaults.items():
            setattr(self, key, value)
        super(lab, self).__init__()

# aarafat-tag:
# node object with default parameter
class node(object): 
    defaults = {
        'console': 'telnet',
        'delay': '0',
        'id': '1',
        'left': '360',
        'icon': 'Router.png',
        'image': 'timos-15.0.R3',
        'name': 'vSIM-01-from-API-class',
        'ram': '4096',
        'status': '0',
        'template': 'timos',
        'type': 'qemu',
        'top': '177',
        'config': '0',
        'cpu': '2',
        'ethernet': '10'
        }
    
    def __init__(self, image=None):
        if image:
            node.defaults['image'] = image
        for key, value in node.defaults.items():
            setattr(self, key, value)
        super(node, self).__init__()


# aarafat-tag:
# network object with default parameter    
class network(object): 
    defaults = {
        'count':'1',
        'name':'netNameDefault',
        'type':'bridge',
        'left':'420',
        'top':'210',
        'visibility':'1',
        'postfix':'0'
        }
    
    def __init__(self, name=None):
        if name:
            network.defaults['name'] = name
        for key, value in network.defaults.items():
            setattr(self, key, value)
        super(network, self).__init__()
        
        

def login(serverIP):
    headers = {
        'Content-type': 'application/json',
        }
    payload = credential
    response = requests.post('http://'+str(serverIP)+'/api/auth/login', headers=headers, data=payload)
    cookie = response.cookies
    #print(datetime.datetime.now())
    #print (json.dumps(json.loads(response.text), indent=5))
    return cookie
    
    
def createLab(serverIP, payloadLab):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    response = requests.post('http://'+str(serverIP)+'/api/labs', headers=headers, cookies=cookies, data=payloadLab)
    parsed = json.loads(response.text)
    print(datetime.datetime.now())
    print (json.dumps(parsed, indent=5))
    return response

def deleteLab(serverIP):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    response = requests.delete('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl', headers=headers, cookies=cookies)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response



def createNode(serverIP, payload):  
    #print login()
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    #payload = nodeJson
    #print payload
    response = requests.post('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/nodes', headers=headers, cookies=cookies, data=payload)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response

def getNodes(serverIP):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    response = requests.get('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/nodes', headers=headers, cookies=cookies)
    #print(datetime.datetime.now())
    #print (json.dumps(json.loads(response.text), indent=5))
    return response

# to be fixed
def getNode(nodeid):  
    response = getNodes()
    #print json.dumps(response.json().get('data').get('1').get('id'), {},indent=5, sort_keys=True)
    data = json.dumps(response.json().get('data').get(str(nodeid)), {},indent=5, sort_keys=True)
    data = json.loads(data)

    return data
    
def getNodeId(serverIP, nodeName):
    dictNodeId =  json.loads(json.dumps(getNodes(serverIP).json().get('data'), {},indent=5, sort_keys=True))
    for key, node in dictNodeId.items():
        #print type (node)
        #print node
        #print node.get('name')
        if node.get('name') == str(nodeName):
            return node.get('id')

def deleteNodes():  
    cookies = login()
    headers = {
        'Content-type': 'application/json',
        }
    response = requests.delete('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/nodes', headers=headers, cookies=cookies)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response

def connectNodes(serverIP, nodeID, netID, interface):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    print 'http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/nodes/'+str(nodeID)+'/interfaces'
    #payload = '\n  {\n   "'+str(netID)+'":'+str(interface)+'\n  }\n  '
    payload = '\n  {\n   "'+str(interface)+'":'+str(netID)+'\n  }\n  '
    print payload
    response = requests.put('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/nodes/'+str(nodeID)+'/interfaces', headers=headers, cookies=cookies, data=payload)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response



def createNet(serverIP, payload):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    print payload
    response = requests.post('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/networks', headers=headers, cookies=cookies, data=payload)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response

def getNet():  
    cookies = login()
    headers = {
        'Content-type': 'application/json',
        }
    response = requests.get('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/networks', headers=headers, cookies=cookies)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response

def hideNetVisibility(serverIP, netID):  
    cookies = login(serverIP)
    headers = {
        'Content-type': 'application/json',
        }
    payload = '\n {\n   "visibility":0\n }\n '
    print payload
    response = requests.put('http://'+str(serverIP)+'/api/labs/api-folder/from-api.unl/networks/'+str(netID), headers=headers, cookies=cookies, data=payload)
    print(datetime.datetime.now())
    print (json.dumps(json.loads(response.text), indent=5))
    return response



# aarafat-tag: to update node instance attributes with actual one from eve-server
node01 = node()
def setNodeObjectAtr(nodeObject, attributeDict):
    for key, value in attributeDict.items():
        setattr(node01, key, value)



# aarafat-tag:
## HOW TO USE:
##
### 1/ edit default attributes of lab, node and network class.
### 2/ edit serverIPaddress and credential
### 3/ edit topology - to connect router-a with port 1/1/1 to router-b with port 1/1/2
###                    use following syntax ('router-a', '1'): ('router-b', '2')
##
## TODO 
##
### - / generalized the API path
### - / randomised node and net coordinate

serverIPaddress = '135.241.247.222'
credential =  json.dumps({
        "username": "admin",
        "password": "mainstreet"
        })

topology = {('R1', '1'): ('B2', '1'),
            ('R2', '2'): ('B3', '2'),
            ('R1', '3'): ('B3', '3'),
            ('R2', '4'): ('B2', '4'),
            ('R1', '5'): ('R2', '5'),
            ('R10', '6'): ('B10', '6')}

topo = topology

lab01 = lab()
payloadLab = json.dumps(lab01.__dict__)

def buildTopo(serverIP, topo):
    
    deleteLab(serverIP)
    nets = dict()
    nodes = dict()

    createLab(serverIP, payloadLab)
    nodesJson = dict() 
    netsJson = dict()

    netID = 0

    for (a_name, a_intf), (b_name, b_intf) in topo.iteritems():
        
        netID = netID + 1
    
        if not a_name in nodes:
            nodes[a_name] = node()
            nodes[a_name].name = a_name
            nodesJson[a_name]=json.dumps(nodes[a_name].__dict__)
            payload = nodesJson[a_name]
            createNode(serverIP, payload)                
            print(datetime.datetime.now())
            print("*** NODE {} CREATED".format(a_name))
            
        if not b_name in nodes:
            nodes[b_name] = node()
            nodes[b_name].name = b_name
            nodesJson[b_name]=json.dumps(nodes[b_name].__dict__)
            payload = nodesJson[b_name]
            createNode(serverIP, payload)
            print(datetime.datetime.now())
            print("*** NODE {} CREATED".format(b_name))
        time.sleep(1)
        nets[netID] = network()
        nets[netID].name ='net-'+str(netID)
        netsJson[netID]=json.dumps(nets[netID].__dict__)
        payloadNet = netsJson[netID]
        createNet(serverIP, payloadNet)

        print '*********'
        print 'NET: '+ str(netID)
        print 'node_name_a: '+ a_name
        print 'nodeID:'
        print getNodeId(serverIP, a_name)
        print 'interface_a: '+ a_intf
        print 'node_name_b: '+ b_name
        print 'nodeID:'
        print getNodeId(serverIP, b_name)
        print 'interface_b: '+ b_intf
        print '*********'
        

        connectNodes(serverIP, getNodeId(serverIP, a_name), netID, a_intf)
        connectNodes(serverIP, getNodeId(serverIP, b_name), netID, b_intf)
        time.sleep(1)
        hideNetVisibility(serverIP, netID)


buildTopo(serverIPaddress, topo)


