from ipaddress import IPv4Network

# Step 1: User enters in their network VPC CIDR 
cidr_notation= input("Please enter VPC cidr e.g. 10.0.0.0/24: ")
num_subnets = int(input("Please enter in the number of subnets you'll like to create: "))

network = IPv4Network(cidr_notation)
prefix = network.prefixlen
netmask_dot_notation = network.netmask
# print(f"the net mask decimal dot notation: {netmask_dot_notation} ")


# Step 2: Validate Users answers and enforce AWS requirements
def validate_input():
    if prefix >= 28 and num_subnets <=200:
        return 
    else:
        print("AWS requires you to have a prefix length/netmask of no less than /28 and no more than 200 subnets")
  
total_ips = print(validate_input())


