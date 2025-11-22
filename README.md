# Introduction 
I'm building a CIDR range calculator inspired by AWS IPAM. I couldn't find a simple calculator online that took AWS' requirements into consideration so I built my own 

# Goals: 
    - User is able to enter in a VPC CIDR block (IPV4 address and net mask) and the number of subnets they want
    - User will receive a range of ip addresses for each subnet (with a new subnet mask)
    - User is able to interact with it via a web interface (implemented by flask, docker, Terraform and CI/CD pipelines)
    - Write an article to further reinforce what I've learned


# My understanding so far
    - A VPC is your very own slice of the cloud. It provides an isolated network for you to build a web application using cloud resources (some resources may be public whereas others can only communicate with the resources in the private network)
    - In order to isolate internet facing resources vs private resources, public and private subnets need to be created (we'll need an Internet gateway and Nat Gateway too) 
    - The Internet Assigned numbers Authority (IANA) govern unique id's on the internet such as IP addresses. WHY?
    - However, private networks are able to use IP addresses without IANA's permission due to Request for Comment 1918 (RFC 1918)
    - RFC 1918 allows for organisations to create ip addresses within their internal private networks (private subnets)
    - They have reserved 3 IP address ranges for this:
        - 10.0.0.0 - 10.255.255.255 (10/8 prefix)
        - 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
        - 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
    - Amazon VPC IP Address Manager (IPAM) is a service in AWS designed to manage IP addresses across an organisation's AWS environment. It works by keeping track and distributing ip addresses across the network and saving a few ranges in case of changes to demand

## Why is a CIDR calculator important? 
    - to prevent ip addresses from overlapping and allow for efficient ip address planning 

 ##  What requirements does AWS have?
    - 5 reserved IPs per subnet so they must be deducted:
        - Network address (x.x.x.0)
        - AWS services (x.x.x.1, x.x.x.2, x.x.x.3)
        - Broadcast address (x.x.x.255)
- Minimum subnet size: /28 (16 - 5 IPs) 

## What don't I understand yet?
  - Flask 
  - How to work out the new subnet mask 



# Builder's Checklist
    [] create a function to allow users to input CIDR block and number of subnets
        [] Add validations to ensure only valid CIDR notations are inputted 
        [] Write unit tests for the function (using pytest).
    [] create a function that works out the number of available hosts on the network using the net mask 
    [] Create a function that works out the total number of ips
    [] create function that equally divides (as much as possible) the available IPs among the specified number of subnets, deducting 5 IP’s in line with AWS' rules (remove the first four and the last one.)
    [] Translate the number of IPs needed for each subnet into the correct CIDR prefix length
    [] Provide user with a list of subnet cidrs
    [] Create a Flask app with a form
    [] Dockerize the Flask app.
    [] Deploy using Terraform and CI/CD
   

# Resources
    - [What is RFC 1918?](https://www.techtarget.com/whatis/definition/RFC-1918) 
    - [More RFC 1918 ](https://datatracker.ietf.org/doc/html/rfc1918)
    - [Understanding Private and Public Subnets ](https://docs.netgate.com/pfsense/en/latest/network/addresses.html)
    - [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) 
    - [How does IPAM work?](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/)
    - [Ipaddress Module Docs](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts)
    - [AWS' Requirements](https://aws.amazon.com/vpc/faqs/#topic-3)
    