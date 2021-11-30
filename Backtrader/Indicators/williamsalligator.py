class WilliamsAlligator(bt.Indicator):
    lines = ('jaw', 'teeth', 'lips',)
    params = (
        ('jaw_period', 13),
        ('teeth_period', 8),
        ('lips_period', 5),
        ('jaw_offset', 8),
        ('teeth_offset', 5),
        ('lips_offset', 3),
    )
    plotinfo = dict(plot = True,
                    subplot=False,
                    plotname='Williams Alligator'
                    )

    def __init__(self):
        self.jaw = self.l.jaw = bt.ind.SmoothedMovingAverage(self.data, period = self.p.jaw_period)(-self.p.jaw_offset)
        self.teeth = self.l.teeth = bt.ind.SmoothedMovingAverage(self.data, period = self.p.teeth_period)(-self.p.teeth_offset)
        self.lips = self.l.lips = bt.ind.SmoothedMovingAverage(self.data, period = self.p.lips_period)(-self.p.lips_offset)

    def next(self):
        pass