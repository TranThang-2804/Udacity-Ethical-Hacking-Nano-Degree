I. Overview

This project will take you on a journey through modern penetration tester and red teamer methodologies. This project will reinforce skills demonstrated throughout the course and challenge you to be efficient with documentation and testing efforts to generate a report in a timely fashion. The reporting process will also help the student understand the many business applications of security testing.


This includes:

1. Organizational Reconnaissance - Identifying where the organization's website is hosted, the platform on which it is hosted, and any DNS records of interest.
2. Network Scanning - The target company will provide a virtual machine intended for production point of sale and customer interaction. This virtual machine is to be scanned heavily to gather as much intelligence as possible.
3. Vulnerability and Exploit Research - You will spend time investigating software version discoveries for known vulnerabilities and any published exploit code.
4. System Exploitation - You will exploit two specific vulnerabilities on the system, though more exist. These vulnerabilities may compound on each other and lead to other mistakes made by the developers.
5. Produce a Meaningful Report - You will craft a single report that speaks to multiple audiences, some technical, and some non-technical. This report will include an executive summary, significant findings, and reproducible methodology.

II. Information about the system
1. Network investigation
![Alt text](./images/network_diagram.png?raw=true "Optional Title")

2. Detailed information
![Alt text](./images/infrastructure.svg "Optional Title")

III. Instruction
1. Recon
  - Checking public webpage (https://learnaboutsecurity.com/) information
    + [ ] Search for the website on Shodan or other recon websites
    + [ ] Discover the DNS information of the website
    + [ ] Identify web technologies the website uses

2. Scanning
> You will need to complete vulnerability scans against the public website (learnaboutsecurity.com), the DMZ servers (DMZIServer and Debianx64DMZOnCloudNew), and the employee workstation (Win-10).

  + [ ] Scan for open ports
  + [ ] Scan for running services
  + [ ] Scan for sensitive files

> You also recall that there is sometimes a hidden folder that stores access credentials by default. You should be able to reveal sensitive data by:

  + [ ] Running a directory scan (dirb) against DMZIServer using the Udacity wordlist
  + [ ] Reveal root access to the DMZIserver