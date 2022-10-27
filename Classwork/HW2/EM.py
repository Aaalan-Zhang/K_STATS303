class TwoMeans(object):
    def __init__(self,SampData) -> None:
        super().__init__()
        self.Sample = SampData
        x_min, x_max, y_min, y_max = SampData[:,0].min(), SampData[:,0].max(), SampData[:,1].min(), SampData[:,1].max()
        self.miu1 = np.array([random.uniform(x_min,x_max),random.uniform(y_min,y_max)])
        self.miu2 = np.array([random.uniform(x_min,x_max),random.uniform(y_min,y_max)])
        self.labls = np.zeros(SampData.shape[0])
        # self.Estep()
        self.J = self.Estep()

    def Estep(self):
        theJ = 0 
        for i in range(self.Sample.shape[0]):
            d1, d2 = la.norm(self.Sample[i,:] - self.miu1), la.norm(self.Sample[i,:] - self.miu2)
            if (d1 < d2):
                theJ += d1
                self.labls[i] = 1
            else:
                theJ += d2 
                self.labls[i] = 2
        return theJ

    def Mstep(self):
        theJ  = 0
        # for i in range(self.Sample.shape[0]):
        OneLabl = (self.labls == 1)

        self.miu1 = self.Sample[OneLabl].mean(axis=0)
        self.miu2 = self.Sample[~OneLabl].mean(axis=0)

    def RunEM(self):
        lastJ  = self.J
        thisJ = lastJ - 1e5
        self.Mstep()
        while(abs(thisJ - lastJ) > 1e-10):
            lastJ = thisJ
            thisJ = self.Estep()
            self.J = thisJ
            self.Mstep()