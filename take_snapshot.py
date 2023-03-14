import json
import urllib3
import requests
from requests.auth import HTTPBasicAuth

prism_addr = "10.129.40.15"
prism_user = "localadmin"
prism_pass = "Nutanix/4all!"

request_headers = {"Content-Type": "application/json", "charset": "utf-8"}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_vm_specs():
    # get all VM specs
    endpoint = f'https://{prism_addr}:9440/api/nutanix/v2.0/vms'

    results = requests.get(
        endpoint,
        headers=request_headers,
        verify=False,
        auth=HTTPBasicAuth(prism_user, prism_pass),
    ).json()

    vm_specs = results["entities"]
    return vm_specs


def take_snapshot(snapshot_name, vm_uuid):
    payload = {
            "snapshot_specs": [
                {
                    "snapshot_name": snapshot_name,
                    "vm_uuid": vm_uuid
                }
            ]
    }
    endpoint = f'https://{prism_addr}:9440/api/nutanix/v2.0/snapshots'
    results = requests.post(
        endpoint,
        data=json.dumps(payload),
        headers=request_headers,
        verify=False,
        auth=HTTPBasicAuth(prism_user, prism_pass)
    )

    return results


if __name__ == '__main__':

    vm_specs = get_vm_specs()
    snapshot_name = "test_20220912"

    for vm in vm_specs:
        print(type(vm))
        vm_name = vm.get("name")
        vm_uuid = vm.get("uuid")
        print(f"vm_name:{vm_name} vm_uuid:{vm_uuid}")

        task = take_snapshot(snapshot_name, vm_uuid)
        print(task.text)
