import os
import pyfiglet
os.system("tput setaf 2")
print("-".center(150,"-"))
os.system("tput setaf 1")
welcome="Python Automation"
ascii_banner = pyfiglet.figlet_format(welcome)
print(ascii_banner)
while True:
	os.system("tput setaf 3")
	print(" \n 1.Basic Linux Commands \n 2.AWS Cloud \n 3.Docker \n 4.Apache httpd(WebServer) \n 5.Hadoop \n 6.Exit \n")
	os.system("tput setaf 2")
	print("-".center(150,"-"))
	main_choice=input("Choose your domain(1-6):")
	if main_choice=='6':
		exit(); 
	system=input("\n Where you want to perform this[Local(L)/Remote(R)/AWS(A)]:")
	while True:
		os.system("tput setaf 4")
		if main_choice=='1' and system=='L':
			print("\n 1.Date \n 2.Calendar \n 3.Network details \n 4.Other Linux Commands \n 5.Go back to main menu \n")
			basic_choice=input("Please specify your requirement:")
			if basic_choice=='1':
				os.system("tput setaf 2")				
				os.system("date")
			elif basic_choice=='2':	
				os.system("tput setaf 2")			
				os.system("cal")
			elif basic_choice=='3':
				os.system("tput setaf 2")
				os.system("ifconfig")
			elif basic_choice=='4':
				li_cmd=input("Enter the Linux command:")
				os.system("tput setaf 2")
				os.system("{}".format(li_cmd))
			elif basic_choice=='5':
			 	break
		elif main_choice=='1' and system=='R':
			ip=input("Enter the remote IP:")
			print("\n 1.Date \n 2.Calendar \n 3.Network details \n 4.Other Linux Commands \n 5.Go back to main menu \n")
			basic_choice=input("Please specify your requirement:")
			if basic_choice=='1':
				os.system("tput setaf 2")				
				os.system("ssh {} date".format(ip))
			elif basic_choice=='2':
				os.system("tput setaf 2")			
				os.system("ssh {} cal")
			elif basic_choice=='3':
				os.system("tput setaf 2")
				os.system("ssh {} ifconfig")
			elif basic_choice=='4':
				os.system("tput setaf 2")
				li_cmd=input("Enter the Linux command:")
				os.system("ssh {} {}".format(ip,li_cmd))
			elif basic_choice=='5':
			 	break
		elif main_choice=='2' and system=='A':
			print(" \n 1.Create Key Pair \n 2.Delete Key Pair \n 3.Create Security group \n 4.Launch EC2 instance \n 5.Start EC2 instance \n 6.Stop EC2 instance \n 7.Create EBS volume \n 8.Attach EBS volume to EC2 instance \n 9.Describe instance \n 10.Create S3 bucket \n 11.Put object in S3 bucket \n 12.Remove object in S3 bucket \n 13.Delete S3 bucket \n 14.Create Cloudfront distribution \n 15.Go back to main menu \n")
			aws_choice=input("Please specify your requirement:")
			if aws_choice=='1':
				keyname=input("Please enter the keyname:")
				os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
			elif aws_choice=='2':
				keyname=input("Please enter the keyname:")
				os.system("aws ec2 delete-key-pair --key-name {}".format(keyname))
			elif aws_choice=='3':
				grpname=input("Enter group name:")
				os.system("aws ec2 create-security-group --group-name {} --description tasksg".format(grpname))
			elif aws_choice=='4':
				sgid=input("Please provide the security group id:")
				os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-917871f9 --security-group-ids {1} --key-name {0}".format(keyname,sgid))
			elif aws_choice=='5':
				sinstid=input("Please provide the instance id:")
				os.system("aws ec2 start-instances --instance-ids {}".format(sinstid))
			elif aws_choice=='6':
				sinstid=input("Please provide the instance id:")
				os.system("aws ec2 stop-instances --instance-ids {}".format(sinstid))
			elif aws_choice=='7':
				ebs_size=input("Enter the EBS volume size:")
				os.system("aws ec2  create-volume  --availability-zone ap-south-1a --size {}".format(ebs_size))
			elif aws_choice=='8':
				volid=input("Please provide the Volume id:")
				instid=input("Please provide the Instance id:")
				os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(volid,instid))
			elif aws_choice=='9':
				instid=input("Please provide the Instance id:")
				os.system("aws ec2 describe-instances --instance-id {}".format(instid))
			elif aws_choice=='10':
				s3_name=input("Enter unique name for S3 bucket:")
				os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1".format(s3_name))
			elif aws_choice=='11':
				object_name=input("Enter Object name to put inside S3 bucket:")
				s3_name=input("Enter S3 Bucket name:")
				os.system("aws s3 cp /root/Documents/ARTH/{} s3://{} --acl public-read".format(object_name , s3_name))
			elif aws_choice=='12':
				object_name=input("Enter S3 bucket name:")
				s3_name=input("Enter object name:")
				os.system("aws s3 rm s3://{}/{}".format(object_name , s3_name))
			elif aws_choice=='13':
				s3_name=input("Enter S3 Bucket name:")
				os.system("aws s3api delete-bucket --bucket {} --region ap-south-1".format(s3_name))
			elif aws_choice=='14':
				s3_name=input("Enter S3 bucket name:")
				os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(s3_name))
			elif aws_choice=='15':
				break
		elif main_choice=='3' and system=='L':
			print(" 1.Pull image from docker hub \n 2.Launch Container \n 3.Details of running docker container \n 4. Details of docker images \n 5.Start docker container \n 6.Inspect docker Container \n 7.Stop docker container \n 8.Remove docker image \n 9.Delete a docker container \n 10.Delete all containers \n 11.Go back to main menu \n")
			doc_choice=input("Please specify your requirement:")
			if doc_choice=='1':
				img=input("Enter Image name: ")
				os.system("tput setaf 2")
				os.system("sudo docker pull {}".format(img))
			elif doc_choice=='2':
				cnt=input("Enter Container Name: ")
				img=input('Enter Image Name :-  ')
				os.system("tput setaf 2")
				os.system("docker run -dit --name {} {}".format(cnt, img))
			elif doc_choice=='3':
				os.system("tput setaf 2")
				os.system("docker ps")
			elif doc_choice=='4':
				os.system("tput setaf 2")
				os.system("docker images")
			elif doc_choice=='5':
				img=input("Enter docker container name: ")
				os.system("tput setaf 2")
				os.system("docker start {}".format(img))
			elif doc_choice=='6':
				img=input("Enter container name to inspect: ")
				os.system("tput setaf 2")
				os.system("docker inspect {}".format(img))
			elif doc_choice=='7':
				img=input("Enter docker container name: ")
				os.system("tput setaf 2")
				os.system("docker stop {}".format(img))
			elif doc_choice=='8':
				img=input("Enter Image name to remove: ")
				os.system("tput setaf 2")
				os.system("sudo docker rmi {}".format(img))
			elif doc_choice=='9':
				img=input("Enter container name to delete: ")
				os.system("tput setaf 2")
				os.system("docker rm -f {}".format(img))
			elif doc_choice=='10':
				os.system("tput setaf 2")
				os.system("docker rm -f $(sudo docker ps -a -q)")
			elif doc_choice=='11':
				break
		elif main_choice=='4' and system=='L':
			print("Configuring WebServer.Hold on :) ")
			os.system("tput setaf 2")
			os.system("yum install httpd -y")
			os.system("systemctl start httpd")
			os.system("systemctl enable httpd")
			os.system("cp index.html /var/www/html")
			gb=input("\n Press 1 to go back to main menu:")
			if gb=='1':
				break
		elif main_choice=='4' and system=='R':
			ip=input("Enter the remote IP:")
			print("Configuring Remote WebServer.Hold on :) ")
			os.system("tput setaf 2")
			os.system("ssh {} yum install httpd -y".format(ip))
			os.system("ssh {} systemctl start httpd".format(ip))
			os.system("ssh{} systemctl enable httpd".format(ip))
			os.system("scp index.html{}:/var/www/html".format(ip))
			gb=input("\n Press 1 to go back to main menu:")
			if gb=='1':
				break
		elif main_choice=='5' and system=='L':
			import os
			print(" 1.Configuring core-site.xml (Similar for NameNode & DataNode) \n 2.Configuring hdfs-site.xml of NameNode \n 3.Configuring hdfs-site.xml of DataNode \n 4.Formatting NameNode \n 5.Starting NameNode \n 6.Checking whether Hadoop Service Started of NameNode/DataNode \n 7.Checking the no. of DataNodes \n 8.Starting DataNode \n 9.Disable Firewall \n 10.Creating a Directory in Hadoop Cluster \n 11.Uploading a File in the Directory \n 12.Viewing the List of Files in the Directory \n 13.Deleting the Directory \n 14.Stopping the Hadoop Cluster NameNode \n 15.Stopping the Hadoop Cluster DataNode \n 16.Go back to main menu")
			i=int(input("Enter the requirement:"))
			if i==1:
				os.system('echo \<configuration\> >> core-site.xml')
				os.system('echo \<property\> >> core-site.xml')
				os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
				nnip=input("Enter the IP Address of NameNode:")
				os.system("tput setaf 2")
				os.system("echo \<value\>{}:9001\<\/value\> >> core-site.xml".format(nnip))
				os.system('echo \<\/property\> >> core-site.xml')
				os.system("echo \<\/configuration\> >> core-site.xml")
				os.system("mv -f core-site.xml /etc/hadoop")
			elif i==2:
				os.system('echo \<configuration\> >> hdfs-site.xml')
				os.system('echo \<property\> >> hdfs-site.xml')
				os.system("echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml")
				ndir = input('Enter directory name you want to create for Namenode:')
				os.system("tput setaf 2")
				os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(ndir))
				os.system('echo \<\/property\> >> hdfs-site.xml')
				os.system("echo \<\/configuration\> >> hdfs-site.xml")
				os.system("mv -f hdfs-site.xml /etc/hadoop")
			elif i==3:
				os.system('echo \<configuration\> >> hdfs-site.xml')
				os.system('echo \<property\> >> hdfs-site.xml')
				os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
				ddir = input('Enter directory name you want to create for Datanode:')
				os.system("tput setaf 2")
				os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(ddir))
				os.system('echo \<\/property\> >> hdfs-site.xml')
				os.system("echo \<\/configuration\> >> hdfs-site.xml")
				os.system("mv -f hdfs-site.xml /etc/hadoop")
			elif i==4:
				os.system("tput setaf 2")
				os.system("hadoop namenode -format")
			elif i==5:
				os.system("tput setaf 2")
				os.system("hadoop-daemon.sh start namenode")
			elif i==6:
				os.system("tput setaf 2")
				os.system("jps")
			elif i==7:
				os.system("tput setaf 2")
				os.system("hadoop dfsadmin -report")
			elif i==8:
				os.system("tput setaf 2")
				os.system("hadoop-daemon.sh start datanode")
			elif i==9:
				os.system("tput setaf 2")
				os.system("systemctl disable firewalld")
			elif i==10:
				dir=input("Enter the Name of Directory to be Created:")
				os.system("tput setaf 2")
				os.system("start -dfs.sh")
				os.system("hadoop fs -mkdir \{}" . format(dir))
			elif i==11:
				file=input("Enter the Name of File:")
				os.system("tput setaf 2")
				os.system("hadoop fs -put \{} \{}" . format(file,dir))
			elif i==12:
				os.system("tput setaf 2")
				os.system("hadoop fs -ls \{}" . format(dir))
			elif i==13:
				dir=input("Enter the Name of Directory to be Deleted:")
				os.system("tput setaf 2")
				os.system("hadoop fs -rmr \{}" . format(dir))
				os.system("stop -dfs.sh")
			elif i==14:
				os.system("tput setaf 2")
				os.system("hadoop-daemon.sh stop namenode")
			elif i==15:
				os.system("tput setaf 2")
				os.system("hadoop-daemon.sh stop datanode")
			elif i==16:
				break
		else:
			print("Wrong command!!Please try again")

		
			
		
	



