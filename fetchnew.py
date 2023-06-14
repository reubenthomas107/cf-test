import time

def process_vms(vm_list):
    # Your code to make predictions on VMs goes here
    for vm in vm_list:
        # Make predictions on vm
        # ...

# Initial list of VMs
vm_list = ["vm1", "vm2", "vm3"]

while True:
    # Check for updates to the list of VMs
    # Update vm_list from your frontend or a file
    updated_vm_list = get_updated_vm_list()  # Implement this function to retrieve the updated list
    
    if updated_vm_list != vm_list:
        # Process the updated list of VMs
        process_vms(updated_vm_list)
        vm_list = updated_vm_list

    # Sleep for a specific interval before checking for updates again
    time.sleep(60)  # Sleep for 60 seconds before checking for updates
