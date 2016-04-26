class DTLSContext(object):
    def __init__(self):
        self.identities = []
        self.trusted_peers = []

    def add_identity(self, keystore):
        self.identities.append(keystore)

    def add_trusted_peer(self, keystore):
        self.trusted_peers.append(keystore)

    def create_session(self, ip_addr, port):
        pass

    def is_trusted_peer(self, peer_keystore):
        pass

