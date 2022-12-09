def is_full(self, ):
    for row in self.board:
        for item in row:
            if item != 'x' or 'o':
                return False
        return True

