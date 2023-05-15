from jsonseq.decode import JSONSeqDecoder

#Inizializziazione contatori e lista dei valori di RTT
sent_count = 0
recv_count = 0
total_rtt = 0
num_rtt = 0
rtt_list = []

# Lettura del file qlog e aggiornamento dei contatori sent_count e recv_count
with open("./Client/5204a9b1680f8f3a500e2cb7a1d1c0821ee.sqlog") as client:
    for obj in JSONSeqDecoder().decode(client):
        if 'name' in obj:
            name_dict = obj['name']
            if 'packet_received' in name_dict:
                 recv_count+=1
            if 'data' in obj:
                 data_dict = obj['data']
                 if 'latest_rtt' in data_dict:
                    rtt=obj['data']['latest_rtt']
                    total_rtt += rtt
                    num_rtt += 1
                    rtt_list.append(rtt)

with open("./Server/5ce59f211796efcf3ddcef78e7a14cd64a88a.sqlog") as server:
    for obj1 in JSONSeqDecoder().decode(server):
        if 'name' in obj1:
            name_dict = obj1['name']
            if 'packet_sent' in name_dict:
                 sent_count+=1

#Calcolo Packet Loss
packet_loss = (sent_count-recv_count) / sent_count * 100
print("Packet loss: {:.2f}%".format(packet_loss))

#Calcolo RTT
rtt_mean = total_rtt / num_rtt
print("RTT medio: {:.2f} ms".format(rtt_mean))