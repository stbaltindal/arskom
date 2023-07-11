import mailbox

mbox_file = '/Users/burak/Desktop/ARSKOM/mlstore/dpdk-dev/git/0.git/objects/pack-99493df56b69c60f442bde04dc08f8418c16e928.pack'
mbox = mailbox.mbox(mbox_file)

for message in mbox:
    print('From:', message['From'])
    print('Subject:', message['Subject'])
    print('Body:', message.get_payload())
    print('---')