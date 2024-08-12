class StockSpanner:
    def __init__(self):
        self.st=[]
    def next(self, price: int) -> int:
        curr_span=1
        while self.st and self.st[-1][0]<=price:
            prev_price,prev_span=self.st.pop()
            curr_span+=prev_span
        self.st.append((price,curr_span))
        return curr_span