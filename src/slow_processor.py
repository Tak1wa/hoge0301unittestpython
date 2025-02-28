import time

class SlowProcessor:
    def process_data(self, data, sleep_time=2):
        """時間のかかる処理をシミュレート"""
        time.sleep(sleep_time)
        return data.upper()
    
    def complex_calculation(self, n, sleep_time=1):
        """複雑な計算をシミュレート"""
        time.sleep(sleep_time)
        result = sum(i * i for i in range(n))
        return result