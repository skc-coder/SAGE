https://en.wikipedia.org/wiki/MAC_address

# doubt
	can hosts communciate using only mac address? how does a lan work? do these applications use only mac address? how does os support it? doesnt os try to forward it to a socket/port?

	does router/local hosts use ip address and mac both to communicate with local devices/ with each other.
	why?




Why we need IP address when we have mac?
Becuase mac address can be spoofed/cpoied and hence traffic can be higecked.

It also doesnt support suppernetting.

Why mac when we have IP?
If we dont have a device specific idnetifier we will always need a [[DHCP]] server like thing to give ids for devices to communicate. that is inefficient.  
Bad answers here:
https://stackoverflow.com/questions/66290232/why-do-we-need-mac-addresses-when-you-have-local-ip-addresses