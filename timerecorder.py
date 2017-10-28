import time
class TimeCount:
    start_time = 0
    stop_time = 0
    together = 0
    ret = 0
    def __add__(self,  other):
        together = int.__add__(self.secs,  other.secs)
        return int(together)
    def __repr__(self):
        ret = getattr(self,  'secs',  '未开始计时')
        if isinstance(ret,  int):
            return int(ret)
        return int(ret)
    def start(self):
        self.start_time = time.time()
        print('start！')
    def stop(self):
        if self.start_time == 0:
            print('请先调用 start() 开始计时！')
        else:
            self.stop_time = time.time()
            self.secs = round(self.stop_time - self.start_time)
            return round(self.stop_time - self.start_time)