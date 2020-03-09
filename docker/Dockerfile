FROM docker.0xhash.cn/node:9.4.0
RUN mkdir -p /opt/app && cd /opt/app && git clone https://github.com/handshake-org/hs-airdrop.git
RUN cd /opt/app/hs-airdrop && npm install -f --loglevel http
RUN mkdir -p /root/.hs-tree-data && cd /root/.hs-tree-data && wget https://github.com/handshake-org/hs-tree-data/raw/master/tree.bin
RUN mkdir -p /root/.hs-tree-data/nonces && cd /root/.hs-tree-data/nonces && wget https://github.com/handshake-org/hs-tree-data/raw/master/nonces/103.bin
