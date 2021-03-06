class kpi_databank:
    def __init__(self, consumption, ref_dispatch, synthetic_dispatch, prods_charac=None, loads_charac=None, prices=None):

        # Create Class variables
        self.consumption = consumption
        self.ref_dispatch = ref_dispatch
        self.syn_dispatch = synthetic_dispatch

        # Reindex to avoid problems
        # self.consumption.index.rename('Time', inplace=True)
        # self.ref_dispatch.index.rename('Time', inplace=True)
        # self.syn_dispatch.index.rename('Time', inplace=True)

        # Aggregate variables
        self.agg_conso = consumption.sum(axis=1)
        self.agg_ref_dispatch = ref_dispatch.sum(axis=1)
        self.agg_syn_dispatch = synthetic_dispatch.sum(axis=1)

        # Read grid characteristics (csv generated by notebook...)
        self.prod_charac = prods_charac
        self.load_charac = loads_charac
        self.prices = prices

        # # Check consisten information
        # try:
        #     if self.consumption.index.equals(self.ref_dispatch.index) \
        #         and self.ref_dispatch.index.equals(self.syn_dispatch.index) \
        #         and self.syn_dispatch.index.equals(self.consumption.index):
        #         pass
        # except:
        #     print ('Input data should have same time frame')

        # Months are used in multiple KPI's
        self.months = self.ref_dispatch.index.month.to_frame()
        self.months.index = self.ref_dispatch.index
        self.months.columns = ['month']

        # Set precision for percentage
        # output values
        self.precision = 1

        # Json to save all KPIs
        self.output = {}