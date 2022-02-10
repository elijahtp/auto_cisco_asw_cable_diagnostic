# Automation of cable lines diagnostic for cisco 2960 switches

This repository contains two scripts. First one works with cisco 2960 access layer switches on local network, using ssh coonection. Firstly it runs checking if ports connect. Then send command of cable diagnostic to the connected port. In case of some problem (short,open,crosstalk) it puts result of the command in .txt file.
The second script send an email with the result txtfile (the latest created file from the specified folder ).     

 You can execute scripts together one by one, using .bat file and schedule it in task manager. 
