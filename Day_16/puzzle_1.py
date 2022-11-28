#Run with -O to skip debug messages

def read_packet(data_bin, index):
	if __debug__:
		print("Data to process: " + data_bin[index:])
	packet = []
	#Read header
	packet_version = int(data_bin[index:index+3], base=2)
	index+=3
	packet_type = int(data_bin[index:index+3], base=2)
	index+=3
	if __debug__:
		print("Version: " + str(packet_version))
		print("Type: " + str(packet_type))

	#Literal Value
	if packet_type == 4:
		literal_value = ""
		#Read the literal value, divided in 5-bit groups
		while True:
			#Add the 4 bits in the group
			literal_value+=data_bin[index+1:index+5]
			index+=5
			#Read the group's initial bit
			if data_bin[index-5]=='0':
				#If the initial bit is 0 (last group), skip the padding 0s and end
				#while index<len(data_bin) and data_bin[index]=='0':
				#	index+=1
				break
		if __debug__:
			print("Literal value bin: " + literal_value)
			print("Literal value int: " + str(int(literal_value, base=2)))

		packet = [packet_version, packet_type, int(literal_value, base=2)]
	#Operator
	else:
		subpackets = []
		packet_lenght_type_id = int(data_bin[index], base=2)
		index+=1

		#Length of the sub-packets
		if packet_lenght_type_id == 0:
			subpackets_length = int(data_bin[index:index+15], base=2)
			if __debug__:
				print("Subpackets  length: " + str(subpackets_length))

			index+=15
			subindex=0
			#Read subpackets
			while subindex < subpackets_length:
				subpacket,subindex = read_packet(data_bin[index:index+subpackets_length], subindex)
				subpackets.append(subpacket)
			index+=subpackets_length	

			packet = [packet_version, packet_type, subpackets]

		#Number of sub-packets
		else:
			subpackets_num = int(data_bin[index:index+11], base=2)
			if __debug__:
				print("Subpackets  num: " + str(subpackets_num))

			index+=11
			#Read subpackets
			for i in range(subpackets_num):
				subpacket,index = read_packet(data_bin, index)
				subpackets.append(subpacket)

			packet = [packet_version, packet_type, subpackets]

	return(packet, index)

def sum_versions(packets):
	total = 0
	for packet in packets:
		total+=packet[0]
		if type(packet[2]) != int:
			total+=sum_versions(packet[2])
	return total

file = open("input")

data_hex = file.read().strip()
#Format to keep leading 0s
data_bin = format(int(data_hex, base=16), '0'+str(len(data_hex)*4)+'b')

#Number of 0s at the end
possible_padding = len(data_bin) - len(data_bin.rstrip("0"))

packets = []
index = 0
while index<len(data_bin) and len(data_bin)-index > possible_padding:
	packet,index = read_packet(data_bin, index)
	packets.append(packet)

if __debug__:
	print(packets)
print(sum_versions(packets))