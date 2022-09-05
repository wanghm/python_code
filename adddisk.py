
# Variables

pe_username = 'huimin.wang@ntnx.apj'
pe_password = '!QAZ2wsx'
pe_vip = '10.129.40.11'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
vm_uuid= "@@{platform.metadata.uuid}@@"
size = @@{DummyAPI.CVM_DISK_SIZE}@@*1024*1024*1024
print size

# Get storage container uuid
payload = {}
api_url = "https://"+pe_vip+":9440/PrismGateway/services/rest/v2.0/vms/"+vm_uuid+"?include_vm_disk_config=true"

resp = urlreq(api_url, verb='GET', auth='BASIC', user=pe_username, passwd=pe_password, params=json.dumps(payload), headers=headers)
if resp.ok:
  storage_config = json.loads(resp.text)
  storage_container_uuid = storage_config["vm_disk_info"][1]["storage_container_uuid"]
  print "Storage container uuid is", storage_container_uuid
else:
  print "Error getting storage container uuid", json.dumps(json.loads(resp.content), indent=4)
  exit(1)


# Add new disk to CVM
payload = {"vm_disks":[{"is_cdrom": 'false',"disk_address":{"device_bus":"SCSI","device_index": 1},"vm_disk_create":{"size": size, "storage_container_uuid": storage_container_uuid}}]}
api_url = "https://"+pe_vip+":9440/PrismGateway/services/rest/v2.0/vms/"+vm_uuid+"/disks/attach"
                   
resp = urlreq(api_url, verb='POST', auth='BASIC', user=pe_username, passwd=pe_password, params=json.dumps(payload), headers=headers)
if resp.ok:
  print "Add new disk to CVM successfull", json.loads(resp.text)
else:
  print "Error getting storage container uuid", json.loads(resp.content)
  exit(1)