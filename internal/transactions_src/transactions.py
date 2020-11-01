import internal.shared_function.shared_function as shared_function


class transactions(object):
    def __init__(self):
        self._id = ""
        self._vin = []
        self._vout = []

    def __repr__(self):
        string = f"ID : {self._id}\n"
        string += "TXin : "
        for vin in self._vin:
            string += f"({vin}) "
        string += "\nTXout : "
        for vout in self._vout:
            string += f"({vout}) "
        return string

    @property
    def id(self):
        return self._id

    @property
    def vin(self):
        return self._vin

    @property
    def vout(self):
        return self._vout

    def set_id(self):
        self._id = self.hash()

    def hash(self):
        string = f"{self._id}"
        for vin in self._vin:
            string += f"{vin}"
        for vout in self._vout:
            string += f"{vout}"
        return shared_function.hash_string(string)

    def add_vin(self, txin):
        self._vin.append(txin)

    def add_vout(self, txout):
        self._vout.append(txout)

