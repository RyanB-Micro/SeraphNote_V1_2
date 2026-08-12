

class Sheet:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.node_list = []
        self.fact_list = []
        self.source_list = []
        self.quote_list = []
        self.bond_list = []
        self.tools_list = []

        self.datum = [0,0]
        self.datum_range = [100, 100]

    def add_node(self):
        pass

    def add_fact_node(self):
        pass

    def update_datum(self, dy, dx):
        self.datum[0] += dy
        self.datum[1] += dx

        # Clamping datum range
        if self.datum[0] > self.datum_range[0]:
            self.datum[0] = self.datum_range[0]
        if self.datum[0] < -self.datum_range[0]:
            self.datum[0] = -self.datum_range[0]
        if self.datum[1] > self.datum_range[1]:
            self.datum[1] = self.datum_range[1]
        if self.datum[1] < -self.datum_range[1]:
            self.datum[1] = -self.datum_range[1]

    def data_out(self):
        data = {
            'sheet_name': self.sheet_name,
            'node_list': self.node_list,
            'fact_list': self.fact_list,
            'source_list': self.source_list,
            'quote_list': self.quote_list,
            'bond_list': self.bond_list,
            'tools_list': self.tools_list,
            'datum': self.datum
        }
        return data

    def data_in(self, data):

        self.sheet_name = data['sheet_name']
        self.node_list = data['node_list']
        self.fact_list = data['fact_list']
        self.source_list = data['source_list']
        self.quote_list = data['quote_list']
        self.bond_list = data['bond_list']
        self.tools_list = data['tools_list']
        self.datum  = data['datum']

        return data
