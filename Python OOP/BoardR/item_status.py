class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    @classmethod
    def next(cls, current):
        if current == ItemStatus.OPEN:
            return ItemStatus.TODO
        elif current == ItemStatus.TODO:
            return ItemStatus.IN_PROGRESS
        elif current == ItemStatus.IN_PROGRESS:
            return ItemStatus.DONE
        elif current == ItemStatus.DONE:
            return ItemStatus.VERIFIED
        elif current == ItemStatus.VERIFIED:
            return ItemStatus.VERIFIED

    @classmethod
    def previous(cls, current):
        if current == ItemStatus.OPEN:
            return ItemStatus.OPEN
        elif current == ItemStatus.TODO:
            return ItemStatus.OPEN
        elif current == ItemStatus.IN_PROGRESS:
            return ItemStatus.TODO
        elif current == ItemStatus.DONE:
            return ItemStatus.IN_PROGRESS
        elif current == ItemStatus.VERIFIED:
            return ItemStatus.DONE
