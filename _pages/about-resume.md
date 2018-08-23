---
toc: true 
toc_label: 'Contents' 
toc_icon: 'cog'
layout: single
permalink: /aboutme-ahmedzbyr-R1ljWmE0RXVrblUyWVo0eW51OFhWR2piNmI1eGR3/
title: "ZUBAIR AHMED"
last_modified_at: 2018-01-30T11:22:24-05:00
header: { overlay_image: /assets/images/amsterdam1.jpg}
---

![Mobile:](https://raw.githubusercontent.com/ahmedzbyr/Font-Awesome-SVG-PNG/master/black/png/32/phone-square.png) `+31-6-8750-6688` <br>
![Email:](https://raw.githubusercontent.com/ahmedzbyr/Font-Awesome-SVG-PNG/master/black/png/32/envelope-square.png)  `ahmedzbyr@gmail.com` <br>
![Location:](https://raw.githubusercontent.com/ahmedzbyr/Font-Awesome-SVG-PNG/master/black/png/32/globe.png) `Amsterdam, Netherlands.`

## What I Do and Love.

* I am a passionate DevOps engineer with a strong focus on Hadoop, AWS and big data infrastructure automation. Have worked on automating deployments of Cloudera Hadoop infrastructure using Cloudera python API.  Most of the project worked on have been scrum agile. 
* Have been working on deploying many Cloudera Hadoop environments. Since we had many different business groups/companies which required a cloudera hadoop environments, we had to automate these deployments. 
* Initial deployments were done manually, as OS deployment / Networking deployment was done manually, which took about 10 weeks, most of the time was spent on OS installations, networking and deploying/configuring servers using shell/Ansible scripts. Later OS/Networking was moved to our team we automated this workflow and moved the time from weeks to a couple of days (excluding network VLAN assignments), OS deployment, networking was done using **`Foreman`**, disk-partition and pre-configuration was done using **`Chef`**. Cloudera Hadoop deployment was done using **`Cloudera Python API`**. 
* Currently a cluster with about 40-120 nodes would be deployed in 60 minutes after pre-configuration, including setting **`Kerberos`** security for the cluster, larger cluster take a little longer as the configuration can be deployed parallelly to about 20-30 nodes at a time to reduce load on the admin node. Further automation scripts were created for capacity add for existing environments.    
* Earlier deployments which I had worked on involved using Apache Hadoop, this was for one of the telecom giants for a real-time data processing. This infrastructure was deployed using Ansible which had different components like **`Nginx`**, **`NodeJS`**, **`Kafka`**, **`Storm`**, **`HBase`**, **`Cassandra`**. 
* Keen on working with **`python`**, **`shell scripting`**, **`Chef`**, **`Ansible`** and anything which help me automate.
* In depth knowledge on functionality of every Hadoop daemon, interaction between them, resource utilization and dynamic tuning using python api to make cluster highly available and efficient.
* Access control to data, based on the user groups using the extended ACL features in **`HDFS`** and using **`ldap/kerberos`**, also further enhancing security using **`sentry`**,  **`KTS/KMS`** and **`TLS/SSL`**.
* Setting up monitoring tools such as **`zabbix`**, **`nagios`** and **`ganglia`** to monitor and analyze optimal functioning of cluster and telecom devices, using automation scripts.
* Good understanding of **`NoSQL`** databases such as **`Hbase`**, **`MongoDB`**, **`Cassandra`**.
* Currently learning about **`Tez`**, **`Mesos`**, **`docker`**, **`kubernetes`** would love to work with them. 

## Tools, Achievements & Experience

### Skills, Software and Tools

* **Programming**: Python, C, CoreJava, Shell scripting.
* **Configuration Management**: Ansible, Chef.
* **Repository**: svn, git.
* **Load Balancing**: NginX, Tomcat - http - In-memory Session Replication.
* **Big Data**: HDFS, HBase, Kafka, Storm, Zookeeper, Cassandra. Logstash, Elastic Search, Kibana.
* **Monitoring**: Ganglia, Zabbix, Grafana, OpenTSDB.
* **BI Tools**: SpagoBI.

### Significant Projects

* Automated Hadoop Deployments
* Realtime Log/Event Processing
* Network Performance Analysis
* Network Acceleration Product

### Education

* 2001 - 2005 Bachelor of Engineering in Information Science, Global Academy of Technology, VTU, Bangalore INDIA.

### Certifications

* **Hadoop Administration** - Edureka License [14041203004](http://www.edureka.co/certificates/mycertificate/0e205dfadd4208d823f6bb2fb298ecbe) `June 2014`
* **MongoDB Dev and Admin** - Edureka License [44583561233](http://www.edureka.co/certificates/mycertificate/61802318c7fba83d9c8316586a11b584) `June 2014`
* **R Programming** - Coursera Verified Certificates License [6EA836QXK2](https://www.coursera.org/account/accomplishments/certificate/6EA836QXK2) `August 2014`
* **The Data Scientist’s Toolbox** - Coursera Verified Certificates License [AXZRABXRTG](https://www.coursera.org/account/accomplishments/certificate/AXZRABXRTG) `August 2014`
* **MongoDB Dev** - [M101P: MongoDB for Developers](http://university.mongodb.com/course_completion/335aa77fffce4625be18c2b1e2405799) `May 2016`
* **MongoDB DBA** - [M102: MongoDB for DBAs](http://university.mongodb.com/course_completion/ab4f68832e12496584d2d50d17c629b7) `May 2016`

### Organization

* [CGI Nederland](https://www.cgi.com/nl), Amsterdam Netherlands, **[Jan 2018 - Till Date]**
* [Happiest Minds India Private Ltd](http://www.happiestminds.com), Bangalore INDIA, **[Jun 2014 - Dec 2017]**
* [Saggezza India Private Ltd](http://www.saggezza.com), Bangalore INDIA, **[Aug 2006 - Jun 2014]**

## Latest Project Details

### Hadoop Auto Deployment Using Chef [May 2016 - Jul 2016, Oct 2016 - Dec 2017]

Cloudera Manager 5.7, Chef, Python, Cloudera API, MySQL

#### Project Overview

* Baremetal server deployment using Foreman and Chef. 
* Cluster deployment with HDFS, Yarn, Spark, Hue, Hive,Impala, Sentry, Oozie, etc (Automated using Cloudera API).
* Setting up Kerberos for the Hadoop cluster (Automated using Cloudera API).
* Setting up keytrustee server for data-at-rest Encryption. 

#### Roles and Responsibilities

Requirement Analysis

* Gather requirements from business units. 
* Cluster Planning and Cluster Sizing based on the data processing requirements from the business unit. 
* Setting up design patterns for the Cluster. 
* Create documentation workflow and technical douments of the task completed.

DevOps

* Setting up environment for Chef Deployments.
* Cluster deployment with HDFS, Yarn, Spark, Hue, Hive, Impala, Sentry (Automated using Cloudera API).
* Setting up Kerberos for the Hadoop cluster (Automated using Cloudera API Python).
* Setting up keytrustee server for data-at-rest Encryption using Key Trustee Server and Key Management Server.
* Setting up TLS for Cloudera manager and Kafka.
	* TLS Configuration was done using chef cookbook.
	* Dev environments used self-signed certificates and 
	* Prod Env used signed certificates shared by the security team. 
* Creating cookbooks for deployment.
* Created chef cookbooks for Post OS configuration, which included [Base Cookbook]
	* Setting up SSSD, iptables, selinux, sysctl, disk paritions.
	* Setting up users, mysql connectors, squid proxy, sysauth, krb5 configuration.
	* Setting up cloudera manager daemons and agents.
* Created chef cookbook for Cloudera Manager, which includes. [Base Cookbook]
	* Setting mysql or postgres based on requirements.
	* Creating Databases for different services cloudera manager, activity monitor, resource monitor, sentry, navigator audit, navigator metastore, hue, oozie, hive metastore.
	* Create Database users which have permissions on specific databases created above.
	* Setup Cloudera manager server and agent.
	* Setup and install mysql connector and postgres client based on requirement.
	* Configuration of Cloudera Manager Server to database and deploy metadata into the database created. 
* Creating RBAC cookbook for each environment. [Custom Cookbook]
	* Created specific cookbook for each team which had specific requirements on deployments.
	* This helps us maintain a base setup cookbook and manager each team from different cookbooks. 


## Other Projects


### Nagios Monitoring and Chef Auto Deployments						Aug 2016 - Sep 2016

Chef, Nagios, Python, MongoDB.

#### Project Overview

* Monitoring Infra using Nagios and Automating installation and setup of Infra using Chef.
* Setting up Nagios Server and Chef Server.
* Configuration of around 450 nodes into Nagios.
* Setting up agents on all the nodes using Chef.
* Configuration of new nodes using Chef Automation, which includes linux and windows based servers. 


### Hadoop Security Implementation [Aug 2015 – Apr 2016]

Cloudera Manager 5.4, LDAP/Kerberos, Squid, Heartbeat

#### Project Overview

* Security Implementation for Hadoop Cluster.
* Integration of LDAP Kerberos with Hadoop Authentication.

#### Roles and Responsibilities:

Requirement Analysis

* Gather requirement from client and current processing workflow.
* Cluster planning - Using the inputs from the client requirement we create cluster requirements.
* Create requirement specification and design document.

DevOps

* Setting up Cloudera Manager and optimization of Hadoop Cluster.
* Ansible automation for updating and setting up Infrastructure Environment.
	* Setting up Users, Installation of base packages.
	* Setting up LDAP Proxy, Heartbeat for HA.
	* Setting up Squid Proxy.
	* Setting up Monitoring and Performance tuning.
	* SSSD configuration and setup for all nodes.
* Integration of Active Directory with Cloudera Manager.
* Creating RBAC Role based access control for all the users, based on Teams, Business units.
* Setting up Pentaho.
	* Preprocessing data on Pentaho, which was arriving from Mainframe.
	* Raw data was processed to generate CSV data and moved to HDFS.
	* Again this CSV data was processed using Hadoop MR Jobs and stored in Hive and Hbase.

### RealTime Log/Event Processing [Dec 2014 – Jul 2015]

Python, Shell scripting, Hadoop, Ansible, NginX, NodeJS/http2kafka, Kafka, Storm, HBase, Zabbix.

#### Project Overview

* Logs/Events are generated on mobile devices.
* These events are processed in real-time to generate report of current users.
* Logs/Events are send from the devices to the NginX, which is load balanced to NodeJS.
* NodeJS then forwards data to Kafka, which has multiple topics to process each type of Event.
* Kafka sends data to Storm, Which again processes further and stores it in HBase.  
* Hbase data is retrieved using web-service and consumed by D3.

#### Roles and Responsibilities

* Lead the DevOps team to develop scripts for monitoring and processing.
* Auto deployments using Ansible.
* Responsible for back-end data processing.
* Hadoop Cluster Administration, Hadoop Cluster Planning / Monitoring, Hadoop Backup/Recovery, Hbase Administration.
* Performance Tuning for high volume data in-flow.
	* Hadoop, MapReduce Jobs, Hbase, Kafka, Storm, NginX  

### NRT (Near Real Time) CDR Collection and Zabbix Monitoring [June 2014 – Nov 2014]

Python, Shell scripting, Logstash, Elastic Search, Hadoop, Zabbix.

#### Project Overview

* Project is to collect CDR records from multiple devices in near real time using Logstash to put data into HDFS and processing it using Elastic Search and further visualization using Kibana.  
* Zabbix Monitoring was used to monitor Telecom devices using SNMP v1/v2 and custom scripts.

#### Roles and Responsibilities

* Lead the team to develop Monitoring Scripts.
* Scripts for processing.
* Ansible infrastructure deployments.


### Insight Analytics – Network Performance Analysis [Mar 2012 – June 2014]

Python, Shell scripts, Java, HBase DevOps, Hadoop DevOps.

#### Project Overview

* Project was to analyze Network Performance. We get data for all the network elements in the network and do analysis.
* Few of the Analysis is done as follows.
	1. Analysis of node performance.  
	2. Network packet flow performance.
	3. Radio base station (RBS) to Radio Network Controller (RNC) path generation (Forward and Reverse).
	4. LSP path generation and LSP performance, Trunk performance, PWE (Pseudo Wire) analysis, Node Performance.

#### Product Overview.

1. Data Collector
2. Data Processing to HBase
3. Data API Layer
4. Graphs for data analysis

#### Roles and Responsibilities

* Hadoop Cluster Administration,  Hadoop Cluster Planning / Monitoring, Hadoop Backup/Recovery,  Hbase Administration.
* Project data processing workflow.
* Creating task and task allocation, unit test plan, Integration test plan.
* Complete integration and final testing.
* Data analysis.
* Data processing development using JavaScript, shell script and python.

### Statistics Module Generating Process file for Insight Analysis LTE. [Apr 2011 – Feb 2012]

C Programming and Shell scripts.

#### Project Overview

* Development of statistics module. This module is responsible to generate all the statistics for the node (network element).
* Module gets data from the Interfaces, CPU, Tunnels, Shared Memory, MIB2 and more.
* These files are later used for data analysis of the network using OBIEE tools.

### Network Data Acceleration using UDT [Mar 2009 – June 2011]

C++, QT, InnoSetup, DOxygen, Windows, Linux and Mac OS X.

#### Project Overview

* This product was developed from ground up to a fully functional product called Network Data Tunnel.
* Network Data Tunnel (NDT as we call it) is a peer to peer network data packet acceleration product. NDT architecture is designed such that we don't need to have specific application to be installed on each host machine.
* We use proxy based communication using SOCKS4/5 to communicate between host to forwarder proxy and intern this proxy communicates to receiver proxy. (NDT here runs as forwarder and receiver proxy).
* NDT runs with any FTP client which can communicate with SOCKS4/5.
* We have tested NDT with FileZilla and FireFTP and many other FTP clients which support SOCKS4/5.
* Further tested were done for http traffic.

### Network Security and Optimizations [July 2008 – Feb 2009]

C Programming, shell scripting.

#### Project Overview

* Was part of network project management team.
* Task was to ensure project plan was drawn out.
* Getting approvals from all business units. (Third party, Internal business unit, security, Implementation, Project management, vendor management teams).
* VPN site to site connectivity from our client to offshore offices.  
* Ensure secure connections over SonicWall Aventail.
* Managing and monitoring network firewalls.
* Establishing secure network based on the internal security policy.

### Linux Porting on ARM based Boards (Embedded) [Aug 2006 – June 2008]
C, Embedded C, Kernel Cross compiling, Device Drivers.
Linux, MontaVista Linux.

#### Project Overview

* Porting linux kernel to melco custom board.
* Porting linux kernel to TMS320C64 board.
* Development and testing exception handlers.
* Porting x-windows for davinci ARM board using ARM crosscompiler (ARM9TDMI).
