
class ReservationModel:
    def __init__(self, *, id, user_id, projection_id, row, col):
        self.id = id
        self.user_id = user_id
        self.projection_id = projection_id
        self.row = row
        self.col = col
